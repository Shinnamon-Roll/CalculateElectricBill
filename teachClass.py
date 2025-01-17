def plus(a, b):
    a = 50
    b = 100

    z = a + b
    x = a + a + b

    return z, x

def minus(a, b):
    print(a - b)

def heemah():
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))

    choice = int(input("What do you want to do : "))

    if choice == 1:
        z, x = (plus(num1, num2))
        print(z, x)
    
    elif choice == 2:
        minus(num1, num2)
    
    print(z * x)

heemah()