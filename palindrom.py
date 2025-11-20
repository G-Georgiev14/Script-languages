s=input("enter text: ")
i,j=0,len(s)-1
palindrome=True

while i<j:
    if s[i]is not s[j]:
       palindrome=False
       break
    i+=1
    j-=1

if palindrome:
    print("palindrome")
else:
    print("not palindrome")

