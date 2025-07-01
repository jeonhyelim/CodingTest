def solution(clothes):
    
    # hash map
    clothes_dict = {}
    for i in clothes:
        if i[1] in clothes_dict:
            clothes_dict[i[1]] += 1
        else:
            clothes_dict[i[1]] = 1
            
    # 경우의 수 계산
    answer = 1
    for _, v in clothes_dict.items():
        answer *= (v + 1)
        
    # 전부 안 입는 경우 제외
    answer -= 1
    
    return answer
    