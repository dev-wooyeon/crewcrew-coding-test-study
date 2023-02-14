'''
풀이 및 접근방법
  1. 라이언이 화살을 쏘는 모든 경우의 수를 중복조합을 이용해 shot에 세팅한다.
  2. shot을 순회하며 다음을 수행한다.
  3. 쏘는 과녁을 shotList에 세팅한다.
  4. shotList와 info를 비교하며, 더 많이 쏜 쪽의 점수를 rion과 apeach에 더한다 (같은 경우는 apeach에 더하며, 둘 다 0인 경우 둘 다 더하지 않는다)
  5. rion과 apeach의 점수 차이값을 gap에 세팅하며, 차이값이 가장 큰 경우를 answer에 세팅해 리턴한다.
'''

from itertools import combinations_with_replacement
from collections import deque

def solution(n, info):
    answer = [-1]
    shot = list(combinations_with_replacement(range(11), n))
    dq = deque(shot)
    maxGap = 0
    while dq:
      cur = dq.popleft()
      rion = 0
      apeach = 0
      shotList = [0 for i in range(11)]
      for i in cur:
        shotList[10 - i] += 1
      for idx, i in enumerate(shotList):
        if i > info[idx]:
          if i > 0:
            rion += (10 - idx)
        else:
          if info[idx] > 0:
            apeach += (10 - idx)
      if rion > apeach:
        gap = rion - apeach
        if gap > maxGap:
          maxGap = gap
          answer = shotList
    return answer