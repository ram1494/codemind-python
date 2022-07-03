x=int(input())
s=0
for i in range(x):
    n=input()
    I=len(n)
    for j in n:
        if j>='0' and j<='9':
            s+=1
    if I==s:
        print(True)
    else:
        print(False)
    s=0