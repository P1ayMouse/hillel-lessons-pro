import os
from time import sleep

if __name__ == '__main__':
    A = 5
    B = 10

    for i in range(0, 5):
        print(i)
        sleep(0.5)

    x = os.fork()

    print('X =', x)

    if x == 0:
        for i in range(A, A+5):
            print('Child:', i)
            sleep(0.5)
    else:
        for i in range(B, B+5):
            print('Parent:', i)
            sleep(0.5)