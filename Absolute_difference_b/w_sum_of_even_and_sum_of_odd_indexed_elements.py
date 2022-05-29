n=int(input())
a=list(map(int,input().split()))
s=0
s1=0
for i in range(n):
    if i%2==0:
        s+=a[i]
    elif i!=0:
        s1+=a[i]
print(abs(s1-s))