#File name
fileName = "test_text_file.txt"

#Content going to file
def writeToFile(content):
    try:
        with open(fileName, 'a') as file:
            content = content +"\n"
            file.write(content)
            print("content added!")
            file.close()
    except:
        print("Error!")

#Reading from text file
def readFromFile():
    try:
        with open(fileName, 'r') as file:
            content = file.read()
            print(content)
            file.close()
    except:
        print("An error has occured!")
    

while True:
    print("What would you like to do?")
    print("1: send data   2:read data   3:exit program")
    choice = input("->")
    if choice == "1":
        print("What data do you want to send?")
        content = input("->")
        writeToFile(content)
        print("Content added to file")

    elif choice == "2":
        print("Reading the text file")
        readFromFile()

    elif choice == "3":
        break
print("Good Bye")
