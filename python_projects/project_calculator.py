num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

operator = input("Enter operator: ")

match operator:
    case '+':
        print("Addition is: ",num1+num2)
    case '-':
        print("Substraction is: ",num1-num2)
    case '*':
        print("Multiplication is: ",num1*num2)
    case '/':
        print("Division is: ",num1/num2)
    case '%':
        print("Modulo is: ",num1%num2)
    case _:
        print("Invalid operator!")
    
