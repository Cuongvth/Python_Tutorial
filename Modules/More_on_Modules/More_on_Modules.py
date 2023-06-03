from Modules.fibo import fib, fib2  # Thêm hai hàm là fib và fib2 từ Module fibo

fib(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

from Modules.fibo import *  # Thêm tất cả các thành phần từ Module fibo

fib(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

import Modules.fibo as fib  # Thêm Module fibo dưới tên là fib

fib.fib(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
