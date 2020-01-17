import csv
import os

os.chdir(r"C:\\Users\\Usuario\\Documents\\Adrian\\Python\\Python Practices\\CVS") 
print(os.getcwd())


with open('colors.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)
    print(dates)
    print(colors)

    
    # now, remember our lists?

    whatColor = input('What color do you wish to know the date of?:')
    coldex = colors.index(whatColor)
    theDate = dates[coldex]
    print('The date of',whatColor,'is:',theDate)