# McDaddy delivery system
items_ordered= []
menu_items = {}

with open("impmenu.txt", "r") as file:
    for i, line in enumerate(file, start=1): # learn this (NKS)
        if "-" in line:
            name, price = line.strip().split(" - ")
            menu_items[str(i)] = (name, int(price))

print("==========================================[[WELCOME]]===========================================")
cart_file=open("Cart.txt","w")
print("1. To view Menu enter \"Menu\" or \"m\"")
print("2. To add to cart enter the item's Sno")
print("3. To view cart enter view cart")
print("4. EXIT --> EE")
while True: 
    print("======================")
    a=input("Waiting for input --> ").strip()
    print("======================")
    if a in ("Menu", "m"):
        with open("Menu.txt","r") as menu:
            print(menu.read())
    elif a=="1":
        print("Name: Suprise Burger\nPrice: 75\nAvailability: Available")
        print("Would you like to add it to cart")
        b=input("--> ")
        if b in ("yes", "y"):
            try:
                qty = int(input("Enter quantity --> "))
                total = price * qty
                items_ordered.append((item, qty, total))
                print("Suprise Burger added !", "x", qty, "=", total)
            except ValueError:
                print("Invalid input")
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
    elif a=="5":
        print("Name: McFlurry Black Forest (M)\nPrice:136\nAvailability: Available ")
        b=input("--> ")
        if b in ("yes", "y"):
            cart_file.write("Medium McFlurry Black Forest")
            print("McFlurry Black Forest added !")
        elif b in ("no","n"):
            print("sad --(*)_(*)--")
        else:
            print("Skipping...")
    elif a=="6":
        print("Name: McAloo Tikki (Single/double patty)\nPrice: 74/93\nAvailability: Available")
        print("Would you like to add it to cart")
        if b in ("yes", "y"):
            print("Single patty or Double patty")
            c=input("S/D--> ")
            if c in ("Single patty","Single", "S","s"):
                print("Single patty McAloo Tikki added !")
                cart_file.write("Single patty McAloo Tikki")
            elif c in ("Double patty","Double", "D", "d"):
                print ("Double patty McAloo Tikki added !")
                cart_file.write("Double patty McAloo Tikki")
        elif b in ("no","n"):
            print("sad --(*)_(*)--")
        else:
            print("Skipping...")
    elif a=="7":
        print("Name: Crispy Veggie burger\nPrice: 198\nAvailability: Available")
        print("Would you like to add it to cart")
        b=input("--> ")
        if b in ("yes", "y"):
            cart_file.write("Crispy Veggie burger")
            print("Crispy Veggie burger added !")
        elif b in ("no","n"):
            print("sad --(*)_(*)--")
        else:
            print("Skipping...")
    elif a=="8":
        print("Name: McCrispy Chicken burger\nPrice:222\nAvailability: Available")
        print("Would you like to add it to cart")
        b=input("--> ")
        if b in ("yes", "y"):
            cart_file.write("McCrispy Chicken burger")
            print("McCrispy Chicken burger added !")
        elif b in ("no","n"):
            print("sad --(*)_(*)--")
    elif a=="Suprise Burger":
        cart_file.write("Suprise Burger")
        print("Suprise Burger added !")
    elif a=="Pizza McPuff":
        cart_file.write("Pizza McPuff")
        print("Pizza McPuff added !")
    elif a=="EE":
        break
    else:
        print("Please choose something from the given options")