import csv
import openpyxl as openpyxl
from openpyxl import Workbook

with open('dictwriter.csv', 'r', encoding='utf-8', newline='') as data:
    file_reader = csv.reader(data)
    for row in file_reader:
        print(', '.join(row))

excel_file = Workbook()
excel_file = openpyxl.load_workbook('records.xlsx')

