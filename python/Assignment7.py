n=int(input ("Enter a positive number: "))
fact=1
for i in range (1,n+1):
    fact=fact*i
    
print("Factorial of ",n,"=",fact)