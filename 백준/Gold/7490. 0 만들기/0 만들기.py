import copy

#연산자 조합 재귀함수
def recursive(array,n):
    if len(array) == n:
        operators_list.append(copy.deepcopy(array))
        return
    array.append(' ')
    recursive(array,n)
    array.pop()
    
    array.append('+')
    recursive(array,n)
    array.pop()
    
    array.append('-')
    recursive(array,n)
    array.pop()
    
    
test_case = int(input())

#각 테스트 케이스 실행
for _ in range(test_case):
    operators_list = []
    n = int(input())
    
    recursive([],n-1) #연산자 조합 생성 : n-1개
        
    integers = [i for i in range(1,n+1)] #1~n까지의 리스트 생성
        
    #생성된 연산자 조합 이용한 수식 생성
    for operators in operators_list:
        string = "" #수식 저장할 문자열 초기화
        
        for i in range(n-1):
            string += str(integers[i]) + operators[i]
        string += str(integers[-1])
        
        if eval(string.replace(" ","")) == 0:
            print(string)
            
    print()