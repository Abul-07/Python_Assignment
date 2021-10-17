def add(num1 , num2):
    return num1 + num2

def sub(num1 , num2):
    return num1 - num2

def multiply(num1 , num2):
    return num1 *  num2

def divide(num1 , num2):
    return num1 / num2
        
print("Operation :")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    select = input("Enter any of the above operation: ")

    if select in ('1', '2', '3', '4'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if select == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif select == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif select == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif select == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
    
    else:
        print("Invalid Input")
    break