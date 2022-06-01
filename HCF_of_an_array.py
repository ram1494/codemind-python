n=int(input())
a=list(map(int,input().split()))
hcf=a[0]
i=0
j=1
while j<n:
    if a[j]%hcf==0:
        j+=1
    else:
        hcf=a[j]%hcf
        i+=1
print(hcf)
        
        
        
        