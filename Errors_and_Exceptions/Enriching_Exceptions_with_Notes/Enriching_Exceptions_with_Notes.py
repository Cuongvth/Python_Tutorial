def f():
    raise OSError("operation failed")


excs = []
for i in range(3):
    try:
        f()  # Ném ra exception
    except Exception as e:
        e.add_note(f"Happened in Iteration {i+1}")  # Thêm thông báo vào exception
        excs.append(e)  # Thêm exception vào mảng excs
raise ExceptionGroup(
    "We have some problems", excs
)  # Ném ra ExceptionGroup gồm các exception trong mảng excs

# | ExceptionGroup: We have some problems (3 sub-exceptions)
#   +-+---------------- 1 ----------------
#     | Traceback (most recent call last):
#     | OSError: operation failed
#     | Happened in Iteration 1
#     +---------------- 2 ----------------
#     | Traceback (most recent call last):
#     | OSError: operation failed
#     | Happened in Iteration 2
#     +---------------- 3 ----------------
#     | Traceback (most recent call last):
#     | OSError: operation failed
#     | Happened in Iteration 3
#     +------------------------------------
