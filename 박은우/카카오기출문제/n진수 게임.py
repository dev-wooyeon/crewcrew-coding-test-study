# n진수로 변환하는 함수
def convert(number, n):
    if number == 0:
        return '0'
    NUMBERS = "0123456789ABCDEF"
    res = ""
    while number > 0:
        number, mod = divmod(number, n)
        res += NUMBERS[mod]
    return res[::-1]


def solution(n, t, m, p):
    answer = ''
    game = ''
    cur = p - 1
    for num in range(t * m):
        # print('num = {}'.format(num))
        game += convert(num, n)
    while 1:
        if len(answer) == t:
            break
        answer += game[cur]
        cur += m
    return answer


# Expect "0111"
print(solution(2, 4, 2, 1))
# Expect "02468ACE11111111"
print(solution(16, 16, 2, 1))
# Expect "13579BDF01234567"
print(solution(16, 16, 2, 2))
