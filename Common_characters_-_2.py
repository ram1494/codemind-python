s=input().lower()
I=s.split()
I1=list(I[0])
I.remove(I[0])
c=0
e=[]
for i in I1:
    for j in range(len(I)):
        if i not in I[j] and i not in e:
            break
    else:
        e.append(i)
print(len(e))