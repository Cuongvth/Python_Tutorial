fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]

print(fruits.count("apple"))  # In ra số lượng phần tử trong đối tượng
# 2

print(fruits.count("tangerine"))  # In ra số lượng phần tử được chỉ định trong đối tượng
# 0

print(
    fruits.index("banana")
)  # In ra vị trí đứng của phần tử đầu tiên được chỉ định xuất hiện trong đối tượng
# 3

print(
    fruits.index("banana", 4)
)  # In ra vị trí đứng của phần tử đầu tiên được chỉ định xuất hiện trong đối tượng tính từ một vị trí được chỉ định
# 6

fruits.reverse()  # Đảo ngược các phần tử có trong đối tượng
print(fruits)
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

fruits.append("grape")  # Thêm một phần tử vào cuối đối tượng
print(fruits)
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

fruits.sort()  # Sắp xếp các phần tử trong đối tượng
print(fruits)
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

print(fruits.pop())  # In ra phần tử cuối cùng trong đối tượng
# pear
print(fruits)
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']
