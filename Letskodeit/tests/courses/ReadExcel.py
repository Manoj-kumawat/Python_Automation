from utilities.read_data import getExcelData
import os
import xlrd
import openpyxl

BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(BASEDIR)
TESTDATA_FILE_PATH = os.path.join(BASEDIR,'test_data_sheet.xlsx')

def getExcelData(filePath, sheetName):
    wb = xlrd.open_workbook(filePath)
    sheet = wb.sheet_by_name(sheetName)
    total_row = sheet.nrows
    rows = []
    for r in range(1, total_row):
        rows.append(sheet.row_values(r))
    return rows

def writeExcelData(filePath, sheetName, status):
    wb = openpyxl.load_workbook(filePath)
    sheet = wb[sheetName]
    count = 2
    for st in status:
        sheet['G'+str(count)] = st
        count += 1
    wb.save(filePath)
        
getExcelData(TESTDATA_FILE_PATH, "TestData")

writeExcelData(TESTDATA_FILE_PATH, "TestData", ["Pass", "Fail"])