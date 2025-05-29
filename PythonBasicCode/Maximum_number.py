def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


num1 = input("Enter first number:")
num2 = input("Enter second number:")
num3 = input("Enter third number:")

print("Max number is " + str(max_num(int(num1), int(num2), int(num3))))
