n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    print(a[i],end=' ')
if n%2!=0:
    print('0')