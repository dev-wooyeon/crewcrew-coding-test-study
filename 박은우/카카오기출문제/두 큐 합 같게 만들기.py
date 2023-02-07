from collections import deque


# 테스트11과 테스트28에서 시간초과가 뜬다.
# 두큐의 합이 1밖에 차이가 나지 않은 경우 탈출 조건식을 맞추기 못하기 때문에 시간 초과가 걸림
# for 문을 이용해서 range를 정해주거나, while문에 종료조건을 포함해주는 방법으로 해결
# def solution(queue1, queue2):
#     q1, q2 = deque(queue1), deque(queue2)
#     q1_sum, q2_sum = sum(q1), sum(q2)
#     cnt = 0
#     while q1 and q2: # 큐가 빌 때 까지
#         if q1_sum == q2_sum:
#             return cnt
#         elif q1_sum > q2_sum:
#             num = q1.popleft()
#             q2.append(num)
#             q1_sum -= num
#             q2_sum += num
#             cnt+= 1
#         else: # q2_sum이 q1_sum보다 클 때
#             num = q2.popleft()
#             q1.append(num)
#             q2_sum -= num
#             q1_sum += num
#             cnt+= 1
#     return -1 # 값이 같아지지 않으면 -1을 반환

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    q1_sum, q2_sum = sum(q1), sum(q2)
    for i in range(300000):
        if q1_sum == q2_sum:
            return i
        elif q1_sum > q2_sum:
            num = q1.popleft()
            q2.append(num)
            q1_sum -= num
            q2_sum += num
        else:  # q2_sum이 q1_sum보다 클 때
            num = q2.popleft()
            q1.append(num)
            q2_sum -= num
            q1_sum += num
    return -1  # 값이 같아지지 않으면 -1을 반환


# Expect 2
print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
# Expect 7
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
# Expect -1
print(solution([1, 1], [1, 5]))

"""
문제 유형 : Greedy, Queue
Greedy : 어떠한 규칙을 정해, 해당 규칙대로 진행하다보면 답이 나오게 되는 그리디 유형의 문제이다.
Queue : FIFO (선입선출) 특징을 가지는 큐에 대한 개념이 있어야 구현할 수 있다.

풀이 방식 :
1. 제목부터 두 큐 합 같게 만들기여서 from collections import deque로 deque라이브러리를 import 해줬다.
2. q1, q2 = deque(queue1), deque(queue2)로 큐 생성
3. q1_sum, q2_sum = sum(q1), sum(q2)로 q1, q2의 합을 각각 만들어준다.
4. q1_sum이 q2_sum보다 크면 q1에서 가장 첫번째 원소를 pop해서 빼준 다음, q2에 append해준다. 또한 q2_sum에 그 값을 더해준다.
5. 이렇게 연산이 발생할 때 마다 개수를 더해주고 결과값을 return한다.
"""
