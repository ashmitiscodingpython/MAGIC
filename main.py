import time
chosen = [
    ['APPLE', 'PINEAPPLE', 'MANGO'],
    ['MANGO', 'APPLE', 'BLUEBERRY'],
    ['BLUEBERRY', 'STRAWBERRY', 'APPLE'],
    ['MANGO', 'STRAWBERRY', 'PINEAPPLE']
]
UAnswers = []
Chosen = [False, False, False, False]
index = 0
apple1, apple2, apple3 = False, False, False
blueberry1, blueberry2 = False, False
mango1, mango2, mango3 = False, False, False
pineapple1, pineapple2 = False, False
strawberry1, strawberry2 = False, False


def update():
    global index
    print('IS YOUR FRUIT HERE?')
    print(*chosen[index])
    x = input('> ').upper()
    if x == 'YES':
        Chosen[index] = True
    else:
        pass
    index += 1


def update2():
    global apple1, apple2, apple3, mango1, mango2, mango3, pineapple1, pineapple2, blueberry1, blueberry2, strawberry1, strawberry2
    if Chosen[0]:
        apple1, pineapple1, mango1 = True, True, True
    if Chosen[1]:
        mango2, apple2, blueberry1 = True, True, True
    if Chosen[2]:
        blueberry2, strawberry1, apple3 = True, True, True
    if Chosen[3]:
        mango3, strawberry2, pineapple2 = True, True, True


def check():
    if apple1 and apple2 and apple3:
        print('YOUR FRUIT IS...')
        time.sleep(1)
        print('APPLE!')
    elif mango1 and mango2 and mango3:
        print('YOUR FRUIT IS...')
        time.sleep(1)
        print('MANGO!')
    elif blueberry1 and blueberry2:
        print('YOUR FRUIT IS...')
        time.sleep(1)
        print('BLUEBERRY!')
    elif pineapple1 and pineapple2:
        print('YOUR FRUIT IS...')
        time.sleep(1)
        print('PINEAPPLE!')
    elif strawberry1 and strawberry2:
        print('YOUR FRUIT IS...')
        time.sleep(1)
        print('STRAWBERRY!')
    else:
        print('SORRY THERE SEEMS TO BE A MISTAKE ON YOUR END.')


print('HELLO. WELCOME TO MAGIC!\nCHOOSE A FRUIT FROM HERE\nAPPLE BLUEBERRY MANGO PINEAPPLE STRAWBERRY')
time.sleep(3)
for i in range(4):
    update()
update2()
check()
