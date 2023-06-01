knights = {"gallahad": "the pure", "robin": "the brave"}

for k, v in knights.items():
    print(k, v)
# Lặp qua tất cả các phần tử trong từ điển knights và lấy ra khóa cùng giá trị của nó
# Output:
# gallahad the pure
# robin the brave

for i, v in enumerate(["tic", "tac", "toe"]):
    print(i, v)
# Lặp qua tất cả các phần tử trong đối tượng enumerate(['tic', 'tac', 'toe']) và lấy ra số thứ tự cùng giá trị của nó
# Output:
# 0 tic
# 1 tac
# 2 toe

questions = ["name", "quest", "favorite color"]  # Khởi tại mảng questions
answers = ["lancelot", "the holy grail", "blue"]  # Khỏi tạo mảng answers
for q, a in zip(questions, answers):
    print("What is your {0}?  It is {1}.".format(q, a))
# Lặp qua tất cả các phần tử trong mảng questions và answers lấy ra các phần tử trong hai mảng
# Output:
# What is your name?  It is lancelot.
# What is your quest?  It is the holy grail.
# What is your favorite color?  It is blue.
