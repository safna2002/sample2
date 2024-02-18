l=[45, 78, 4, 34, 67, 3, 93, 101, 77]
s=[]
for i in range(0,len(l)):
    if(l[i]%2==0):
        continue
    else:
        s.append(l[i])
print(s)
