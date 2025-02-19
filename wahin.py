symbol = input("Enter the symbol (+ - * / ): ")
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
if symbol == "+":
    result = num1 + num2
    print(result)
elif symbol == "-":
    result = num1 - num2
    print(result)
elif symbol == "*":
    result = num1 * num2
    print(result)
elif symbol == "/":
    result = num1 / num2
    print(result)
