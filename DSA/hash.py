n = int(input())
l=[]*n
for i in range(n):
   i = int(input())
   l.append(i)


hash = [0]*13
for i in range(n):
    hash[l[i]] += 1


q = int(input())
while(q > 0):
    number = int(input())
    print(hash[number])
    q -= 1