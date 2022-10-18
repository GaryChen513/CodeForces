for _ in range(int(input())):
    n=int(input())
    s=input()
    a=list(map(int,input().split()))
    t,l=[0,-2147483]
    for i in range(0,n):
        if s[i]=='1':
            t+=max(a[i],l)
        if s[i]=='0' or a[i]<l:
            l=a[i]
    print(t)