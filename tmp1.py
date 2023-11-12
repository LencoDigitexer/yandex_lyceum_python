import xlsxwriter
import sys
from collections import defaultdict
 
 
workbook = xlsxwriter.Workbook('statement.xlsx')
worksheet = workbook.add_worksheet("Sheet_1")
 
data = sys.stdin.readlines()
data = [line.rstrip() for line in data]
 
d = []
n = int(data[-1])
data.pop(-1)
 
for i in data:
    i = i.split("\t")
    d.append(i)
 
data = d
row = 1
 
cell_format = workbook.add_format({'bold': True})
 
worksheet.write(0, 0, "employee", cell_format)
worksheet.write(0, 1, "department", cell_format)
worksheet.write(0, 2, "work", cell_format)
worksheet.write(0, 3, "payment", cell_format)
 
department = set()
 
bv = []
for i in range(0, len(data)):
    row += 1
    department.add(data[i][1])
    worksheet.write(i + 1, 0, data[i][0])
    worksheet.write(i + 1, 1, data[i][1])
    worksheet.write(i + 1, 2, int(data[i][2]))
    worksheet.write(i + 1, 3, int(data[i][2]) * n)
    bv.append(int(data[i][2]) * n)
 
#########
b = []
for i in department:
    b.append(i)
department = b
department.sort()
 
worksheet2 = workbook.add_worksheet("Sheet_2")
 
worksheet2.write(0, 0, "department", cell_format)
worksheet2.write(0, 1, "total work", cell_format)
worksheet2.write(0, 2, "total cost", cell_format)
 
c = 0
m = 0
for i in range(0, len(department)):
    worksheet2.write(i + 1, 0, department[i])
    for j in range(len(data)):
        if data[j][1] == department[i]:
            c += int(data[j][2])
            m += bv[j]
    worksheet2.write(i + 1, 1, c)
    worksheet2.write(i + 1, 2, m)
    c = 0
    m = 0
 
workbook.close()