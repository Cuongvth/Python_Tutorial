from heapq import heapify, heappop, heappush


def Demo():
    scores = []
    value = "-1"
    while value != "":
        value = input("Hãy nhập các giá trị trong phần tử không nhập gì để dừng lại: ")
        if value == "":
            break
        try:
            heappush(scores, int(value))
        except Exception as ex:
            print(ex)
    print(scores[0:10])
