a = list(map(int, input().split(' ') )) #map : 각각 원소를 int형으로 바꿈

ascending = True
descending = True

for i in range(1,8):
    if a[i] > a[i-1]:
        descending = False
    elif a[i] < a[i-1]:
        ascending = False
        
if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')