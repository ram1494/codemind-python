def gcd(N,M):
    if(M==0):
        return N
    else:
        return gcd(M,N%M)
N,M=map(int,input().split())
num=gcd(N,M)
print(num)