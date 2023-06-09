def Demo():
    try:
        args = [int(input("Min: ")), int(input("Max: "))]
        print(list(range(*args)))
    except Exception as ex:
        print(ex)
