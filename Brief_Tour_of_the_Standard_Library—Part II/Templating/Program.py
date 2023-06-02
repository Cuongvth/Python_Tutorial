import TemplateDemo

selection = "-1"
while selection != "0":
    print("----------------------------Menu----------------------------")
    print("1. TemplateDemo")
    print("2. TemplateDemoOther")
    print("0. Exit")
    print("----------------------------Menu----------------------------")
    selection = input("Enter selection: ")
    if selection == "1":
        TemplateDemo.Demo()
    elif selection == "2":
        TemplateDemo.DemoOther()
    elif selection == "0":
        exit()
    else:
        print("Again")
