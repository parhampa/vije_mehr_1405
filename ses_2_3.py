x=int(input("please insert your number: "))
count=0
for i in range(2,x):
    if x%i==0:
        print("aval nist")
        count+=1
        break
if count==0:
    print("aval ast")