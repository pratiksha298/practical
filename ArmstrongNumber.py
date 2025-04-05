def isArmstrong(num):
    n = len(str(num))
    temp= sum(int(digit) ** n for digit in str(num))
    if temp == num:
        return True
    else:
        return False
number = int(input("Enter a number: "))
if isArmstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
