def team(a,n):
    global result #최소 능력치 차이
    
    if a == N//2: #종료
        start, link = 0,0
        
        #모든사람을 대상으로 능력치 계산
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]: #i j 둘 다 방문했으면
                    start += S[i][j]
                elif not visited[i] and not visited[j]:
                    link += S[i][j]
        
        #능력치 차이 최솟값            
        result = min(result, abs(start - link))
        return
    
    #백트래킹을 통해 팀 조합 탐색
    for x in range(n, N):
        if not visited[x]: #아직 선택x
            visited[x] = 1 #스타트팀에 포함
            team(a+1, x+1) #재귀호출(다음사람 선택하여 팀 구성)
            visited[x] = 0 #백트래킹(원래 상태로)
            

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
result = float('inf')
team(0,0) #백트래킹 시작
print(result)
