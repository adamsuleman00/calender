#Calendar Final Version (Python 3.x)
#Adam Suleman

from datetime import datetime
from time import strftime, sleep

#main function, displays menu
def chooseFunction():
    while True:
        try:
            sleep(2)
            print("\ni.    Import entries from a file (will delete existing entries)\nv.    View all entries\na.    Add a new entry\ne.    Edit existing entries\ns.    Save entries to a file")
            choice = input("Choose a character from above: ").strip().lower()
            if choice == "i":
                importFromFile() 
            elif choice == "v":
                viewAllEntries()
            elif choice == "a":
                add()
            elif choice == "e":
                edit()
            elif choice == "s":
                saveToFile()
            else:
                pass
        except ValueError:
            pass

#function to obtain date:
#validates date to exist before accepting, loops until correct input received
def getDate():
    while True:
        try:
            dateInput = input("\nPlease input a date (dd/mm/yyyy):\n")
            date = validateDate(dateInput)
            return(date)
        except ValueError:
            print("Invalid date, please try again")

#function which validates a given date
#year must be four digits long, and the datetime module must be able to verify the date exists
def validateDate(dateInput):
        dd, mm, yyyy = dateInput.split("/")
        if len(str(int(yyyy))) != 4:
            raise ValueError
        date = datetime(int(yyyy), int(mm), int(dd))
        return(date)

#general function to get a string from the user (i.e. diary entry)
def getString(prompt):
    while True:
        stringInput = input(prompt).strip()
        if len(stringInput) != 0:
            return(stringInput)

#display all entries to user
def viewAllEntries():
    print()
    for pair in entryList:
        date = pair[0]
        entry = pair[1]
        viewEntry(date, entry)

#function to display an entry
#string format function is used to display date objects as readable dates
def viewEntry(date, entry):
    print(date.strftime("\n%d/%m/%Y:\n") + entry)

#add function:
def add():
    date = getDate()
    entry = getString("\nPlease input an entry:\n")
    addEntry(date, entry)

def addEntry(date, entry):

    #check if date entered by user is already in diary
    index = searchEntriesForDate(date)
     
    #if date is not in diary, create new entry
    if index is None:  
        entryList.append([date,entry])
        entryList.sort()
                
    #if date already exists, append to the old entry
    else:
        oldEntry = entryList[index][1]
        entryList[index][1] = oldEntry + ";" + entry

#check if a date already exists in diary, return entry's index within entryList
def searchEntriesForDate(inputDate):
    for index, pair in enumerate(entryList):
        date = pair[0]
        if inputDate == date:
            return(index)
    return(None)

#edit function:
#allows user to edit an existing entry by date
def edit():
    inputDate = getDate()
    index = searchEntriesForDate(inputDate)

    #if no such entry for given date, alert user
    if index is None:
        print("Date not found in diary")

    #if entry exists for given date, obtain previous date and entry from entryList:
    #display to previous entry to user and ask for a new entry to replace it
    else:
        pair = entryList[index]
        date = pair[0]
        entry = pair[1]
        viewEntry(date, entry)
        newEntry = getString("\nPlease input a new entry for this date:\n")
        entryList[index][1] = newEntry
        viewAllEntries()

#import function:
def importFromFile():

    #ask user for filename, store all lines from file in 'lines' list
    while True:
        try:
            filename = input("\nEnter filename with extension:\n")
            with open(filename, 'r') as file:
                lines = file.readlines()
                break
        except FileNotFoundError:
            print("File does not exist")

    #clear previous diary
    entryList.clear()

    #attempt to split each line at commas: (date,entry)
    #validate date and entry for each line:
    #if format is incorrect the line is skipped and not added to diary
    for line in lines:
        try:
            values = line.split(",")
            dateInput = values[0].strip()
            date = validateDate(dateInput)
            entry = values[1].strip()
            addEntry(date,entry)
        except ValueError:
            continue
        except IndexError:
            continue
    
    viewAllEntries()

#save function:
#ask user for output filename, write all values in entryList to this file
def saveToFile():
    filename = getString("\nPlease input filename to save as:\n") + ".txt"
    with open(filename, 'w') as file:
        for pair in entryList:
            date = pair[0]
            entry = pair[1]
            file.write(date.strftime("%d/%m/%Y") + "," + entry + "\n")

def main():
    chooseFunction()

#create empty entryList which stores date, entry pairs in sublists
entryList = []
main()
