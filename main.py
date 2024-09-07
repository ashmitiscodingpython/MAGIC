import time
chosen = [
    ['Apple', 'Pineapple', 'Mango'],
    ['Mango', 'Apple', 'Blueberry'],
    ['Blueberry', 'Strawberry', 'Apple'],
    ['Mango', 'Strawberry', 'Pineapple']
]
UAnswers = []
Chosen = [False, False, False, False]
index = 0
apple, pineapple, mango, blueberry, strawberry = 0


def update():
    global index
    print('Is your fruit here?')
    print(*chosen[index])
    x = input('> ').upper()
    if x == 'YES':
        Chosen[index] = True
    else:
        pass
    index += 1


def check():
    global apple, blueberry, strawberry, mango, pineapple
    if Chosen[0]:
        apple += 1
        pineapple += 1
        mango += 1
    if Chosen[1]:
        mango += 1
        apple += 1
        blueberry += 1
    if Chosen[2]:
        blueberry += 1
        strawberry += 1
        apple += 1
    if Chosen[3]:
        mango += 1
        strawberry += 1
        apple += 1


def announce():
    fruit = None
    if apple == 3:
        fruit = "Apple"
    elif mango == 3:
        fruit = "Mango"
    elif blueberry == 2:
        fruit = "Blueberry"
    elif pineapple == 2:
        fruit = "Pineapple"
    elif strawberry == 2:
        fruit = "Strawberry"
    else:
        print('Sorry, there seems to be a mistake at your end.')
        return
    print("Your fruit is...")
    time.sleep(0.5)
    print(".....")
    time.sleep(0.5)
    print("Let me see....")
    time.sleep(1)
    print(f"Yes, your fruit is {fruit}!")
    time.sleep(0.5)
    print("Yes, thank you, thank you! *bows*")
    time.sleep(0.1)
    print("Byeeee...")
    time.sleep(0.1)
    print("For now....")

        
print('Hello! Welcome to the MAGIC project!\nChoose a fruit from any of these:\nApple Blueberry Mango Pineapple Strawberry')
time.sleep(3)
for i in range(4):
    update()
check()
announce()
