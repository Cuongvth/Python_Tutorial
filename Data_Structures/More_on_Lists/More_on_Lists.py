fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]

print(fruits.count("apple"))  # Lấy ra số lượng phần tử trong mảng
# 2

print(fruits.count("tangerine"))  # Lấy ra số lượng phần tử được chỉ định trong mảng
# 0

print(
    fruits.index("banana")
)  # Lấy ra vị trí đứng của phần tử đầu tiên được chỉ định xuất hiện trong mảng
# 3

print(
    fruits.index("banana", 4)
)  # Lấy ra vị trí đứng của phần tử đầu tiên được chỉ định xuất hiện trong mảng tính từ một vị trí được chỉ định
# 6

fruits.reverse()  # Đảo ngược các phần tử có trong mảng
print(fruits)
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

fruits.append("grape")  # Thêm một phần tử vào cuối mảng
print(fruits)
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

fruits.sort()  # Sắp xếp các phần tử trong mảng
print(fruits)
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

print(fruits.pop())  # Lấy ra phần tử cuối cùng trong mảng
# pear
print(fruits)
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']
