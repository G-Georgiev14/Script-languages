set = {"peach", "apple", "banana", "cherry", "chips", "pizza", "orange"}
list=["apple", "pizza"]
for i in range(len(list)):
    set.discard(list[i])
print(set)
    