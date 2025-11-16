from datetime import datetime
now = datetime.now()
items_ordered= []
menu_items = {}
total=0
with open("impmenu.txt", "r") as file:
    for i, line in enumerate(file, start=1): # learn this (NKS)
        if "-" in line:
            name, price = line.strip().split(" - ")
            menu_items[str(i)] = (name, int(price))
print(''' 
                                           ┌──────────────────────────────────┐

========================================== |    McDonald's Delivery System    | ===========================================

                                           └──────────────────────────────────┘
                                   ╔════════════════════[[OPTIONS]]══════════════════╗
                                   ║1. To view Menu enter \"Menu\" or \"m\"              ║
                                   ║2. To add to cart enter the item's Serial Number ║
                                   ║3. To view cart enter \"cart\"                     ║
                                   ║4. Invoice I or i                                ║
                                   ║5. To exit press e                               ║
                                   ╚═════════════════════════════════════════════════╝    
''')
while True: 
    a=input("Waiting for input --> ").strip()
    print("======================")
    if a in ("Menu", "m"):
        with open("Menu.txt","r") as menu:
            print(menu.read())
    elif a in ("1","2","5","6","7","8"):
        item, price= menu_items[a]
        print("Name:", item)
        print("Price:", price)
        print("Availability: Available")
        print('────────────────────────────────────')
        print("Would you like to add it to cart")
        print('────────────────────────────────────')
        b=input("==> ")
        if b in ("yes", "y"):
            while True:
                try:
                    qty = int(input("Enter quantity --> "))
                    total = total + (price * qty)
                    items_ordered.append((item, qty, price*qty))
                    print("┌────────────Item───────────────┐")
                    print(" ","📦",item,"added !")
                    print("    ","₹",price, "x", qty, "=", price*qty)
                    print("└───────────────────────────────┘")
                    break
                except ValueError:
                     print("That ain't a number !?!?!?")
        elif b in ("no","n"):
            print("sad --(*)_(*)--")
        else:
            print("Skipping...")
    elif a in ("3","4"):
        item, price= menu_items[a]
        print("Name:", item,"[S/M]")
        print("Price:", price, "[S]","/",price+25,"[M]")
        print("Availability: Available")
        print('────────────────────────────────────')
        print("Would you like to add it to cart")
        print('────────────────────────────────────')
        b=input("==> ")
        if b in ("yes", "y"):
            print("Small or Medium")
            print('────────────────────────────────────')
            c=input("S/M--> ")
            if c in ("Small", "S","s"):
                while True:
                    try:
                        qty = int(input("Enter quantity --> "))
                        total = total + (price * qty)
                        items_ordered.append((item+"[S]", qty, price*qty))
                        print("┌────────────Item───────────────┐")
                        print(" ","📦",item," [S] ","added !")
                        print("    ","₹",price, " x ", qty, " = ", price*qty,sep='')
                        print("└───────────────────────────────┘")
                        break
                    except ValueError:
                        print("That ain't a number !?!?!?")
            elif c in ("Medium","M","m"):
                while True:
                    try:
                        qty = int(input("Enter quantity --> "))
                        total = total + (price * qty)
                        items_ordered.append((item+"[M]", qty, (price+25)*qty))
                        print("┌────────────Item───────────────┐")
                        print(" ","📦",item," [M] ","added !")
                        print("    ","₹",price, " x ", qty, " = ", (price+25)*qty,sep='')
                        print("└───────────────────────────────┘")
                        break
                    except ValueError:
                        print("That ain't a number !?!?!?")  
    elif a in ("Invoice", "I","i"):
        if total==0:
            print("Your cart is empty, please add something first")
            print("======================")
        else:
            print("Enter details for Invoice")
            name=input("Name ")
            while True:
                try:
                    phone=int(input("Phone number "))
                    break
                except ValueError:
                    print("Enter the number damnit")
            address=input("Address ")
            with open("filename.txt", "w+") as file:
                file.write("═══════ McDonald's Delivery Invoice ═══════\n")
                file.write(f"Date: {now.strftime('%d-%m-%Y %H:%M:%S')}\n")
                file.write(f"Customer Name: {name}\n")
                file.write(f"Phone: {phone}\n")
                file.write(f"Address: {address}\n")
                file.write("───────────────────────────────────────────\n")
                file.write("Items Ordered:\n")

                for item_name, qty, amount in items_ordered:
                    file.write(f"{item_name} x{qty} = {amount}\n")

                file.write("───────────────────────────────────────────\n")
                file.write(f"Total Bill: ₹{total}\n")
                file.write("Thank you for ordering from McDonald's!\n")
                file.write("Your food will be delivered shortly 🍟🍔\n")
                file.write("═══════════════════════════════════════════\n")
                file.seek(0)
                print(file.read())
    elif a=="cart":
        if total==0:
            print("Nothing in cart")
            print("======================")
        else:
            print('''  ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
░▒▓█▓▒░      ░▒▓████████▓▒░▒▓███████▓▒░  ░▒▓█▓▒░     
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░
 ''')
            count=1
            for item_name, qty, amount in items_ordered:
                print(count,". ",item_name, " qty ", qty," amount ", amount, sep='')

                count += 1
    elif a=="e":
        print('''         _   _                                 _                _             
        | | | |                               (_)              | |            
        | |_| | __ ___   _____    __ _   _ __  _  ___ ___    __| | __ _ _   _ 
        |  _  |/ _` \ \ / / _ \  / _` | | '_ \| |/ __/ _ \  / _` |/ _` | | | |
        | | | | (_| |\ V /  __/ | (_| | | | | | | (_|  __/ | (_| | (_| | |_| |
        \_| |_/\__,_| \_/ \___|  \__,_| |_| |_|_|\___\___|  \__,_|\__,_|\__, |
                                                                        __/ |
                                                                        |___/ ''')
        break
    else:
        print("Please choose something from the given options")
        print("======================")
'''
   _____          _____ _______ 
  / ____|   /\   |  __ \__   __|
 | |       /  \  | |__) | | |   
 | |      / /\ \ |  _  /  | |   
 | |____ / ____ \| | \ \  | |   
  \_____/_/    \_\_|  \_\ |_|   
                                
                                
'''