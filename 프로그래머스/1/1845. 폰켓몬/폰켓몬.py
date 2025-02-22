def solution(nums):
    answer = 0
    chosen_length = len(nums)//2
    
    tmp = set(nums) #num 리스트에서 중복 제거한 집합
    num_li = list(tmp) #집합->리스트
    answer_leng = len(num_li)
    
    if chosen_length < answer_leng:
        answer = chosen_length
    else:
        answer = answer_leng
        
    return answer