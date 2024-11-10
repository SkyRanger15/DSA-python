import math
def checkPrime(x):
    if x<=1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

x = int(input("Enter the number to check: "))
if checkPrime(x):
    print("Number is Prime")
else:
    print("Number is Not Prime")