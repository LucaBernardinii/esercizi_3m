age = int(input("Insert your age: "))

if age >=0 and age <=12:
    print("You're a child")
elif age >=13 and age <=19:
    print("You're a teenager")
elif age >=20 and age <=64:
    print("You're an adult")
elif age >= 65:
    print("You're a senior")
else:
    print("Error")
