s =input()


h = [0]*256
for i in range(len(s)):
    h[ord(s[i])] += 1

#abcdefghijklmnopqrstuvwxyz

q = int(input())

while(q>0):
    c = input()
    print(h[ord(c)])

    q -= 1