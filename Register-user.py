names=[]
def Register_user():
    id=input("Your name ")
    pw=input("Password ")
    for i in range (names):
        if id==i:
            print("Name already exists ")
        else:
            print("Profile created")
