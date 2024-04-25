#BROWNTOWN BURGER JOINT POINT OF SALE SOFTWARE
#VERSION 1.21 LAST REVISION DATE 3/11/2024


#VARIABLES
orderComplete = False
totalCost = 0
tax = 0.06
orderSummary = ""

#WELCOME THE USER TO THE POINT OF SALE(POS)
print("Welcome to the Browntown Burger Joint, voted 2nd best Burger in Browntown")
print("We sell deloicious brugers, sides, and soda!")

#ASK THEM FOR THEIR NAME AND STORE IT IN name
name = input("Can I have your name please?  ")
print()
print("Thanks " + name)
print()
print()


#POINT OF SALE LOOP
while orderComplete == False:
    #STAY IN THIS LOOP UNTIL THEY SELECT "COMPLETE ORDER"
    print()
    print ("What would you like to order: Burgers, Sides, Drinks, Complete Order.")
    menu = input("-> ")
    
    
    if menu == "Burgers":
        #IF THEY WANT TO ADD A BURGER:
        print("We offer the following burgers:")
        print("1: Hamburger $5.50")
        print("2: Cheesebuger $6.00")
        print("3: Western burger (Cheese, onion, western sauce) $6.75")
        print("4: Chicken Burger $4.50")
        burgerChoice = input("What would you like (input a number 1-4): ")
        #BURGER 1: HAMBURGER
        if burgerChoice == "1":
            totalCost = totalCost + 5.50
            print("You added Hamburger to your order")
            print("Your total cost so far: $", totalCost)
            orderSummary = orderSummary + "Hamburger "

        #BURGER 2: CHEESEBURGER
        elif burgerChoice == "2":
            totalCost = totalCost + 6.00
            print("You added Cheeseburger to your order")
            print("Your total cost so far: $", totalCost)
            orderSummary = orderSummary + "Cheeseburger "

        #BURGER 3: WESTERN BURGER
        elif burgerChoice == "3":
            totalCost = totalCost+ 6.75
            print("You added Western Burger to your order")
            print("Your total cost so far: $", totalCost)
            orderSummary = orderSummary + "Western Burger "
        
        #BURGER 4: Chicken Burger
        elif burgerChoice == "4":
            totalCost = totalCost+ 4.50
            print("You added Chciken Buger to your order")
            print("Your total cost so far: $", totalCost)
            orderSummary = orderSummary + "Chicken Burger "


            
        #IF THEY GET HERE, THEY DID NOT MAKE A VALID SELECTION
        else:
            print("please make a valid choice")
        
    elif menu == "Sides":
        print("sides")
        print("We offer the following sides:")
        print("1: Fries $3.50")
        print("2: Mozzarella Sticks $3.00")
        print("3: Tater Tots $2.75")
        sideChoice = input("What would you like (input a number 1-3): ")

        #Side 1: Fries
        if sideChoice == "1":
            totalCost = totalCost + 3.50
            print("You added Fries to your order")
            print("Your total cost so far: $", totalCost)
            orderSummary = orderSummary + "Fries "
        #Side 2: Mozzarella Sticks
        if sideChoice == "2":
            totalCost = totalCost + 3.00
            print("You added Mozzarella Sticks to your order")
            print("Your total cost so far: $", totalCost)
            orderSummary = orderSummary + "Mozzarella Sticks "
        #Side 3: Tater Tots
        if sideChoice == "3":
            totalCost = totalCost + 2.75
            print("You added Tater Tots to your order")
            print("Your total cost so far: $", totalCost)
            orderSummary = orderSummary + "Tater Tots "
        
    elif menu == "Drinks":
        print("drinks")
        print("We offer the following drinks:")
        print("1: Coke $2.50")
        print("2: Sprite $2.50")
        print("3: Dr Pepper $2.50")
        drinkChoice = input("What would you like (input a number 1-3): ")

        #Drink 1: Coke
        if sideChoice == "1":
            totalCost = totalCost + 2.50
            print("You added Coke to your order")
            print("Your total cost so far: $", totalCost)
            orderSummary = orderSummary + "Coke "
        #Drink 2: Sprite
        if sideChoice == "2":
            totalCost = totalCost + 2.50
            print("You added Sprite to your order")
            print("Your total cost so far: $", totalCost)
            orderSummary = orderSummary + "Sprite "
        #Drinl 3: Dr Pepper
        if sideChoice == "3":
            totalCost = totalCost + 2.50
            print("You added Dr Pepper to your order")
            print("Your total cost so far: $", totalCost)
            orderSummary = orderSummary + "Dr Pepper "

    
    
    elif menu == "Complete Order":
        #IF THEY SELECT COMPLETE ORDER, SET THE ORDERCOMPLETE TO TRUE
        orderComplete = True
        print("Your order is complete!")

        #GIVE THEM THEIR TOTALS
        #Finish this section to give you a grand total as well as print your complete order
        print("order finished")
        print("You have ordered", orderSummary)
        print("Subtotal: $", totalCost)
        totalTax = float(totalCost) * tax
        print("Total Tax: $", totalTax)
        print("Grand Total: $", totalCost+ totalTax)
        
 
        
    else:
        print("Sorry, not a valid choice, please start over...")

#THE USER ONLY GETS HERE IF THEY FINISH THEIR ORDER
print("Thank you for eating with us!")
