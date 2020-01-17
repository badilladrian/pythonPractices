import csv
import os

print(os.getcwd())
os.chdir(r"C:\\Users\\Usuario\\Documents\\Adrian\\Python\\Python Practices") 
print(os.getcwd())

with open('clockinout.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
    print(f'Processed {line_count} lines.')