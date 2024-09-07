"WAP to find the greatest of 3 numbers entered by the user."

a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
c = int(input("Enter c value: "))

if (a>b and a>c):
    print(a,"More than ",b,"and",c)
elif(b>a and b>c):
    print(b,"More than ",a,"and",c)
else:
    print(c,"More than ",a,"and",b)