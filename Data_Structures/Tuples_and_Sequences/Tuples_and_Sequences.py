t = 12345, 54321, "hello!"

print(t[0])  # In ra phần tử thứ 0 trong đối tượng
# 12345

print(t)
# (12345, 54321, 'hello!')

u = t, (1, 2, 3, 4, 5)  # Khai báo đối tượng u gồm đối tượng t và mảng (1, 2, 3, 4, 5)
print(u)
# ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

v = ([1, 2, 3], [3, 2, 1])  # Khia báo đối tượng v gồm mảng  [1, 2, 3] và [3, 2, 1]
print(v)
# ([1, 2, 3], [3, 2, 1])

empty = ()  # Khai báo đối tượng empty rỗng

singleton = (
    "hello",
)  # Khia báo dối tượng  singleton gồm chuỗi "hello" và một dữ liệu rỗng

print(len(empty))  # In ra số lượng phần tử trong đối tượng empty
# 0

print(len(singleton))  # In ra số lượng phần tử có trong đối tượng singleton
# 1

print(singleton)
# ("hello",)
