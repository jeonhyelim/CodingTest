def ascending(array): #왼쪽에서 봤을때 트로피가 몇 개 보이는지
    now = array[0] #현재 보이는 트로피의 높이
    result = 1 #첫 번째 보이고 있는 트로피
    for i in range(1, len(array)): #두 번째 트로피부터 끝까지 탐색
        if now < array[i]: #높은 트로피
            result += 1 #보이는 트로피 + 1
            now = array[i]
    return result


n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))
print(ascending(array))
array.reverse()
print(ascending(array)) #오른쪽에서 보았을 때
