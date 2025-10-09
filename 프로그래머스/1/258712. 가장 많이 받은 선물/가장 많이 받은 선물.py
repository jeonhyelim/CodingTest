def solution(friends, gifts):
    
    answer = 0
    
    n = len(friends)
    friend_dict = dict()
    
    for i in range(n):
        friend_dict[friends[i]] = i
        
    table = [[0]*n for _ in range(n)] # 표
    gift_num = [0] * n # 선물지수
    
    for g in gifts:
        giver,taker = g.split()
        idx1, idx2 = friend_dict[giver], friend_dict[taker]
        gift_num[idx1] += 1
        gift_num[idx2] -= 1
        table[idx1][idx2] += 1
        
    get_gift = [0]*n 
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if table[i][j] > table[j][i]:
                get_gift[i] += 1
            elif table[i][j] == table[j][i]:
                if gift_num[i]> gift_num[j]:
                    get_gift[i] += 1
            
    answer = max(get_gift)
    
    return answer