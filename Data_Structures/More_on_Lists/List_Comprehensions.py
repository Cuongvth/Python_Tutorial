squares = []

for x in range(10):
    squares.append(x**2)
# Tạo một danh sách dựa trên danh sách range(10) tương đương với [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Danh sách mới là một danh sách các bình phương của các phần tử trong danh sách cũ
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Tương đương với
squares = list(map(lambda x: x**2, range(10)))
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Hoặc
squares = [x**2 for x in range(10)]
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


combs = []

for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
# Tạo một danh sách mới gồm một phần tử x và một phần tử y
# Phần tử x được dựa trên danh sách  [1, 2, 3]
# Phần tử y được dựa trên danh sách  [3, 1, 4]
# Lấy những phần tử có x và y khác nhau vào danh sách mới
print(combs)
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# Tương đương với
combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combs)
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
