#!/usr/bin/env python
import csv
import re

"""
This code deals with loading data from two files and saving changes when done.
This code can accept database operation for find and insert
Examples of command
    Find order EmployeeID=5, ShipCountry=Brazil
    Insert customer ("ALFKI","Alfreds Futterkiste","Maria Anders","Sales Representative","Obere Str.57","Berlin","null","12209","Germany","030-0074321","030-0076545")
When inserting a new line. Make sure to use null when wanting to leave a plaec blank
"""
# csv reader 's indice is integer while cvs DictReader uses indice of the firstrow str
userInput = raw_input('please enter your instruction')
userInput2 = re.split('\"|,|\(|\)| ', userInput)
userInput2 = [item for item in filter(lambda x:x != '', userInput2)]
userInput3 = re.split('\"|,|\(|\)', userInput)
userInput3 = [item for item in filter(lambda x:x != '', userInput3)]
if userInput2[0]=='Find':
    if userInput2[1] == 'order':
        with open('orders.csv') as csvfile:
            readCSV = csv.DictReader(csvfile, delimiter=',')
            findOrNot = False
            for row in readCSV:
                isthis = True
                index = 2
                #Find order OrderID=10248, CustomerID=VINET
                while(index < len(userInput2)):
                    indexparse = re.split('=', userInput2[index])
                    isthis = isthis and (row[indexparse[0]] == indexparse[1])
                    index=index+1
                if (isthis):
                    print(row)
                    findOrNot=True
        if(findOrNot==False):
            print"Sorry, we don't have this query"
    if(userInput2[1]=='customer'):
        with open('customers.csv') as csvfile:
            readCSV = csv.DictReader(csvfile, delimiter=',')
            findOrNot = False
            for row in readCSV:
                isthis = True
                index = 2
                while(index < len(userInput2)):
                    indexparse = re.split('=', userInput2[index])
                    isthis = isthis and (row[indexparse[0]] == indexparse[1])
                    index=index+1
                if (isthis):
                    print(row)
                    findOrNot=True
        if(findOrNot==False):
            print"Sorry, we don't have this query"
# When inserting things into file. Null is needed for the field which tends to left as blank
if userInput2[0]=='Insert':
    if userInput2[1]=='order':
        userInput3=userInput3[1:len(userInput3)]
        with open('orders.csv', 'a') as csvfile:
            writeCSV = csv.writer(csvfile, delimiter=",")
            writeCSV.writerow(userInput3)
    if userInput2[1]=='customer':
        userInput3=userInput3[1:len(userInput3)]
        with open('customers.csv', 'a') as csvfile:
            writeCSV = csv.writer(csvfile, delimiter=",")
            writeCSV.writerow(userInput3)
  # Insert customer ("ALFKI","Alfreds Futterkiste","Maria Anders","Sales Representative","Obere Str.57","Berlin","","12209","Germany","030-0074321","030-0076545")

