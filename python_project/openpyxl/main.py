from openpyxl import Workbook,load_workbook
# import pyscript
sel = load_workbook('ini.xlsx')
kotak = sel.active
sheet = sel['Sheet']
op = ['a','b','c','d']
h= 'A'
h += '1'
op[2] = h 
i=''
for i in op[2]:
    print(i)
    print(op)


sheet[op[2]] = 20
# sheet['A2'] = 20
# sheet['A3'] = sheet['A1'].value * sheet['A2'].value
# print(sheet['A1'],sheet['A2'],sheet['A3'])
#print(sel.sheetnames)
# kotak.cell(row=1,column=1).value= '1'
# kotak.cell(row=2,column=1).value='2'
# kotak.cell(row=3,column=1).value='hello \n world'
print(sheet['A1'].value)
sel.save('ini.xlsx')
