string=input()
I=len(string)
c=1
co=0
for i in range(0,I-1):
    if string[i]==string[i+1]:
        c+=1
    else:
        if co<c:
            co=c
        c=1
if co<c:
    co=c
print(co)