n = int(input("Enter Total No of Elements : "))
arr = []

for i in  range(1,n+1):
    element = int(input(f"Enter element {i} : "))
    arr.append(element)

mpp ={}

for i in range(n):
    if arr[i] in mpp:
        mpp[arr[i]] += 1
    else:
        mpp[arr[i]] =1

for key,values in mpp.items():
    print(f"{key} -> {values}")


maxfreq = max(mpp.values())  # Find the highest frequency
minfreq = min(mpp.values())  # Find the lowest frequency
maxelement = next(key for key, value in mpp.items() if value == maxfreq)  # Find the element with the highest frequency
minelement = next(key for key, value in mpp.items() if value == minfreq)  # Find the element with the lowest frequency



# maxfreq = 0
# minfreq = n
# maxelement = 0
# minelement = 0

# for key,values in mpp.items():
#     if(values > maxfreq):
#         maxfreq = values
#         maxelement = key
#     if(values<minfreq):
#         minfreq = values
#         minelement = key


print(f" Highest occurence {maxelement} -> {maxfreq}")
print(f" Lowest occurence {minelement} -> {minfreq}")
