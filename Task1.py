print("-----------CLI Calculator------------")

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

n = int(input("Select The Operation : "))

if n==1:
    print("Result :",a+b)
elif n==2:
    print("Result :",a-b)
elif n==3:
    print("Result :",a*b)
elif n==4:
    if b==0:
        print("Cannot divide by zero")
    else:
        print("Result :", a/b)
else:
    print("Invalid Operation")