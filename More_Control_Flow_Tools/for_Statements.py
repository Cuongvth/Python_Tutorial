def Demo():
    arr = {}
    key = "fake"
    while key != "":
        key = input("Key: ")
        if key != "":
            arr[key] = input("Value: ")
    for k, v in arr.items():
        print(f"Key: {k}, Value: {v}")
