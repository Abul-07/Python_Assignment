print("Operation :")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

select = input("Enter any of the above operation (1,2,3,4): ")

if select in ('1', '2', '3', '4'):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

     if select == '1':
        print(num1, "+", num2, "=", num1 + num2 )

      elif select == '2':
         print(num1, "-", num2, "=", num1 - num2 )

      elif select == '3':
         print(num1, "*", num2, "=", num1 * num2 )

      elif select == '4':
         print(num1, "/", num2, "=", num1 / num2 )
    
 else:
    print("Invalid Input")
 break
