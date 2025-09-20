from openpyxl import workbook
from openpyxl import *

h= Workbook
k = h.active


k.cell(row=1,column=1).value = 'halo dunia'
#menyimpan file excel
h.save('baru.xlsx')



# class baru:
#     def __init__(self,j,l):
#         self.k = j
#         self.l = l
        
#     def op(self):
#         h = self.k
#         o = self.l * h
#         return o
        
        
# ui = baru(89,89)
# print(ui.op())