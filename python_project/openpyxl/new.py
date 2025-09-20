import openpyxl

wb = openpyxl.Workbook()

sheet = wb.active

sheet.cell(row=1,column=1).value = "dahdi dan mutia sabrina"

wb.save('new.xlsx')
print('berhasil')
