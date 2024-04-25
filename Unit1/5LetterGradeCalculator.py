print("Welcome to the Did I Fail? Calculator.")
print("This Calculator will tell whether or not you failed.")
num1 = input("How many points was the grade out of?")
num2 = input("What did you score?")
grade = int(num2)/int(num1) * 100
print(grade)
if grade > 89.5:
    print("A")
    print("You passed!")
elif grade > 79.5:
    print("B")
    print("You passed!")
elif grade > 69.5:
    print("C")
    print("You passed!")
elif grade > 59.5:
    print("D")
    print("You passed.")
elif grade < 59.5:
    print("F")
    print("You failed!!")
