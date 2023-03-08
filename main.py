import csv
import datetime
import Modules
import Pizza_Types
import Sauces_Types


with open("Menu.txt", "r") as f:
    menu = f.read()

print(menu)

# Prompt the user to choose a pizza and a sauce


 # take the chosen pizza object
while True:
    pizza_choice = input("Please choose a pizza (1-4): ")
   
    if pizza_choice == "1":
        pizza = Pizza_Types.ClassicPizza()
        break
    elif pizza_choice == "2":
        pizza = Pizza_Types.MargheritaPizza()
        break
    elif pizza_choice == "3":
        pizza = Pizza_Types.TurkPizza()
        break
    elif pizza_choice == "4":
        pizza = Pizza_Types.PlainPizza()
        break
    else:
        print("Invalid pizza choice please try again.")


 # take the chosen sauce object
while True:
    sauce_choice = input("Please choose a sauce (11-16): ")
    if sauce_choice == "11":
        sauce = Sauces_Types.Olives(pizza)
        break
    elif sauce_choice == "12":
        sauce = Sauces_Types.Mushrooms(pizza)
        break
    elif sauce_choice == "13":
        sauce = Sauces_Types.GoatCheese(pizza)
        break
    elif sauce_choice == "14":
        sauce = Sauces_Types.Meat(pizza)
        break
    elif sauce_choice == "15":
        sauce = Sauces_Types.Onions(pizza)
        break
    elif sauce_choice == "16":
        sauce = Sauces_Types.Corn(pizza)
        break
    else:
        print("Invalid sauce choice please try again.")
    



# Calculate the total cost of the order
total_cost = float(sauce.cost) + float(pizza._cost)

# Prompt the user for their information
name = input("Please enter your name: ")


while True:
    credit_card_number = input("Please enter your credit card number: (Your credit number has to be 16 digits.)  ")
    if len(credit_card_number) != 16 or not credit_card_number.isdigit():
        print("Please enter valid credit card.")
    else:
        break
while True:
    credit_card_password = input("Please enter your credit card password: (Your credit card password has to be 4 digits.) ")
    if len(credit_card_password) != 4 or not credit_card_password.isdigit():
        print("Please enter valid credit card password")
    else:
        print("Your order is preparing...")
        break
id_number = name[:3] + str(credit_card_number)[-3:]   #id number is customer's first 3 letter and credit card's last 3 number

# Write the order information to the Orders_Database.csv file
with open("Orders_Database.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([name, id_number, credit_card_number, sauce.description, pizza._description, total_cost, datetime.datetime.now(), credit_card_password])