from collections import deque

queue = deque(["Eric", "John", "Michael"])

queue.append("Terry")  # Thêm vào hàng chờ
queue.append("Graham")  # Thêm vào hàng chờ
print(
    queue.popleft()
)  # Lấy ra phần tử đến lượt là phần tử thêm vào sớm nhất trong hàng chờ
# "Eric"
print(
    queue.popleft()
)  # Lấy ra phần tử đến lượt là phần tử thêm vào sớm nhất trong hàng chờ
# "John"
print(queue)  # Kiểm tra hàng chờ
# deque(["Michael", "Terry", "Graham"])
