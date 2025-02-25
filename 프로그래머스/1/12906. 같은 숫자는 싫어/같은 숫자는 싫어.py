def solution(arr):
    stack = [-1]
    for i in range(len(arr)): #stack[-1](현재 stack의 마지막 값)과 arr[i](현재 검사 중인 값)을 비교
        if stack[-1] != arr[i]: #다르면 → 새로운 숫자이므로 stack에 추가
            stack.append(arr[i])
    return stack[1:]
    