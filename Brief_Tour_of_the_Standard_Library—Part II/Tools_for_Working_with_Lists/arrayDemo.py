from array import array


def Demo():
    type = "-1"
    while type not in ["i", "I", "b", "B", "f", "d", "l", "L"]:
        type = input(
            'Nhập kiểu dữ liệu là một kí tự trong mảng sau ["i", "I", "b", "B", "f", "d", "l", "L"]: '
        )
    a = array(type, [])
    value = "-1"
    while value != "":
        value = input(
            "Hãy nhập các giá trị trong phần tử không nhập gì để dừng lại: "
        )
        if value == "":
            break
        try:
            a.append(int(value))
        except Exception as ex:
            print(ex)
    print("Sum: ", sum(a))
