N=int(input())
largest=0
while(N>0):
    remainder=N%10
    if(largest<remainder):
        largest=remainder
    N=N//10
print(largest)