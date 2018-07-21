n = int(raw_input())
res = []
for i in range (n+1):
    x = str(bin(i))
    count = 0
    for j in x:
        if j is "1":
            count+=1
    res.append(count)
print res
