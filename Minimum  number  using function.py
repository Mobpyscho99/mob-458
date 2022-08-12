a= (int)(input("Enter first no:"))
b= (int)(input("Enter second no:"))
c= (int)(input("Enter thrid no:"))

def min(a,b,c):
        smallest = 0

if a < b and a < c :
    smallest = a
elif b < c :
    smallest = b
else :
    smallest = c

print(smallest, "is the smallest of three numbers.")
 
     
