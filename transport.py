n= int(input("Enter km:"))
dayNight = input("Day or Night? (d/n): ")
allPrice = 0
if n < 20:
    print("Your best option is taxi.")
    if dayNight == "d":
        allPrice = (n * 0.79) + 0.70
    else:
        allPrice = (n * 0.90) + 0.70
elif n >= 20 and n < 100:
    print("Your best option is bus.")
    allPrice = n * 0.09
elif n >= 100:
    print("Your best option is train.")
    allPrice = n * 0.06
print("Total price is:", allPrice)