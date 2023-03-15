def int_to_bstr(num: int) -> str:
    '''

    :param num: 要转换的整数
    :return: 输出的二进制字符串
    '''
    bits = 64  # 假设使用 64 位二进制表示
    if num >= 0:
        # 正数的补码等于原码
        binary = bin(num)[2:].zfill(bits)
    else:
        # 负数的补码等于其对应正数的补码取反再加 1
        binary = bin((1 << bits) - abs(num))[2:]
    return binary

int_a = int(input("输入目标整数："))
bstr = int_to_bstr(int_a)
cnt = bstr.count('1')
print(f"{int_a}对应的二进制补码中含有{cnt}个1")
