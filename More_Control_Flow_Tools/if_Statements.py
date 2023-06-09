def Demo():
    try:
        x = int(input("Please enter an integer: "))
    except Exception as ex:
        print(ex)
        return
    if x < 0:
        print(f"{x} < 0")
    elif x == 0:
        print(f"{x} = 0")
    else:
        print(f"{x} > 0")
