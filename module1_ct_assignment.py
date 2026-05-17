num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

def addition(num1, num2):
    return num1 + num2

def substraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

print(f"{num1} plus {num2} is {addition(num1, num2)}")
print(f"{num1} minus {num2} is {substraction(num1, num2)}")
print(f"{num1} multiplied by {num2} is {multiplication(num1, num2)}")
print(f"{num1} divided by {num2} is {division(num1, num2)}")