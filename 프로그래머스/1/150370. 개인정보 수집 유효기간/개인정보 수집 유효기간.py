def solution(today, terms, privacies):
    answer = []
    dates= []
    types = []
    for p in privacies:
        date, type = p.split()
        dates.append(date)
        types.append(type)
    term = dict()
    for t in terms:
        a, b = t.split()
        term[a] = int(b)
    
    def date_calc(date):
        dy, dm, dd = map(int,date.split("."))
        return dy * 12 * 28+ dm * 28 + dd
    
    def re_date_calc(num):
        y= num // (12*28)
        m = ( num % (12*28) ) // 28
        d = ( num % (12*28) ) % 28
         # 보정 (0일 → 이전달 28일)
        if d == 0:
            d = 28
            m -= 1

        # 보정 (0월 → 이전해 12월)
        if m == 0:
            m = 12
            y -= 1

        return f"{y:04d}.{m:02d}.{d:02d}"
        
        
    # 각 p 별 현 날짜 - 유효기간
    lst_date = [0]*len(privacies)
    for i in range(len(privacies)):
        tmp = date_calc(dates[i])+(term[types[i]]*28)-1
        lst_date[i] = re_date_calc(tmp)
        
        if tmp < date_calc(today): 
            answer.append(i+1)
    
    return answer