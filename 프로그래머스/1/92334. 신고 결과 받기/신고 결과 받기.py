def solution(id_list, report, k):
    answer = []
    dic = {}
    for id in id_list:
        dic[id] = [0,[]]
        
    for i in report:
        a,b = i.split() #a 신고한유저, b 신고당한유저
        # id의 신고내역을 dic에 추가
        if b not in dic[a][1]:
            dic[a][1].append(b)
            dic[b][0] += 1
    
    lst = [] # k이상이면 정지시킴
    for i in dic.items():
        if i[1][0] >= k:
            lst.append(i[0])
            
    for i in dic.values(): # (횟수,리스트)
        cnt = 0
        for j in lst:
            if j in i[1]:
                cnt += 1
        answer.append(cnt)
            
    
    
    return answer