import bisect


def Demo():
    scores = []
    value = "-1"
    while value != "":
        value = input("Hãy nhập các giá trị trong phần tử không nhập gì để dừng lại: ")
        if value == "":
            break
        try:
            bisect.insort(scores, (int(value), "Value"))
        except Exception as ex:
            print(ex)
    print(scores)
