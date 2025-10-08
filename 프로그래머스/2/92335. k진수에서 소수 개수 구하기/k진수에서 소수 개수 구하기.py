def solution(n, k):
    word = ""
    
    # 숫자 n을 k 진수로 변환
    while n:
        word = str(n%k) + word
        n = n//k
    
    # k진수 숫자n을 0 기준으로 나눔
    word = word.split("0")
    
    count = 0

    for w in word:
        if len(w) == 0:
            continue
        num = int(w)
        
        if num <2:
            continue
            
        sosu = True

        # 소수인지 판별
        for i in range(2,int(num**0.5) + 1):
            if num % i ==0:
                sosu = False
                break
        if sosu == True:
            count += 1 
    
    return count