print("Check Prime Number ")
num = int(input("Enter a number : "))
def isPrime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    else:
        return False

if isPrime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")