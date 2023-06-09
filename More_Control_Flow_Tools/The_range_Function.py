def Demo():
    try:
        arr = range(int(input("Range: ")))
        for i in arr:
            print(i)
        print(f"Sum: {sum(arr)}")
    except Exception as ex:
        print(ex)
