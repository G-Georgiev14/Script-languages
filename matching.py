tuple=("apple", "banana", "cherry")
for i in range(len(tuple)):
    if tuple.count(tuple[i])>1:
        print("Found a match:", tuple[i])
    else: 
        print("No match for:", tuple[i])
