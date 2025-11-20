n=int(input("enter n: "))
str = []
lenght = 0

for i in range(n):
    text=input("enter text: ")
    str.append(text)

for j in str:
    lenght += len(j)

lenght = lenght/n

print("avg len= ",lenght)
