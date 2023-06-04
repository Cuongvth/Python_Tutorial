import arrayDemo
import dequeDemo
import bisectDemo
import heapqDemo

selection = "-1"
while selection != "0":
    print("----------------------------Menu----------------------------")
    print("1. arrayDemo")
    print("2. dequeDemo")
    print("3. bisectDemo")
    print("4. heapqDemo")
    print("0. Exit")
    print("----------------------------Menu----------------------------")
    selection = input("Enter selection: ")
    if selection == "1":
        arrayDemo.Demo()
    elif selection == "2":
        dequeDemo.dequeDemo.Demo()
    elif selection == "3":
        bisectDemo.Demo()
    elif selection == "4":
        heapqDemo.Demo()
    elif selection == "0":
        exit()
    else:
        print("Again")
