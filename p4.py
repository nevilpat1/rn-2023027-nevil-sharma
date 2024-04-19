print("# to find factorial of any integer number")
num=int(input("enter a number:"))
factorial=1
if num<0:print("sorry, factorial does not exist for negative numbers")
elif num==0:print("The factorial of 0 is 1")
for i in range (1, num+1): factorial=factorial*i
print("the factorial of", num, "is", factorial)

