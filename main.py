import time
chosen = [
    ['Apple', 'Pineapple', 'Mango'],
    ['Mango', 'Apple', 'Blueberry'],
    ['Blueberry', 'Strawberry', 'Apple'],
    ['Mango', 'Strawberry', 'Pineapple']
]
code = ''
fruits_ = ["1101", "1110", "1001", "0110", "0011"]
fruits = ["Mango", "Apple", "Pineapple", "Blueberry", "Strawberry"]
fruit = ''
index = 0


def update():
    global index, code
    print('Is your fruit here?')
    print(f"{chosen[index][0]}, {chosen[index][1]}, {chosen[index][2]}")
    x = input('> ').upper()
    if x == 'YES':
        code += "1"
    else:
        code += "0"
    index += 1


def check():
    global fruit, fruits, fruits_
    try:
        fruit = fruits[fruits_.index(code)]
    except ValueError:
        print("There has been a mistake at your end. Please run the program again and enter correct inputs.")
        exit(-1)

def announce():
    global fruit
    time.sleep(2)
    print(".... (Where's that script when you actually need it????)")
    time.sleep(2)
    print("(Ah, here it is!)")
    time.sleep(1)
    print("Ahem! Your fruit is...")
    time.sleep(2)
    print(".....")
    time.sleep(1)
    print("Let me see....(Where are my glasses??!)")
    time.sleep(2)
    print(f"Yes, your fruit is {fruit}!")
    time.sleep(1)
    print("Yes, thank you, thank you! *bows*")
    time.sleep(1)
    print("Byeeee...")
    time.sleep(1)
    print("For now....")

        
print('Hello! Welcome to the MAGIC project!\nChoose a fruit from any of these:\nApple Blueberry Mango Pineapple Strawberry')
time.sleep(3)
for i in range(4):
    update()
check()
announce()
