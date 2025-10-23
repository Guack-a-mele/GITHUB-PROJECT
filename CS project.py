import pickle
def showData():
stu={}
fp=open("stu.dat","rb")
print("Roll\tName\tCity")
flag=False
try:
while True:
stu=pickle.load(fp)
#print(emp1)
print(stu['roll'],'\t',stu['name'],'\t',stu['city'])
except EOFError:
fp.close()
def deleteData():
stu={}
fp=open("stu.dat","rb")
r=int(input("Enter the Roll No. for Delete : "))
l1=[]
flag=False
try:
while True:
stu=pickle.load(fp)
#print(emp1)
if stu['roll']!=r:
#print(stu['roll'],'\t',stu['name'],'\t',stu['city'])
l1.append(stu)
flag=True
except EOFError:
fp.close()
if flag==False:
print("Record Not Found " )
else:
print("Record Deleted" )
fp=open("stu.dat","wb")
for a in l1:
pickle.dump(a,fp)
fp.close()
def searchData():
stu={}
fp=open("stu.dat","rb")
r=int(input("Enter the Roll No. for Search : "))
flag=False
try:
while True:
stu=pickle.load(fp)
#print(emp1)
if stu['roll']==r:
print(stu['roll'],'\t',stu['name'],'\t',stu['city'])
flag=True
break
except EOFError:
fp.close()
if flag==False:
print("Record Not Found " )
def addData():
stu={}
fp=open("stu.dat","ab")
while True:
r=int(input("Enter Roll No : "))
n=input("Enter name")
c=input("Enter City")
stu['roll']=r
stu['name']=n
stu['city']=c
pickle.dump(stu,fp)
a=input("if you want to add more data press Y")
if a not in ['Y','y']:
break
fp.close()
while True:
print("1. Add New Student\n2.Print List of Student\n 3.Search any Student\n4.Delete Record \n5.Exit")
ch=int(input("Enter Your Choice : "))
if ch==1:
addData()
elif ch==2:
showData()
elif ch==3:
searchData()
elif ch==4:
deleteData()
elif ch==5:
break
else:
print("Invalid Choice ")
a