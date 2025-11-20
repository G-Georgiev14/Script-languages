n = int(input("enter n:"))
spisuk = []
sum = 0

for i in range(n):
    number = int(input("enter number:"))
    spisuk.append(number)

for j in spisuk:
    sum=sum + j**2
print("sum= ", sum)