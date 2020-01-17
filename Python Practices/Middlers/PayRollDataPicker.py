import csv
import os

os.chdir(r"C:\\Users\\Usuario\\Documents\\Adrian\\Python\\Python Practices\\CVS") 
print(os.getcwd())
LIST_INTERVIEWER_ID= [] 
LIST_INTERVIEWER_NAME= []
LIST_DATE= []
LIST_START_TIME= []
LIST_END_TIME= []
LIST_HOURS_TOTAL= []
LIST_DIALED_PROJECTS= []
LIST_EXTENSIONS= []
LIST_BREAK_TIME= []
LIST_LUNCH_TIME= []
LIST_MEETING_TIME= []
LIST_BREAK_TIMEDISCOUNT= []k
LIST_LUNCH_TIMEPAID= []
LIST_PAID_HOURS = []

with open('clockinout.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        INTERVIEWER_ID = row[0]
        INTERVIEWER_NAME  = row[1]
        DATE  = row[2]
        START_TIME  = row[3]
        END_TIME  = row[4]
        HOURS_TOTAL  = row[5]
        DIALED_PROJECTS  = row[6]
        EXTENSIONS  = row[7]
        BREAK_TIME  = row[8]
        LUNCH_TIME  = row[9]
        MEETING_TIME  = row[10]
        BREAK_TIMEDISCOUNT  = row[11]
        LUNCH_TIMEPAID  = row[12]
        PAID_HOURS  = row[13]

        LIST_INTERVIEWER_ID.append(INTERVIEWER_ID)
        LIST_INTERVIEWER_NAME.append(INTERVIEWER_NAME)
        LIST_DATE.append(DATE)
        LIST_START_TIME.append(START_TIME)
        LIST_END_TIME.append(END_TIME)
        LIST_HOURS_TOTAL.append(HOURS_TOTAL)
        LIST_DIALED_PROJECTS.append(DIALED_PROJECTS)
        LIST_EXTENSIONS.append(EXTENSIONS)
        LIST_BREAK_TIME.append(BREAK_TIME)
        LIST_LUNCH_TIME.append(LUNCH_TIME)
        LIST_MEETING_TIME.append(MEETING_TIME)
        LIST_BREAK_TIMEDISCOUNT.append(BREAK_TIMEDISCOUNT)
        LIST_LUNCH_TIMEPAID.append(LUNCH_TIMEPAID)
        LIST_PAID_HOURS.append(PAID_HOURS)
    
    harmondID = input('What ID you wish to know the name of?:')
    matchingName = LIST_INTERVIEWER_ID.index(harmondID)
    result = LIST_INTERVIEWER_NAME[matchingName]
    print('The Name of ID: ',harmondID,' is: ',result)


 