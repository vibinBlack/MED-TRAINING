"""
Creating module named meetings to build the functionality of creating, reading, updating csv files\
    of Data consisting Employee, in time and out time.
"""
import csv
from tempfile import NamedTemporaryFile
import shutil
import pandas


def create_and_write_csv():
    """ function to create and write a csv file """
    filename = input("Give the filename : ") + ".csv"
    fieldnames = [i.strip() for i in input("Enter the column or fieldnames\
 separated with a comma : ").split(',')]
    rows = int(input("Enter the number of rows : "))
    mylist = []
    for i in range(1, rows + 1):
        mydict = {}
        for j in fieldnames:
            mydict[j] = input(f"Enter the {j} for row {i} : ")
        mylist.append(mydict)
    with open(filename, 'w', encoding='UTF-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(mylist)
        file.close()


def read_csv():
    """ function to read csv file """
    filename = input("Enter the filename you want to read : ") + ".csv"
    # with open(filename, 'r', encoding = 'UTF-8') as file:
    #     reader = csv.reader(file)
    #     print("\nReading csv in the form of lists ")
    #     for lines in reader:
    #         print(lines)

    # with open(filename, 'r', encoding = 'UTF-8') as file:
    #     reader_dict = csv.DictReader(file)
    #     print("\nReading csv in the form of ordered dictionary ")
    #     for lines in reader_dict:
    #         print(lines)
    print("\nReading csv using pandas")
    reader_pandas = pandas.read_csv(filename)
    return reader_pandas.to_string()


def append_csv():
    """ function to append data in csv """
    filename = input("Enter the filename in which you want to append the data : ") + ".csv"
    select = input("Do you want to add any extra column ? (Y for yes or any other key for No) ")
    with open(filename, 'r', encoding='UTF-8') as file_read, \
            open(filename, 'a', encoding='UTF-8', newline='\n') as file:
        reader = csv.DictReader(file_read)
        field_names = reader.fieldnames
        total_rows = len(list(reader))
        new_columns = []
        if select in ('Y', 'y'):
            new_columns = [i.strip() for i in input("Enter the column or\
 fieldnames you want to add separated with a comma : ").split(',')]
            field_names.extend(new_columns)
        rows = int(input("Enter the number of rows you want to append: "))
        mylist = []
        for i in range(total_rows + 1, total_rows + rows + 1):
            mydict = {}
            for j in field_names:
                mydict[j] = input(f"Enter the {j} for row {i} : ")
            mylist.append(mydict)
        if select in ('y', 'Y'):
            file_write = NamedTemporaryFile(mode='w', delete=False)
            with open(filename, 'r', encoding='UTF-8') as file_read_again, file_write:
                reader = csv.DictReader(file_read_again)
                writer = csv.DictWriter(file_write, fieldnames=field_names)
                writer.writeheader()
                for i in new_columns:
                    for j in reader:
                        j[i] = ''
                        writer.writerow(j)
                file_write.close()
            shutil.move(file_write.name, filename)
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writerows(mylist)
        file.close()
