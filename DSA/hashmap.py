n = int(input("Enter total elements in arr: "))
arr = []
mpp = {}
for _ in range(n):
    i = int(input())
    arr.append(i)
    if i in mpp:
        mpp[i] += 1
    else:
        mpp[i] = 1

#pre compute

    


for key,values in mpp.items():
    print(f"{key} -> {values}")


# q= int(input("How many to find: "))
# while(q>0):
#     number = int(input())

#     #fetch
#     print(mpp.get(number,0))


#     q -=1