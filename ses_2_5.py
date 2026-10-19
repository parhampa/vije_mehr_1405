for x in range(1,1001):
    count=0
    for i in range(2,x):
        if x%i==0:
            count+=1
            break
    if count==0:
        print(x)