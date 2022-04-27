from openpyxl import Workbook
import traceback

class DataBooks():
    def __init__(self):
        print(self)

    def addBook(self):
        try:
            book = Workbook()
            sheet = book.active

            rows = [
                [888, 146, 157],
                [189, 138, 112],
                [23, 59, 78],
                [56, 21, 98],
                [24, 18, 43],
                [34, 15, 67]
            ]

            for row in rows:
                sheet.append(row)

            book.save('appending.xlsx')
        except Exception:
           print("DataBooks.addBook error: ",traceback.print_exc())