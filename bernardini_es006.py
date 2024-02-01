num1 = float(input("Insert the first number: "))
num2 = float(input("Insert the second number: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even")
elif num1 % 2 != 0 and num2 % 2 == 1:
    print("Both numbers are odd")
else:
    print("A number is even and the other is odd")