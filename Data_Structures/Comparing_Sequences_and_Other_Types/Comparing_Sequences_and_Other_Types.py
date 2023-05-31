print((1, 2, 3) < (1, 2, 4))  # Khi so sánh tới phần tử thứ 3 thì 3 < 4
# True

print([1, 2, 3] < [1, 2, 4])  # Khi so sánh tới phần tử thứ 3 thì 3 < 4
# True

print(
    "ABC" < "C" < "Pascal" < "Python"
)  # So sánh lần lượt các kí tự có cùng vị trí A < C < P và a < y
# True

print((1, 2, 3, 4) < (1, 2, 4))  # Khi so sánh tới phần tử thứ 3 thì 3 < 4
# True

print(
    (1, 2) < (1, 2, -1)
)  # Khi so sánh tới phần tử thứ 3 thì đối tượng một không có phần tử thứ 3
# True

print(
    (1, 2, 3) == (1.0, 2.0, 3.0)
)  # Tất cả các phần tử bằng nhau đến hết cả hai đối tượng
# True

print(
    (1, 2, ("aa", "ab")) < (1, 2, ("abc", "a"), 4)
)  # Khi so sánh tới ("aa", "ab") và ("abc", "a") thì so sánh "aa" và "abc" được "aa" < "abc"
# True
