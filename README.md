Lubility is just a little utility I made for my wife to save her a bunch of time by renaming all of her photo files in a directory with YYYY-MM-DD format, followed by a number in parentheses indicating the order it was taken on that specific day.

So for instance, if she had three pictures in a file, two of them taken on September 1, 2022 (one at 8:00 am, one at 10:00 am), and another taken September 2, 2022, they would be renamed like this:
2022-09-01 (1)   <-- _the one taken at 8:00 am_
2022-09-01 (2)   <-- _the one taken at 10:00 am_
2022-09-02 (1)

It only works on Windows and only on jpeg files.

To use it you can just use the .exe found in the `dist` folder.

To generate executable:
Run the following command: pyinstaller --onefile --name Lubility app/main.py
This will generate a single executable file in a dist directory within the current directory.