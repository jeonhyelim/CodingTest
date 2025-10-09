def solution(n, info):
    
    max_diff = 0
    answer = [-1]
    
    # 점수를 계산
    def calc(ryan):
        ry_score, ap_score = 0, 0
        for i in range(11): # 0점부터 10점까지 차례로 확인
            if info[i]==0 and ryan[i]==0:
                continue
            if ryan[i] > info[i]:
                ry_score += 10-i
            else:
                ap_score += 10-i
        return ry_score - ap_score
        
        
    def dfs(idx,arrows_left,ryan):
        nonlocal max_diff, answer
        
        if idx == 11:
            if arrows_left > 0:
                ryan[10] += arrows_left
            diff = calc(ryan)
            if diff>0:
                if diff>max_diff:
                    max_diff = diff
                    answer = ryan[:]
                elif diff == max_diff:
                    # 낮은 점수 많이 맞힌 것을 우선
                    for i in range(10, -1, -1):
                        if ryan[i] > answer[i]:
                            answer = ryan[:]
                            break
                        elif ryan[i] < answer[i]:
                            break
            if arrows_left > 0:
                ryan[10] -= arrows_left
            return
            
        
        for i in range(arrows_left+1):
            ryan[idx] = i
            dfs(idx+1,arrows_left - i, ryan)
            ryan[idx]=0
            
        
    dfs(0,n,[0]*11)
    return answer