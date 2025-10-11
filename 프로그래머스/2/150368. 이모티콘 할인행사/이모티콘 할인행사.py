def solution(users, emoticons):
    answer = [0, 0]  # [이모티콘 플러스 가입자 수, 총 수익]
    data = [10, 20, 30, 40]  # 가능한 할인율
    discount = []  # 각 이모티콘의 할인율 조합을 저장할 리스트

    # [1] 모든 할인율 조합 구하기 (DFS)
    def dfs(temp, depth): # 현재까지 정해진 할인율 조합, 이모티콘의 인덱스
        # 모든 이모티콘에 대해 할인율을 정했다면 결과에 추가
        if depth == len(temp):
            discount.append(temp[:])  # deepcopy (값 복사)
            return

        # 현재 depth(이모티콘 인덱스)에 대해 10,20,30,40 중 하나씩 시도
        for d in data:
            temp[depth] += d         # 현재 이모티콘의 할인율 설정
            dfs(temp, depth + 1)     # 다음 이모티콘으로 넘어감 (재귀 호출)
            temp[depth] -= d         # 백트래킹 (원상복구)

    # 이모티콘 개수만큼 할인율 자리를 만들어서 DFS 실행
    dfs([0] * len(emoticons), 0)

    # [2] 구한 모든 할인 조합(discount)에 대해 수익 계산
    for d in range(len(discount)):  # discount의 각 조합을 하나씩 꺼냄
        plus_user = 0  # 플러스 가입자 수
        profit = 0     # 수익

        # 각 유저별로 구매 계산
        for user in users:
            emoticon_buy = 0  # 유저가 구매한 총 금액
            user_discount_limit = user[0]  # 유저가 구매하려는 최소 할인율
            user_price_limit = user[1]     # 이 금액 이상이면 플러스 가입함

            # 모든 이모티콘 순회
            for i in range(len(emoticons)):
                # 유저의 기준 할인율보다 크거나 같으면 구매 대상
                if discount[d][i] >= user_discount_limit:
                    # 실제 구매 금액 계산 (할인 적용)
                    emoticon_buy += emoticons[i] * ((100 - discount[d][i]) / 100)

            # 유저의 구매 금액이 기준을 넘으면 플러스 가입자
            if user_price_limit <= emoticon_buy:
                plus_user += 1
            else:
                # 아니면 그냥 수익으로 더함
                profit += emoticon_buy

        # [3] 결과 갱신: 가입자 수 우선, 수익은 다음 순위
        if answer[0] < plus_user:  # 더 많은 플러스 가입자가 있다면 갱신
            answer = [plus_user, int(profit)]
        elif answer[0] == plus_user:  # 가입자 수가 같다면
            if answer[1] < profit:    # 수익이 더 높은 경우 갱신
                answer = [plus_user, int(profit)]

    return answer