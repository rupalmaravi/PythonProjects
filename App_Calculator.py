var_num1 = float(input("Enter first number:"))
op=input("Enter operator :")
var_num2 = float(input("Enter second number:"))

if op == "+":
    print(var_num1 + var_num2)
elif op == "*":
    print(var_num1 * var_num2)
elif op == "/":
    print(var_num1 / var_num2)
elif op == "-":
    print(var_num1 - var_num2)
else:
    print("Invalid operator !")
