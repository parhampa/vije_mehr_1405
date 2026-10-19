a=int(input("please insert your first data "))
b=int(input("please insert your second data "))
print("for + insert 1: ")
print("for - insert 2: ")
print("for * insert 3: ")
print("for / insert 4: ")
print("for // insert 5: ")
print("for ** insert 6: ")
resact=int(input("please insert action: "))
c=0
if resact==1 :
    c=a+b
if resact==2 :
    c=a-b
if resact==3 :
    c=a*b
if resact==4 :
    c=a/b
if resact==5 :
    c=a//b
if resact==6 :
    c=a**b
    
print("resut of your action is: ",c)