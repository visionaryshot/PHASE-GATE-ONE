#Ask for customer and cashier names
#Initialize variable and Loop to enter multiple goods
#Then Calculate total for this goods
#Ask for more goods 
#Ask for discount
#Calculate for VAT
#print out the invoices

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
bill_total = overall_goods

print("===============================================")
print("\n SEMICOLON GYM INVOICE")
print("MAIN BRANCH")
print("LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA,LAGOS.")
print("Tel: 07086879592")
print(f"{current_time}")
print(f"CASHIER NAME: {cashier_name}")
print(f"USERS  NAME: {users_name}")
print("================================================")
print("   \tITEM   \tQTY   \tPRICE   \tTOTAL" )
print("------------------------------------------------")
print(f"   \t{name_of_goods}   \t{amounts_of_goods}   \t{price_of_goods}   \t{goods_total}")
print("------------------------------------------------")
print(f"SubTotal:      \t{total_amount}")
print(f"Discount:      \t{discount_amount}")
print(f"VAT @ 17.50%:  \t{vat}")
print("================================================")
print(f"Bill Total:     \t{overall_goods}")
print("=================================================")
print(f"THIS IS NOT A RECEIPT KINDLY PAY \t{overall_goods}")
print("=================================================")


user = int(input("HOW MUCH DID THE CUSTOMER GIVE TO YOU:\n"))
balance = user - overall_goods

print("SEMICOLON GYM INVOICE")
print("MAIN BRANCH")
print("LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA,LAGOS.")
print("Tel: 07086879592")
print(f"{current_time}")
print(f"CASHIER NAME: {cashier_name}")
print(f"USERS  NAME: {users_name}")
print("================================================")
print("   \tITEM   \tQTY   \tPRICE   \tTOTAL" )
print("------------------------------------------------")
print(f"   \t{name_of_goods}   \t{amounts_of_goods}   \t{price_of_goods}   \t{goods_total}")
print("------------------------------------------------")
print(f"SubTotal:      \t{total_amount}")
print(f"Discount:      \t{discount_amount}")
print(f"VAT @ 17.50%:  \t{vat}")
print("================================================")
print(f"Bill Total:     \t{overall_goods}")
print(f"Amount Paid:    \t{user}")
print(f"Balance:        \t{balance}")
print("================================================")
print("            THANK FOR YOUR PATRONAGE            ")
print("================================================")