def Demo():
    arr = set(input("Nhập một vài kí tự: "))
    search = input("nhập một kí tự để tìm kiếm: ")[0]
    print(arr)
    for i, v in enumerate(arr):
        if v == search:
            print(f"Index: {i}")
            break
    value = input("nhập một kí tự để loại bỏ: ")[0]
    print(arr)
    arr_last = []
    for i in arr:
        if i == value:
            continue
        arr_last.append(i)
    print(arr_last)
