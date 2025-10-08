from math import ceil
def solution(fees, records):
    
    # 주차요금 dic 만들기
    in_dic = {}      # 차량번호 : 입차 시간
    total_dic = {}   # 차량번호 : 총 주차 시간
    
    for rec in records:
        time, car, stat = rec.split()
        h, m = map (int, time.split(':'))
        minutes = h*60 + m
        
        if stat == "IN":
            in_dic[car] = minutes
        else: # OUT
            # 주차 시간 계산
            parked_time = minutes - in_dic[car]
            # 총 주차 시간 누적
            total_dic[car] = total_dic.get(car,0) + parked_time
            # 입차 기록 삭제
            del in_dic[car]

    # 출차 없으면 23:59로 처리
    for car, in_time in in_dic.items():
        parked_time = (23*60+59) - in_time
        total_dic[car] = total_dic.get(car,0) + parked_time
    
    # 주차요금 계산
    answer =[]
    for car in sorted(total_dic.keys()):
        time = total_dic[car]

        if time <= fees[0]:
            fee = fees[1] # 기본요금부과
        else:
            fee = fees[1]+ceil((time-fees[0])/fees[2])*fees[3]
        answer.append(fee)
    
    return answer