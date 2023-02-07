from collections import deque


def bfs(n, info):
    res = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    maxGap = 0

    while q:
        focus, arrow = q.popleft()

        if sum(arrow) == n:  # 종료조건 1) 화살 다 쏜 경우
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:  # 라이언이 이기면
                gap = lion - apeach
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap  # 최대점수차 갱신
                    res.clear()
                res.append(arrow)  # 최대점수차를 내는 화살상황 저장

        elif sum(arrow) > n:  # 종료조건 2) 화살 더 쏜 경우
            continue

        elif focus == 10:  # 종료조건 3) 화살 덜 쏜 경우
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))

        else:  # 화살 쏘기
            tmp = arrow.copy()
            tmp[focus] = info[focus] + 1
            q.append((focus + 1, tmp))  # 어피치보다 1발 많이 쏘기
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus + 1, tmp2))  # 0발 쏘기
    return res


def solution(n, info):
    winList = bfs(n, info)

    if not winList:
        return [-1]
    elif len(winList) == 1:
        return winList[0]
    else:
        return winList[-1]


# Expect [0,2,2,0,1,0,0,0,0,0,0]
print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
# Expect [-1]
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
# Expect [1,1,2,0,1,2,2,0,0,0,0]
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
# Expect [1,1,1,1,1,1,1,1,0,0,2]
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))

"""
문제 풀이 및 접근 방법
    1. 10점부터 0점까지 차례로 화살을 쏠 것이다. 이를 위해 지금 몇점에 화살을 쏠건지를 나타내는 focus와 현재 화살 상황인 arrow를 덱에 넣어준다.
        focus : 0 (0번째=10점 과녁에 쏘겠다)
        arrow: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] (현재 화살 상황)

    2. 어피치를 이기려면 이 과녁에 어피치보다 1개 더 많이 쏘거나,
        이 과녁에는 아예 0발을 쏘고 화살을 아껴서 다른 과녁의 승률을 높여주는 두가지의 선택권이 있다.
        따라서 arrow를 복사한 리스트를 두개 만든 후,
        하나에는 어피치보다 1개 더 많이 쏘고 다른 하나에는 0발을 쏴서 덱에 넣어준다. 이렇게 focus번째 과녁에 화살을 쐈다.
        다음 while문에서는 다음 과녁을 봐야 하므로 focus는 +1해준다.

    3. 이렇게 쏘다 보면, 극단적으로 계속 어피치보다 1개 많이 쏘는 상황이 생길 수 있다.
        따라서 주어진 화살 개수보다 더 많이 쏘게 되는 경우를 컷해준다.
        마찬가지로, 극단적으로 계속 0발만 쏘는 상황이 생길 수 있다.
        따라서 focus=10이 되어 마지막 과녁을 쏠 차례까지 온 경우 남은 화살을 전부 마지막 과녁에 쏴준다.
        화살을 다 쐈으니 focus는 이제 필요 없으므로 아무 값이나 넣어준다.

    4. 화살을 다 쐈다면 점수를 계산한다. 라이언의 점수가 높다면, 어피치와의 점수차를 계산해서 최대점수차를 갱신한다.
        apeach : 어피치의 점수
        lion: 라이언의 점수
        maxGap: 어피치와 라이언의 최대점수차
        res: 최대점수차를 내는 화살상황들을 모아둔 리스트

    5. 리턴값 res가 winList로 들어온다. 따라서 winList가 최대점수차를 내는 화살상황들을 모아둔 리스트가 된다.
        - winList에 원소가 없다면 라이언이 이기는 경우가 없다는 것이므로 문제 조건에 따라 [-1] 리턴
        - winList에 원소가 한 개 존재한다면 최대점수차를 내는 화살상황이 하나뿐이라는 것이므로 해당 화살상황을 리턴
        - winList에 원소가 여러 개 존재한다면 최대점수차를 내는 화살상황이 여러개라는 것이므로, 가장 낮은 점수를 더 많이 맞힌 경우를 리턴해야 한다.
            우리는 focus를 도입해 높은 점수부터 화살을 쏘도록 문제를 풀었으므로, 보다 낮은 점수를 맞힌
             경우가 나중에 append되었음을 알 수 있다.
            ⇒ 가장 낮은 점수를 맞힌 경우는 winList의 마지막 원소가 된다. 따라서 winList[-1] 리턴
"""
