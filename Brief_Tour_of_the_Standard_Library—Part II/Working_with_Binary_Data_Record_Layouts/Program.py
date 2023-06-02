import structDemo

selection = "-1"
while selection != "0":
    print("----------------------------Menu----------------------------")
    print("1. structDemo")
    print("0. Exit")
    print("----------------------------Menu----------------------------")
    selection = input("Enter selection: ")
    if selection == "1":
        structDemo.Demo()
    elif selection == "0":
        exit()
    else:
        print("Again")
