'''
풀이 및 접근방법
  1. 문자열 l의 길이가 t * m보다 같거나 많아질때까지 n진수로 더해가며 세팅한다.
  2. m번째 순서의 숫자를 t개만큼 answer에 더해서 리턴한다.
'''

def jin(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return jin(q, base) + T[r]

def solution(n, t, m, p):
    max = t * m
    p = p - 1
    answer = ""
    l = ""
    i = 0
    while len(l) < max:
      l += str(jin(i, n))
      i += 1
    for idx, j in enumerate(l):
      if len(answer) >= t:
        break
      if idx%m == p:
        answer += j.upper()
    return answer