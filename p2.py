print ("# To solve quadratic equation a*x*x+b*x+c=0 where a, b, c are integers")
a=int(input("enter coefficient 'a' of x square:"))
b=int(input("enter coefficient 'b' of x:"))
c=int(input("enter the value of constant c:"))
d=(b*b-4*a*c)**0.5
x1=(-b+d)/(2*a)
x2=(-b-d)/(2*a)
print("the roots are", {x1}, "and", {x2})

