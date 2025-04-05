a = int(input("Enter a number: "))
def isPositive(n):
    if(n>0):
        return True
    else:
        return False
    
def isZero(n):
    if(n==0):
        return  True
    else:
        return False
    

def isNegative(n):
    if(n<0):
        return True
    else:
        return False
    
if(isPositive(a)):
    print("number is Positive")
if(isNegative(a)):
    print("number is Negative")
if(isZero(a)):
    print("number is Zero")
