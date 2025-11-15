myscon=mys.connect(host=) #Table is Menu
cursor_=mys.cursor()
print("==========================================[[WELCOME]]===========================================")
print("1. To view Menu enter \"Menu\" or \"m\"")
print("2. To add to cart enter the item's Sno")
print("3. To view cart enter view cart")
print("4. Invoice I or i")
while True: 
    print("======================")
    a=input("Waiting for input --> ").strip()
    print("======================")
  if a in ("Menu", "select S"):
    cursor.execute("select SNo, ItemPrice, Availability from Menu")
    Ret=cursor_.fetchall()
    cursor_.execute("select SNo,Item name, ItemPrice, Availability from Menu")
    Ret=cursor_.fetchall()
    conn.commit()
      
    widths=[]
    columns=[]
    tavnit='|'
    separator='+'
    for cd in cursor.description:
       widths.append(max(cd[2], len(cd[0])))
       columns.append(cd[0])
    for w in width:
       tavnit+="%-"+"%ss |" %(w,)
       seperator+='-'*w+'--+'

     print(seperator)
     print(tavnit%tuple(columns))
     print(seperator)
     for row in Ret:
         print(tavnit%row)
     print(seperator)
  elif a in cou:
     cursor_.execute("select ItemName,ItemPrice,Checknull from Menu where SNo="a")
     Ret=cursor_.fetchone())
     if Ret[1]=="not null":
        print("Name:",Ret[0],"Price:"Ret[1],"Availability: Available")
        print("Would you like to add it to cart")
        b=input("--> ")
        if b in ("yes", "y"):
            print("Small or Medium")
            c=input("S/M--> ")
            if c in ("Small", "S","s"):
                print("Small", Ret[0],"added !")
                try:
                    qty = int(input("Enter quantity --> "))
                    total = total + (price * qty)
                    items_ordered.append((item, qty, total))
                    print(Ret[0],"added !",price, "x", qty, "=", total)
                except ValueError:
                    print("That ain't a number !?!?!?")
            elif c in ("Medium", "M", "m"):
                print ("Medium", Ret[0],"added !")
                try:
                    qty = int(input("Enter quantity --> "))
                    total = total + (price * qty)
                    items_ordered.append((item, qty, total))
                    print(Ret[0],"added !",price, "x", qty, "=", total)
                except ValueError:
                    print("That ain't a number !?!?!?")
        elif b in ("no","n"):
            print("sad --(*)_(*)--")
        else:
            print("Skipping...")
     else:
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
                print("Suprise Burger added !",price, "x", qty, "=", total)
            except ValueError:
                print("That ain't a number !?!?!?")
        elif b in ("no","n"):
            print("sad --(*)_(*)--")
  elif a=="Exit":
      break
