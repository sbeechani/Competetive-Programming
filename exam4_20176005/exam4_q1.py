n = int(raw_input())
b = str(bin(n))
maxi = 0
count=0
print b
for x in b:
    if x is "0":
        if(count>maxi):
            maxi=count
            count = 0
    elif x is "1":
        count+=1
if(count>maxi):
            maxi=count
print maxi
