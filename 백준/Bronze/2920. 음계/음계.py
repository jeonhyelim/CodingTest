a = list(map(int,input().split(' ')))

ascending = True
descending = True

for i in range(1,8): #1~7
    if a[i] > a[i-1]: #a1>a0 오름차순
        descending = False
    elif a[i] < a[i-1]: #a1<a0 내림차순
        ascending = False
        
if ascending == True:
    print("ascending")
elif descending == True:
    print("descending")
else:
    print("mixed")
