'''
풀이 및 접근방법
  1. 목표 알고력, 코딩력을 각각 변수에 세팅한다.
  2. dp에 목표 알고력과 목표 코딩력 만큼의 길이를 가진 이중배열을 무한대 원소로 세팅한다.
  3. dp에 현재 알고력과 코딩력의 위치값에 0을 세팅한다.
  4. 이중배열을 순회하며 다음을 수행한다.
  5. dq의 각 위치값에 그 위치값과 이전 위치값에서 1을 더한 것 중 최소를 세팅한다.
  6. 문제를 순회하며, 풀 수 있는 문제인 경우엔 다음을 수행한다.
  7. 문제를 풀었을때의 보상 알고력과 코딩력을 목표값과 비교해 최소값을 구한다.
  8. 최소값의 좌표에 그 위치값과 이전 위치값에서 코스트를 더한 값 중 최소값을 구해 세팅한다.
  9. dp의 마지막 원소를 리턴한다. 
'''

def solution(alp, cop, problems):
    max_alp_req, max_cop_req = [0, 0]  # 목표값
    
    for problem in problems:
        max_alp_req = max(max_alp_req, problem[0])
        max_cop_req = max(max_cop_req, problem[1])
    
    dp = [[float('inf')] * (max_cop_req+1) for _ in range(max_alp_req+1)]
    
    alp = min(alp, max_alp_req)  # 둘중 하나라도 목표값을 넘어가면 안된다.
    cop = min(cop, max_cop_req)
    
    dp[alp][cop] = 0  # dp[i][j]의 의미 : 알고력 i, 코딩력 j을 도달 할 수 있는 최단시간
    
    for i in range(alp, max_alp_req+1):
        for j in range(cop, max_cop_req+1):
            if i < max_alp_req:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j < max_cop_req:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    new_alp = min(i+alp_rwd, max_alp_req)  # 둘중 하나라도 목표값을 넘어가면 안된다.
                    new_cop = min(j+cop_rwd, max_cop_req)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)
                    
    return dp[max_alp_req][max_cop_req]