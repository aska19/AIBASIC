def add(x,y):
    total = x + y
    return total
def sub(x,y):
    total = x - y
    return total
def multi(x,y):
    total = x * y
    return total
def divi(x,y):
    total = x / y
    return total

while True:
    
    print("1:addition")
    print("2:substraction")
    print("3:multiplication")
    print("4:division")

    x = int(input(" x = "))
    y = int(input(" y = "))
    choice = int(input("choice = "))

    total = 0
    if choice == 1:
        total = add(x,y)
    if choice == 2:
        total = sub(x,y)
    if choice == 3:
        total = multi(x,y)
    if choice == 4:
        total = divi(x,y)
    
    print(total)

    question = input("continue?")
    if question == "Y":
        continue
    else:
        break