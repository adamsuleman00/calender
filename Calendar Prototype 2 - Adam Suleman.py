#Calendar Prototype 2 (Python 3.x)
#Adam Suleman

#main function, displays menu
def chooseFunction():
    while True:
        try:
            print("\nv.    View all entries\na.    Add a new entry\ne.    Edit existing entries")
            choice = input("Choose a character from above: ").strip().lower()
            if choice == "v":
                viewAllEntries()
            elif choice == "a":
                add()
            elif choice == "e":
                edit()
            else:
                pass
        except ValueError:
            pass

#display all entries to user
def viewAllEntries():
    print()
    for pair in entryList:
        date = pair[0]
        entry = pair[1]
        print(date + ": " + entry)

#add function:
def add():
    date = input("\nPlease input a date (dd/mm/yyyy):\n")
    entry = input("\nPlease input an entry:\n")
    entryList.append([date,entry])


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
    
    date = input("\nPlease input a date (dd/mm/yyyy):\n")
    index = searchEntriesForDate(date)

    #if no such entry for given date, alert user
    if index is None:
        print("Date not found in diary")

    #if entry exists for given date, obtain previous date and entry from entryList:
    #display to previous entry to user and ask for a new entry to replace it
    else:
        newEntry = input("\nPlease input a new entry for this date:\n")
        entryList[index][1] = newEntry
        viewAllEntries()

def main():
    chooseFunction()

#create empty entryList which stores date, entry pairs in sublists
entryList = []
main()
