def fact(x):
    if x <= 1:
        return 1
    return x*fact(x-1)

x = int(input("Enter the number: "))
print(fact(x))