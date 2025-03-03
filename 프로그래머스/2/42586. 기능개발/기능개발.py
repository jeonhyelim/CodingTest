def solution(progresses, speeds):
    answer = []
    days = 0
    cnt = 0 #완료된 기능
    
    while len(progresses) > 0:
        if(progresses[0] + days*speeds[0]) >= 100: #완료
            
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0: #완료된 기능이 있으면
                answer.append(cnt)
                cnt = 0
            else: #완료된 기능이 없으면 days 추가
                days += 1
                
    answer.append(cnt)
    return answer