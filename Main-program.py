names=[]
passwords=[]
#def Register_user():
'''while True:
    username=input("Your name ")
    pw=input("Password ")
    
    if username in names:
        print("Name already exists ")
        #break
    else:
        names.append(username)
        passwords.append(pw)
        print("Profile created")'''

bookname=[]
bookauthor=[]
bookdesc=[]
buyprice=[]
rentprice=[]

#def booklist():
while True:
    book_name=input("Book title ")
    book_author=input("Author name ")
    book_desc=input("short description ")
    buy_price=input("buy price ")
    rent_price=input("rent price ")

    if book_name in bookname:
        if book_author in bookauthor:
            print("book already registered! ")
        
    else:
        print("book added")