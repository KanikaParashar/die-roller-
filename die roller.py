from random import randint
while True:
    k = randint(1,7)
    p = input('press "Enter" to continue or "y" to exit')
    if p == "y":
        break
    else:
        if k == 1:
            print('-------------')
            print('|           |')
            print('|     0     |')
            print('|           |')
            print('-------------')
        elif k ==2:
            print('-------------')
            print('|           |')
            print('|  0    0   |')
            print('|           |')
            print('-------------')
        elif k == 3:
            print('-------------')
            print('|        0  |')
            print('|    0      |')
            print('| 0         |')
            print('-------------')
        elif k == 4:
            print('-------------')
            print('|  0     0  |')
            print('|           |')
            print('|  0     0  |')
            print('-------------')
        elif k == 5:
            print('-------------')
            print('| 0       0 |')
            print('|     0     |')
            print('| 0       0 |')
            print('-------------')
        elif k == 6:
           print('-------------')
           print('| 0   0   0 |')
           print('|           |')
           print('| 0   0   0 |')
           print('-------------')
