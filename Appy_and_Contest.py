n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    x=0
    if b%c==0:
        x=b
    elif c%b==0:
        x=c
    else:
        x=b*c
    q=a//x
    w=a//b
    e=a//c
    w=w-q
    e=e-q
    if w+e>=d:
        print('Win')
    else:
        print('Lose')
    