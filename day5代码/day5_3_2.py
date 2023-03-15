space_num_list = [4, 3, 2, 1, 0, 1, 2, 3, 4]
line_num = len(space_num_list)
for space_num in space_num_list:
    print(" " * space_num, end="")  # 前空格
    for i in range(0 + space_num, line_num - space_num):
        if i == space_num or i == line_num - space_num - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print(" " * space_num, end="\n")  # 后空格
