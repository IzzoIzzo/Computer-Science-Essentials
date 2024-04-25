#1st National Bank of Browntown Online Banking Application


class Customer():
    #This is an OBJECT. It has properties of Withdraw, Deposit, BalanceCheck
    def __init__ (self, name, balance = 100.00):#Creates the user and gives him cash.
        self.name = name
        self.balance = balance
        print("Account made for", name, " Current Balance: $", balance)

    def withdraw(self,amount):#The withrdaw ability.
        self.balance = self.balance - amount
        return self.balance
    
    def deposit(self,amount):#Allows you to deposit.
        self.balance = self.balance - amount
        return self.balance
    def BalanceCheck(self):#Ability to check balance.
        return self.balance
    #Add the ability to deposit
       

    #Add the ability to check balance

print("Welcome to the 1st National Bank of Browntown App")
print("All new customers get $100 deposited into their account for signing up!")
print()

name = input("Let's Get Started! What is your name: ")
customer = Customer(name)
#Adds Loop
while True:
    print("What would you like to do: (1) Withdraw   (2) Deposit   (3) Check Balance   (4) Log Out")
    choice = input("->")

        #Withdraw
    if choice == "1": #Choice to withdraw.
            print("How much are you withdrawing")
            amount = float(input("->"))
            balance = customer.balance - amount 
            customer.withdraw(amount)
            print("You have withdrawn ", amount)
            print("You now have...", balance)
            #Add a line that tells them their balance...after you have implemented balance check above

            #Add the ability to deposit
    elif choice == "2":#Choice to deposit.
            print("How much would you like to deposit?")
            amount = float(input("+>"))
            balance = customer.balance + amount
            customer.deposit(amount)
            print("You have deposited", amount)
            print("You now have...", balance)

            #Add the ability to check balance
    elif choice == "3":#Choice to check ur balance.
            balance = customer.balance
            print("Your balance is $", balance)
    elif choice == "4":#Choice to logout.
            print("You have successfully logged out")
            break
    else:#Error code
            print("You have entered an illegal value, plese try again.")
