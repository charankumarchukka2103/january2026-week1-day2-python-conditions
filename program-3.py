a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))
if(a>b and a>c):
    print("A is largest than the other numbers")
elif(b>a and b>c):
    print("B is largest than the other numbers")
elif(c>a and c>b):
    print("C is largest than  the other numbers")
    
    
    
    
#This program compares three input numbers (a, b, and c) to determine which one is the largest.
#The first condition checks if 'a' is greater than both 'b' and 'c. If true, it prints that 'A is largest than the other numbers'.
#If the first condition is false, it checks the second condition to see if 'b' is greater than both 'a' and 'c'. If true, it prints that 'B is largest than the other numbers'.
#If both previous conditions are false, it checks the third condition to see if 'c' is greater than both 'a' and 'b'. If true, it prints that 'C is largest than the other numbers'.