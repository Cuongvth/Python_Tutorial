from Config.Config import path

with open(path + "Errors_and_Exceptions\Predefined_Clean_up_Actions\myfile.txt") as f:
    for line in f:
        print(line, end="")

# Với with giúp đảm bảo file sẽ được đóng tự động khi hoàn thành việc đọc kể cả khi đọc thành công hay không thành công
