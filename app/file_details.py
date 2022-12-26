from datetime import date

class FileDetails:
    def __init__(self, file_name, date_taken, formatted_date_taken = None, file_number = None) -> None:
        self.file_name = file_name
        self.date_taken = date_taken
        self.formatted_date_taken = formatted_date_taken
        self.file_number = file_number

    file_name: str
    date_taken: date
    formatted_date_taken: str
    file_number: int

    def new_file_name(self) -> str:
        return f'{self.formatted_date_taken} ({str(self.file_number)}).jpg'