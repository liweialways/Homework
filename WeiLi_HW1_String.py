
# coding: utf-8

# In[2]:


"""
Homework 1
program: SalesReport.py
student: Wei Li


present a manager's sales report:
1. the inputs are:
    sales.txt
    manager's name:
    
2. computation and outputs are:
    title: Monthly Sales Report for ...
    header: Month Qty Price Revenue
    content: sales records of a certain manager
    
3. the total revenue is also showed at the end.
"""

# input and read the file:
fileName = input('Enter the file name:')
manager = input('Enter the manager name:')
file = open(fileName, 'r').readlines()

# print the title and header:
print('Monthly Sales Report for ' + manager)
print('%-7s%-5s%-8s%-9s'%('Month','Qty','Price','Revenue'))

# convert 'file' into a list of lists:
splitedFile = []
for j in range(len(file)):
    splitedFile.append(file[j].split())

# set the initial total revenue for any manager is zero
Total = 0

# print report for the manager:
for k in range(len(splitedFile)):
    if manager == splitedFile[k][1]:
        Month = int(splitedFile[k][0])
        Qty = int(splitedFile[k][2])
        Price = float(splitedFile[k][3])
        Revenue = float(splitedFile[k][2])*float(splitedFile[k][3])
        Total += Revenue
        print('%-7d%-5d%-8.2f%-9.1f'%(Month, Qty, Price, Revenue))

# print the conclusion sentence:
print('Total revenue is ' + str(Total) + '.')

