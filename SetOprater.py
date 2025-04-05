print("Use of set Operator ...\n")
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
print("setA = ", setA)  
print("setB = ", setB)

print("\n Perform Opration by using oprator : \n")
print("Union of setA and setB is ", setA | setB)
print("Intersection of setA and setB is ", setA & setB)
print("set Differnce of setA and setB is ", setA - setB )
# print("Symmetric Differnce of setA and setB is ", setA ^ setB)

print("\n Perform Opration by using method : \n")

print("Union of setA and setB is ", setA.union(setB))
print("Intersection od setA and setB is ", setA.intersection(setB))
print("set Differnce of setA and setB is ", setA.difference(setB))
# print("Symmetric Differnce of setA and setB is  ", setA.symmetric_difference(setB))