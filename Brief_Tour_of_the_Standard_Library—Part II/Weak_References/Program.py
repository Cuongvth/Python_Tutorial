import Weak_References

selection = "-1"
while selection != "0":
    print("----------------------------Menu----------------------------")
    print("1. Sửa dữ liệu")
    print("2. In dữ liệu")
    print("3. Xóa dữ liệu")
    print("4. Thu hồi bộ nhớ")
    print("0. Exit")
    print("----------------------------Menu----------------------------")
    selection = input("Enter selection: ")
    if selection == "1":
        Weak_References.Weak_References.Demo()
    elif selection == "2":
        Weak_References.Weak_References.Demo4()
    elif selection == "3":
        Weak_References.Weak_References.Demo2()
    elif selection == "4":
        Weak_References.Demo3()
    elif selection == "0":
        exit()
    else:
        print("Again")
