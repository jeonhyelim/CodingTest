def solution(citations):
    citations.sort(reverse = True)
    n = len(citations)
    
    for i in range(n):
        if i >= citations[i]:
            return i

    return n #모든 논문이 조건을 만족x
