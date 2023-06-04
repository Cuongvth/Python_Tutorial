from collections import deque
import threading
import time


class dequeDemo:
    lst = deque([])

    @classmethod
    def add_to_array(cls):
        while True:
            value = input(
                "Hãy nhập các giá trị trong phần tử không nhập gì để dừng lại: "
            )
            if value == "":
                break
            cls.lst.append(value)

    @classmethod
    def print_array_element(cls):
        while True:
            if len(cls.lst) > 0:
                print()
                print("--Handling", cls.lst.popleft())
            time.sleep(5)

    @classmethod
    def Demo(cls):
        print_thread = threading.Thread(target=cls.print_array_element)
        add_thread = threading.Thread(target=cls.add_to_array)
        print_thread.start()
        add_thread.start()
        print_thread.join()
        add_thread.join()
