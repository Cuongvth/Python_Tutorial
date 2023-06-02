try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")  # Khi lỗi ném ra một exception khác


# Traceback (most recent call last):
# FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
# RuntimeError: unable to handle error

try:
    raise ConnectionError  # Ném ra một exception để xử lí
except ConnectionError as exc:
    raise RuntimeError(
        "Failed to open database"
    ) from exc  # Ném ra một exception khác dựa trên exception trên
# Traceback (most recent call last):
# ConnectionError

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
# RuntimeError: Failed to open database

try:
    open("database.sqlite")
except OSError:
    raise RuntimeError from None  # Khi lỗi ném ra một exception không có chuỗi
# Traceback (most recent call last):
# RuntimeError
