def f():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup("group2", [OSError(3), RecursionError(4)]),
        ],
    )


f()  # Thực thi hàm f ném ra hàng loạt exception mà không xử lí
#   | ExceptionGroup: group1 (3 sub-exceptions)
#   +-+---------------- 1 ----------------
#     | OSError: 1
#     +---------------- 2 ----------------
#     | SystemError: 2
#     +---------------- 3 ----------------
#     | ExceptionGroup: group2 (2 sub-exceptions)
#     +-+---------------- 1 ----------------
#       | OSError: 3
#       +---------------- 2 ----------------
#       | RecursionError: 4
#       +------------------------------------

try:
    f()  # Thực thi hàm f ném ra hàng loạt exception
except* OSError as e:  # Xử lí exception OSError
    print("There were OSErrors")
except* SystemError as e:  # Xử lí exception SystemError
    print("There were SystemErrors")
#   | ExceptionGroup: group1 (1 sub-exception)
#   +-+---------------- 1 ----------------
#     | ExceptionGroup: group2 (1 sub-exception)
#     +-+---------------- 1 ----------------
#       | RecursionError: 4
#       +------------------------------------
