print("Swapping to two number ")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number:"))

print("\n using using third variable")
print("Before swapping: a = ",a," b = ",b)
c = a
a = b
b = c
print("after swapping: a = ",a," b = ",b)

print("\n Without using third variable")
print("Before swapping: a = ", a, " b = ", b)
a = a + b
b = a - b
a = a - b
print("After swapping: a = ",a," b = ",b)

