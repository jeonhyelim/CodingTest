def solution(edges):
    
    answer = [0,0,0,0]
    
    max_val = max(map(max,edges)) + 1
    
    in_cnt = [0]*max_val
    out_cnt = [0]*max_val
    
    for u, v in edges:
        out_cnt[u] += 1
        in_cnt[v] += 1
        
    for node in range(1,max_val):
        if in_cnt[node]==0 and out_cnt[node]>=2: # 생성정점이면
            answer[0] = node
        elif in_cnt[node]>=1 and out_cnt[node]==0:
            answer[2] += 1
        elif in_cnt[node] >= 2 and out_cnt[node] == 2: # 8자 그래프     
            answer[3] += 1
        
    answer[1] = out_cnt[answer[0]] - (answer[2]+ answer[3])
    
    return answer