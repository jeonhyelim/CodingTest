n = int(input())
tester = list(map(int, input().split()))
a,b = map(int,input().split())

cnt = n #필요한 감독관 주감독관
for i in tester:
    i -= a #주감독관
    if i>0: #부감독관추가
        if i%b == 0:
            cnt += (i//b)
        else:
            cnt += (i//b)+1
            
print(cnt)