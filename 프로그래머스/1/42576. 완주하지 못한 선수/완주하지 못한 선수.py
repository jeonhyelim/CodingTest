def solution(participant, completion):
    participant.sort()
    completion.sort() #오름차순 정렬
    for i,j in zip(participant,completion):
        if i != j:
            return i
        
    return participant[-1]