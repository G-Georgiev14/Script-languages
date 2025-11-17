n=int(input("Enter n: "))
list=[]
for i in range(n):
    x=int(input("Enter element: "))
    list.append(x)
    
list.sort()
print(list)