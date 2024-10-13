import math
import sys

def check_weird(value):
    if value % 2 != 0:
        return "Weird"
    else:
        if 2 <= value <= 5: 
            return "Not Weird"
        elif 6 <= value <= 20:
            return "Weird"
        else: 
            return "Not Weird"
        
while True:
    try:
#       input_data = sys.stdin.read().strip()
        give = int(input())
        if 0 < give <= 100:
            print(check_weird(give))
        else:
            print("Invalid input") 
    except ValueError:
        break

'''import sys: Đây là bước quan trọng giúp chương trình truy cập module sys để sử dụng hàm sys.stdin.read().
sys.stdin.read(): Đọc toàn bộ dữ liệu đầu vào cùng một lúc, thay vì yêu cầu người dùng nhập từng dòng với input(). Điều này đặc biệt hữu ích khi chạy trên các nền tảng trực tuyến.
strip(): Xóa các khoảng trắng dư thừa hoặc dòng trống từ đầu vào để tránh lỗi khi chuyển đổi thành số nguyên.'''