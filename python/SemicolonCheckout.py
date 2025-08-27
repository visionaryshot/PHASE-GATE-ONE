#Ask for customer and cashier names
#Initialize variable and Loop to enter multiple goods
#Then Calculate total for this goods
#Ask for more goods 
#Ask for discount
#Calculate for VAT
#print out the invoice

import datetime
current_time = datetime.datetime.now()

users_name = input("Enter customer's name: ")
cashier_name = input("Enter cashier's name: ")
total_amount = 0
while (True):
    name_of_goods = input("Enter name of goods: ")
    price_of_goods = float(input(f"Enter price of goods {name_of_goods}:"))
    amounts_of_goods = int(input(f"Enter amounts of goods of {name_of_goods}: "))

   
    goods_total = price_of_goods * amounts_of_goods
    total_amount += goods_total 
   
    ask_for_more = input("do you want to add more? (yes/no): ").lower()
    if ask_for_more != "yes":
        break


discount = float(input("Enter discount: "))
discount_amount = (discount / 100) * total_amount
vat = 0.075 * total_amount
overall_goods = total_amount + vat - discount_amount
print(f"Your Discount: {discount}")

print("\n SEMICOLON GYM INVOICE")
print("MAIN BRANCH")
print("LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA,LAGOS.")
print("Tel: 07086879592")
print(f"CASHIER NAME: {cashier_name}")
print(f"USERS NAME: {users_name}")
print("========================================================")
print("current_time")