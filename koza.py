while True:
    n=int(input("enter n: "))
    if n in range(1,1000):
        break
    else:
        print("enter valid n")

while True:
    k=int(input("enter k: "))
    if k in range(1,1000):
        break
    else:
        print("enter valid k")

kozi=[]

for i in range(n):
    while True:
        weight=int(input("enter weight: "))
        if weight in range(1,1000):
            break
        else:
            print("enter valid weight")
    kozi.append(weight)


kozi.sort(reverse=True)
print("sorted kozi=",kozi)

def check(capacity):
    
    used=[False]*n
    count=0
    for trip in range(k):
        currentload=0
        for i in range(n):
            if not used[i]:
                if currentload+kozi[i]<=capacity:
                    currentload+=kozi[i]
                    used[i]=True
                    count+=1
        if count==n:
            return True
    return count==n
min=kozi[0]
max=sum(kozi)
ans=max
while min<=max:
    mid=(min+max)//2
    if check(mid):
        ans=mid
        max=mid-1
    else:
        min=mid+1
print("min capacity= ",ans)



                

    
