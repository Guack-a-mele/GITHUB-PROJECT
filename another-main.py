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

print("==========================================[[WELCOME]]===========================================")
print("1. To view Menu enter \"Menu\" or \"m\"")
print("2. To add to cart enter the item's Sno")
print("3. To view cart enter view cart")
print("4. Invoice I or i")
while True: 
    print("======================")
    a=input("Waiting for input --> ").strip()
    print("======================")
    if a in ("Menu", "m"):
        with open("Menu.txt","r") as menu:
            print(menu.read())
    elif a in ("1","6","7","8"):
        item, price= menu_items[a]
        print("Name:", item)
        print("Price:", price)
        print("Availability: Available")
        print("Would you like to add it to cart")
        b=input("--> ")
        if b in ("yes", "y"):
            try:
                qty = int(input("Enter quantity --> "))
                total = total + (price * qty)
                items_ordered.append((item, qty, total))
                print("Suprise Burger added !", "x", qty, "=", total)
            except ValueError:
                print("That ain't a number !?!?!?")
        elif b in ("no","n"):
            print("sad --(*)_(*)--")
        else:
            print("Skipping...")
    elif a=="2":
        print("Name: Pizza McPuff\nPrice: 68\nAvailability: Available")
        print("Would you like to add it to cart")
        b=input("--> ")
        if b in ("yes", "y"):
            cart_file.write("Pizza McPuff")
            print("Pizza McPuff added !")
        elif b in ("no","n"):
            print("sad --(*)_(*)--")
        else:
            print("Skipping...")    
    elif a=="3":
        print("Name: McFlurry Oreo (S/M)\nPrice:104/129\nAvailability: Available")
        print("Would you like to add it to cart")
        b=input("--> ")
        if b in ("yes", "y"):
            print("Small or Medium")
            c=input("S/M--> ")
            if c in ("Small", "S","s"):
                print("Small McFlurry Oreo added !")
                cart_file.write("McFlurry Oreo (S)")
            elif c in ("Medium", "M", "m"):
                print ("Medium McFlurry Oreo added !")
                cart_file.write("McFlurry Oreo (M)")
        elif b in ("no","n"):
            print("sad --(*)_(*)--")
        else:
            print("Skipping...")
    elif a=="4":
        print("Name: McFlurry Chocolate Overload (S/M)\nPrice: 134/165\nAvailability: Available")
        print("Would you like to add it to cart")
        b=input("--> ")
        if b in ("yes", "y"):
            print("Small or Medium")
            c=input("S/M--> ")
            if c in ("Small", "S","s"):
                print("Small McFlurry Chocolate Overload added !")
                cart_file.write("McFlurry Chocolate Overload (S)")
            elif c in ("Medium", "M", "m"):
                print ("Medium McFlurry Chocolate Overload added !")
                cart_file.write("McFlurry Chocolate Overload (M)")
        elif b in ("no","n"):
            print("sad --(*)_(*)--")
        else:
            print("Skipping...")
    elif a in ("Invoice", "I","i"):
        print("Enter detetails for Invoice")
        name=input("Name ")
        while True:
            try:
                phone=int(input("Phone number "))
                break
            except ValueError:
                print("Enter the number damnit")
        address=input("Address ")
        with open("filename.txt", "w+") as file:
            file.write("======= McDonald's Delivery Invoice =======\n")
            file.write(f"Date: {now.strftime('%d-%m-%Y %H:%M:%S')}\n")
            file.write(f"Customer Name: {name}\n")
            file.write(f"Phone: {phone}\n")
            file.write(f"Address: {address}\n")
            file.write("-------------------------------------------\n")
            file.write("Items Ordered:\n")

            for item_name, qty, amount in items_ordered:
                file.write(f"{item_name} x{qty} = ₹{amount}\n")

            file.write("-------------------------------------------\n")
            file.write(f"Total Bill: ₹{total}\n")
            file.write("Thank you for ordering from McDonald's!\n")
            file.write("Your food will be delivered shortly 🍟🍔\n")
            file.seek(0)
            print(file.read())
    else:
        print("Please choose something from the given options")