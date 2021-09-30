numbers = map(int, input().split(' '))
ascend_flag: bool = False
descend_flag: bool = False
for i, v in enumerate(numbers):
    if v - 1 == i:
        if not ascend_flag:
            ascend_flag = True
            continue
        elif descend_flag:
            print('mixed')
            break
    elif v == 8 - i:
        if not descend_flag:
            descend_flag = True
            continue
        elif ascend_flag:
            print('mixed')
            break
    else:
        print('mixed')
        break
else:
    # Finish loop without errors
    print('ascending' if ascend_flag else 'descending')



