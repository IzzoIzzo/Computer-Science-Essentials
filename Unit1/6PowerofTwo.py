print("Welcome to the simple calculator")
print("This calculator will multiply by the power of two.")
num1 = input("Enter your first number")
num2 = 2
answer = (int(num1) ** int(num2))
print(answer)
if answer > 100:
    print("You're loud")
elif answer < 100:
    print("You're quiet")
else:
    print("ERROR")


