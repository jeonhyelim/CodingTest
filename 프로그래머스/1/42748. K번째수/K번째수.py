def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        arr = array[commands[i][0] - 1 : commands[i][1]]
        arr.sort()
        answer.append(arr[commands[i][2] - 1]) #k번째 숫자
    return answer