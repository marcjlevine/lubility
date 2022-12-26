from app.file_details import FileDetails
from datetime import datetime
from time import strftime
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from typing import List
import exifread

window = tk.Tk()
window.title('Lubility - The Luba Utility')
window.geometry("600x300")
header_text = tk.Label(text='Hi Luba! \nThis will rename your photos the way you like.', 
    font=('Comic Sans MS', 18),
    wraplength=550,
    justify='left')
header_text.pack(side='top', anchor='w', padx=10, pady=10)

TAG_DATE_FORMAT = '%Y:%m:%d %H:%M:%S'
TARGET_DATE_FORMAT = '%Y-%m-%d'
EXIF_DATE_TAG = 'EXIF DateTimeOriginal'
DIRECTORY_LABEL = 'directory_label'
DO_IT_BUTTON_NAME = 'do_it_button'

selected_directory = 'default'

def show_error(ex: Exception):
    messagebox.showerror(title='Shit happens ¯\_(ツ)_/¯', 
        message=f"Well...  shit.  That didn't work.  Show this to Marc: \n {str(ex)}")

def show_success():
    messagebox.showinfo(title="Success, yay!", 
        message="It worked!  Wow, your husband must be awesome.  To thank him please go give him a giant kiss.")

def get_sorted_files(directory: str) -> List[FileDetails]:
    files: List[FileDetails] = []

    for filename in os.listdir(directory):
        if not filename.endswith('.jpg'):
            continue

        filepath = os.path.join(directory, filename)
        with open(filepath, 'rb') as f:
            tags = exifread.process_file(f)
            pic_timestamp = datetime.strptime(tags.get(EXIF_DATE_TAG).values, TAG_DATE_FORMAT)
            new_filename_datepart = pic_timestamp.strftime(TARGET_DATE_FORMAT)
            next_file = FileDetails(filename, pic_timestamp, new_filename_datepart)

            i = 0
            file_number = 1
            file_inserted = False

            while i <= len(files) and not file_inserted:
                # insert at end or beginning
                if i == len(files) or pic_timestamp < files[i].date_taken:
                    insert_file(files, new_filename_datepart, next_file, i, file_number)
                    file_inserted = True
                    continue

                if new_filename_datepart == files[i].formatted_date_taken: 
                    file_number += 1

                i += 1
                if pic_timestamp > files[i-1].date_taken and (i == len(files) or pic_timestamp < files[i].date_taken): 
                    insert_file(files, new_filename_datepart, next_file, i, file_number)
                    file_inserted = True

    return files

def insert_file(files, new_filename_datepart, next_file, index, file_number):
    next_file.file_number = file_number
    files[index:index] = [next_file]

    next_file = index + 1
    while next_file < len(files) and new_filename_datepart == files[next_file].formatted_date_taken:
        files[next_file].file_number += 1
        next_file += 1

def rename_files(directory, files):
    for file in files:
        os.rename(directory + '/' + file.file_name, directory + '/' + file.new_file_name())

def select_directory():
    global selected_directory
    selected_directory = filedialog.askdirectory()
    window.configure(cursor="watch")
    try:
        selected_directory_label = tk.Label(text=f"Selected directory: {selected_directory}", name=DIRECTORY_LABEL)
        selected_directory_label.pack(anchor='nw', padx=10, pady=10)
        go_button = tk.Button(text='Do it!', 
            command=go, 
            name=DO_IT_BUTTON_NAME,
            font=('Arial', 12))
        go_button.pack(anchor='nw', padx=10)
    except:
        show_error()
    finally:
        window.configure(cursor="arrow")

def go():
    window.configure(cursor="watch")
    try:
        sorted_files = get_sorted_files(selected_directory)
        rename_files(selected_directory, sorted_files)
        window.children[DIRECTORY_LABEL].pack_forget()
        window.children[DO_IT_BUTTON_NAME].pack_forget()
        show_success()
    except Exception as ex:
        show_error(ex)
    finally:
        window.configure(cursor="arrow")


button = tk.Button(window, 
    text="Select Directory", 
    command=select_directory, 
    font=('Arial', 12))
button.pack(anchor='nw', padx=10, pady=5)

window.mainloop()