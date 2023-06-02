raise NameError("HiThere")
# Traceback (most recent call last):
# NameError: HiThere

raise ValueError

try:
    raise NameError("HiThere")
except NameError:
    print("An exception flew by!")
    raise
# Traceback (most recent call last):
# NameError: HiThere
