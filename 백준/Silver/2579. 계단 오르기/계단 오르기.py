n = int(input())
s = [int(input()) for _ in range(n)]

dp = [0] * n

if len(s) <= 2: #계단이 2개 이하
    print(sum(s))
    
else: #계단이 3개 이상
    dp[0] = s[0] #첫 계단까지 도달했을 때의 최대 점수
    dp[1] = s[0] + s[1] #둘째 계단까지 도달했을 때의 최대 점수
    for i in range(2,n): #2~n-1
        dp[i] = max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])
        #i-2번째 계단에서 i번째 계단으로 ,i-3번째 계단에서 i-1을 거쳐 i로 이동
        
    print(dp[-1]) #리스트의 마지막 요소 dp[-1]=dp[n-1]