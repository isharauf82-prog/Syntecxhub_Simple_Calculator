# Simple Calculator - Syntecxhub Project 1
# Made by [ISHA RAUF]

def addition(a,b):
    result = a + b
    return result

def subtraction(a,b):
    return a - b

def multiply(a,b):
    return a * b

def division(a,b):
    if b == 0:
        print("you cant divide with 0")
        return None
    else:
        return a / b

while True:
    print("\n--- Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("choose your option: ")

    if choice == "5":
        print("Good bye!")
        break

    x = float(input("First number: "))
    y = float(input("secomd number: "))

    if choice == "1":
        print("answer is:", addition(x,y))
    elif choice == "2":
        print("answer is:", subtraction(x,y))
    elif choice == "3":
        print("answer is:", multiply(x,y))
    elif choice == "4":
        ans = division(x,y)
        if ans is not None:
            print("answer is:", ans)
    else:
        print("wrong option , try again ")