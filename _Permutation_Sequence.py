from itertools import permutations
a,b=map(int,input().split())
I=list(permutations(range(1,a+1)))
for i in I[b-1]:
    print(i,end='')