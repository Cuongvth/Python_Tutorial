import fibo

fibo.fib(1000)  # Thực thi hàm fib của Module
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

print(fibo.fib2(100))  # Thực thi hàm fib2 của Module
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(fibo.__name__)  # Lấy ra tên của Module
# 'fibo'

fib = fibo.fib  # Gán hàm fib của Module fibo vào đối tượng fib
fib(500)  # Thực thi hàm fib của Module fibo thông qua đối tượng fib
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
