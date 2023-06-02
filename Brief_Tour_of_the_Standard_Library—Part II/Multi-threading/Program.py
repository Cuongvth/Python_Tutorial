import Multi_threadingDemo

selection = "-1"
while selection != "0":
    print("----------------------------Menu----------------------------")
    print("1. Multi_threadingDemo")
    print("0. Exit")
    print("----------------------------Menu----------------------------")
    selection = input("Enter selection: ")
    if selection == "1":
        Multi_threadingDemo.Demo()
    elif selection == "0":
        exit()
    else:
        print("Again")
