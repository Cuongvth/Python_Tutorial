from Company import Company

selection = "-1"
while selection != "0":
    print("----------------------------Menu----------------------------")
    print("1. Read")
    print("2. Write")
    print("3. Show")
    print("4. Add")
    print("5. Delete All")
    print("0. Exit")
    print("----------------------------Menu----------------------------")
    selection = input("Enter selection: ")
    if selection == "1":
        Company.readJson()
    elif selection == "2":
        Company.writeJson()
    elif selection == "3":
        Company.show()
    elif selection == "4":
        Company.addManager()
    elif selection == "5":
        Company.deleteAll()
    elif selection == "0":
        exit()
    else:
        print("Again")
