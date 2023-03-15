a_list = [1, 1, 3, 3, 5, 5, 6, 7]
cnt = 0
for i, j in enumerate(a_list):
    if j not in (a_list[:j] + a_list[j + 1:]):
        print(j)
        cnt += 1
        if cnt == 2:
            break
