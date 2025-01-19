def solve(n,x,y):
    global result #현재까지 몇 번째 칸 방문했는지 저장
    
    #2x2 case
    if n == 2:
        #왼쪽 위 (x,y)
        if x == X and y == Y: #목표 좌표 (X,Y)에 도달했을 경우
            print(result)
            return
        result += 1
        
        #오른쪽 위 (x,y+1)
        if x == X and y+1 == Y:
            print(result)
            return
        result += 1
        
        #왼쪽 아래(x+1,y)
        if x+1 == X and y == Y:
            print(result)
            return
        result += 1
        
        #오른쪽 아래 (x+1,y+1)
        if x+1 == X and y+1 == Y:
            print(result)
            return
        result += 1
        return
    
    #재귀- 4사분면으로 나눠서 탐색
    #solve(n/2,x,y)
    #solve(n/2,x,y+n/2)
    #solve(n/2,x+n/2,y)
    #solve(n/2,x+n/2,y+n/2)
    
    # 격자의 절반 크기
    half = n // 2

    # 목표 좌표가 어느 사분면에 속하는지 확인
    if X < x + half:  # 위쪽 절반
        if Y < y + half:  # 왼쪽 위 사분면
            solve(half, x, y)
        else:  # 오른쪽 위 사분면
            result += half * half  # 왼쪽 위 사분면의 칸을 건너뜀
            solve(half, x, y + half)
    else:  # 아래쪽 절반
        if Y < y + half:  # 왼쪽 아래 사분면
            result += 2 * half * half  # 위쪽 두 사분면의 칸을 건너뜀
            solve(half, x + half, y)
        else:  # 오른쪽 아래 사분면
            result += 3 * half * half  # 위쪽 두 사분면과 왼쪽 아래 사분면의 칸을 건너뜀
            solve(half, x + half, y + half)

    
result = 0
N,X,Y = map(int, input().split(' '))

solve(2 ** N,0,0) #전체 격자 크기 2^N x 2^N