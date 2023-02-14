'''
풀이 및 접근방법
  1. 두 큐의 총합의 2를 나눈 값을 세팅한다. 이 때, 나눈 값이 정수가 아닌 경우 -1을 리턴한다.
  2. 각 큐의 합들을 sum1, sum2에 세팅한다.
  3. queue1의 길이의 3배만큼 다음을 순회한다.
  4. 만약 sum1이 sum2보다 크면, 첫번째 큐에서 원소를 빼서 두번째 큐에 추가한다.
  5. 반대라면, 두번째 큐에서 원소를 빼서 첫번째 큐에 추가한다.
  6. 만약 두 큐의 합이 같다면, 실행횟수를 리턴한다.
'''

from collections import deque

def solution(queue1, queue2):
    answer = -1
    result = (sum(queue1 + queue2)) / 2
    if int(result) != result:
      return -1
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    sum1 = sum(list(dq1))
    sum2 = sum(list(dq2))
    tryN = 0
    while tryN <= len(queue1) * 3:
      if sum1 > sum2:
        cur = dq1.popleft()
        dq2.append(cur)
        sum2 += cur
        sum1 -= cur
      elif sum1 < sum2:
        cur = dq2.popleft()
        dq1.append(cur)
        sum1 += cur
        sum2 -= cur
      else:
        answer = tryN
        break
      tryN += 1
    if sum1 == result:
      return answer
    else:
      return -1