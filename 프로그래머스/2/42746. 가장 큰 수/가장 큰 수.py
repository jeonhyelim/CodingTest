def solution(numbers):
    num_list = list(map(str, numbers))
    num_list.sort(key=lambda x: x*3, reverse = True) #각 문자열 3번 반복하여 정렬기준으로 삼음, 내림차순(큰수부터)
    
    if num_list[0] == '0':
        return '0'
    
    return ''.join(num_list)
    
