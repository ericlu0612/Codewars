# # codewars第四題
# import math
#
#
# def is_square(n):
#     if n >= 0 and math.sqrt(n) == math.floor(math.sqrt(n)):  # floor向下圓整
#         return True
#     else:
#         return False


# # 第二中解法
# import math
#
#
# def is_square(n):
#     return n > -1 and math.sqrt(n) % 1 == 0;  # 巧妙的除1取餘  整數求餘必爲0  非整數求餘不爲0
import math
def is_square(n):
    if n > -1 and math.sqrt(n) % 1 == 0:
        return True
    else:
        return False

x = is_square(0)
print(x)
