'''
풀이 및 접근방법
  1. course와 orders를 기준으로 순회하며 다음을 수행한다.
  2. order의 원소들을 정렬한 다음, course의 원소만큼 조합을 구한다.
  3. 조합들이 나온 갯수를 counter에 저장한다.
  4. counter를 순회하며, 나온 갯수가 가장 많은 것을 answer에 추가한다.
  5. answer를 정렬한 후 리턴한다.
'''

from collections import deque, Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    for count in course:
      arr = []
      dq = deque(orders)
      while dq:
        cur = sorted(dq.popleft())
        arr2 = list(combinations(cur, count))
        arr += arr2
      counter = Counter(arr)
      if len(counter) == 0:
        continue
      maxC = max(counter.values())
      if maxC > 1:
        for i in counter:
          if counter[i] == maxC:
            answer.append("".join(i))
      arr2 = []
    
    return sorted(answer)