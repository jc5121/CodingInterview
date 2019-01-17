# coding: utf-8
# 不使用+-*/做加法 异或，与
# 汇编


# 这种做法c++可以 python不行，这事为啥
def Add(num1, num2):
    while num2 != 0:
        add_sum = num1 ^ num2
        num2 = (num1 & num2) << 1  # 处理进位
        num1 = add_sum
    return num1


print Add(-1, 22)  #

# 不使用加减法交换


def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b


def swap2(a, b):
    a = a + b
    b = a - b
    a = a - b