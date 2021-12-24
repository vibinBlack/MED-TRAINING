import csv 

rows_data=[]

with open("business-financial-data-sep-2021-quarter.csv",'r') as file:
    csvreader = csv.reader(file)
    columns_heading = next(csvreader)

    for row in csvreader:
        rows_data.append(row) 

print(columns_heading)
print(rows_data)
