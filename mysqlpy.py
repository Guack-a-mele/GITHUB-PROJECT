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
    
