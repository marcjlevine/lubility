from datetime import date
import os

class FileDetails:
    def __init__(self, file_name, date_taken, formatted_date_taken = None, file_number = None) -> None:
        self.file_name = file_name
        self.date_taken = date_taken
        self.formatted_date_taken = formatted_date_taken
        self.file_number = file_number
        self.original_extension = os.path.splitext(file_name)[1].lower()

    file_name: str
    date_taken: date
    formatted_date_taken: str
    file_number: int
    original_extension: str

    def new_file_name(self) -> str:
        return f'{self.formatted_date_taken} ({str(self.file_number)}){self.original_extension}'