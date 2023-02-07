from itertools import combinations


def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        new_menu = {}
        for menu in orders:
            menu_li = list(''.join(menu))
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))
                if res not in candidates:
                    candidates.append(res)
                else:
                    if res not in new_menu.keys():
                        new_menu[res] = 2
                    else:
                        new_menu[res] += 1
        sort_menu = sorted(new_menu.items(), key=lambda x: [len(x[0]), x[1]])
        if len(sort_menu):
            now = course[-1]
            maxi = sort_menu[-1][1]
        while sort_menu:
            menu, cnt = sort_menu.pop()
            if len(menu) == now and cnt >= maxi:
                answer.append(menu)
            elif len(menu) != now:
                now = len(menu)
                maxi = cnt
                answer.append(menu)
    return sorted(answer)


# Expect ["AC", "ACDE", "BCFG", "CDE"]
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
# Expect ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
# Expect ["WX", "XY"]
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))

"""
문제 풀이 및 접근 방법
step 1)
각 메뉴별로 가능한 모든 조합을 만든다.
조합을 만들기 위한 개수는 course에 담긴 숫자이므로 course 배열의 원소 순서대로 조합의 개수를 정한다.

step 2)
조합하려는 개수(k)를 선정하였다면 orders에 있는 원소들로 가능한 조합을 만든다.
ex) 'ABCFG', k = 2라면 나올 수 있는 조합은 'AB', 'BC', 'CF' ... 'FG' 가 있다.
이때 조합은 순서와 상관없으므로 'AC'와 'CA'는 같은 메뉴임을 주의한다. → 정렬을 통해 해결

step 3)
가능한 조합을 만들면서 해당 조합이 몇개가 등장하는지 개수를 카운트한다. → 딕셔너리 사용 {'메뉴조합': '갯수'}

step 4)
sorted, lambda를 이용해 딕셔너리를 정렬하고 가장 많이 나온 조합을 answer에 담는다.

step 5)
answer에 담긴 메뉴들을 사전순으로 정렬한다.
"""
