import textwrapDemo
import reprlibDemo
import pprintDemo
import localeDemo

selection = "-1"
while selection != "0":
    print("----------------------------Menu----------------------------")
    print("1. reprlibDemo")
    print("2. textwrapDemo")
    print("3. pprintDemo")
    print("4. localeDemo")
    print("0. Exit")
    print("----------------------------Menu----------------------------")
    selection = input("Enter selection: ")
    if selection == "1":
        reprlibDemo.Demo()
    elif selection == "2":
        textwrapDemo.Demo()
    elif selection == "3":
        pprintDemo.Demo()
    elif selection == "4":
        localeDemo.Demo()
    elif selection == "0":
        exit()
    else:
        print("Again")
