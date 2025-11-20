k=int(input("enter k: "))
page=0
digit=1
count=9

while k>count*digit:
    k-=count*digit
    page+=count
    digit+=1
    count*=10
page+= k//digit
print("page= ",page)
