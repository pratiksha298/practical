def factorial(num):
    for i in range(1,num):
        num = num * i
    return num
n=int(input("Enter a number : "))
print("Factorial of", n, "is", factorial(n))