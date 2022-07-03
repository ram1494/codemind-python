n=int(input())
c,s,t=0,0,n
while n>0:
    r=n%10
    n//=10
    c+=1
n=t
while n>0:
    r=n%10
    s=s+pow(r,c)
    n=n//10
    c-=1
if s==t:
    print("True")
else:
    print("False")