import pprint


def Demo():
    length = int(input("Nhập số lượng phần tử: "))
    arr = []
    for i in range(length):
        arrChild = []
        value = "fake"
        while value != "":
            value = input(
                "Hãy nhập các giá trị trong phần tử không nhập gì để qua phần tử tiếp theo: "
            )
            if value != "":
                arrChild.append(value)
        arr.append(arrChild)
    pprint.pprint(arr, width=int(input("Nhập giới hạn kí tự mỗi dòng: ")))
