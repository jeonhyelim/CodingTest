N = int(input())
timeTable = [list(map(int, input().split())) for _ in range(N)]

# dp[i]: i일까지 얻을 수 있는 최대 수익을 저장하는 배열
dp = [0] * (N + 1)  

for i in range(N):
    time, profit = timeTable[i]

    # 이전 값을 현재 날짜에 반영 (이전까지의 최대 수익 유지)
    if i > 0:
        dp[i] = max(dp[i], dp[i - 1])

    # 상담을 진행할 경우 (퇴사일을 넘지 않는다면)
    if i + time <= N:
        dp[i + time] = max(dp[i + time], dp[i] + profit)

# 마지막 날까지 고려한 최댓값 출력
print(max(dp))