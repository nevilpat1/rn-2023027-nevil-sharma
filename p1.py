print ("# to find the smallest and largest number")
print ("# enter 5 positive integers hitting 'enter' after each integer")
N=int(input())
smallest=0
largest=0
for i in range(N):
    entered_number = int(input())
    if (i==0):
        smallest=entered_number
    if (entered_number<smallest):
        smallest=entered_number
    if (entered_number>largest):
        largest=entered_number
print (smallest)
print (largest)
    
