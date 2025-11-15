num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")
result = None
match operator:
        case '+':
            result = num1 + num2
            print("answer is",result)
        case '-':
            result = num1 - num2
            print("answer is",result)
        case '*':
            result = num1 * num2
            print("answer is",result)
        case '/':
            result = num1 / num2
            print("answer =",result)