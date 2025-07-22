# BFS
def solution(numbers, target):
    # 계산의 시작점이 될 0을 리스트에 담아 초기화
    leaves = [0]
    
    # numbers 리스트의 각 숫자를 순회
    for num in numbers:
        temp = []
        # 이전 단계까지의 모든 결과(leaves)에 현재 숫자를 더하고 뺀 값을 temp에 저장
        for leaf in leaves:
            temp.append(leaf + num)
            temp.append(leaf - num)
        # 다음 연산을 위해 leaves를 최신 결과(temp)로 갱신
        leaves = temp
        
    # 최종 결과가 담긴 leaves 리스트에서 target과 일치하는 값의 개수를 세어 반환
    return leaves.count(target)
