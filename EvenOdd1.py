def isEvenOdd(n):
    if(n%2==0):
        return True
    else:
        return False

a= int(input("Enter a number: "))
if(isEvenOdd(a)):
    print("Number is Even")

else:
    print("number is Odd")