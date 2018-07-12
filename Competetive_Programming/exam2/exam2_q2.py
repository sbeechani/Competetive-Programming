ip = eval(raw_input())
l = len(ip)
op = [0 for i in range(l)]
for i in range (l):
    for j in range (i,l):
        if(ip[j][0]<ip[i][0]):
           (ip[j],ip[i])=(ip[i],ip[j])
for x in ip:
    k = x[1]
    count = 0
    index = 0
    while(count<k and index<l):
        if(op[index]==0):
            count+=1
        index+=1
    while(op[index]!=0):
        index+=1
    op[index]=x
print op
    
