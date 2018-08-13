import csv

def getCSVData(fileName):
    #Create a empty list to store rows
    rows = []
    #Open the CSV file
    datafile = open(fileName, 'r')
    #Create a CSV Reader from CSV File
    csvreader = csv.reader(datafile)
    #Skip the headers
    fields = next(csvreader)
    #Add rows from reader to list
    for row in csvreader:
        rows.append(row)
    return rows
