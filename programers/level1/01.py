"""
LEVEL01
https://school.programmers.co.kr/learn/courses/30/lessons/340199

wallet	bill	result
[30, 15]	[26, 17]	1
[50, 50]	[100, 241]	4
"""
#


def fold(wallet, bill, folded) -> int:
    folded += 1

    target, _else = (bill[0], bill[1]) if bill[0] > bill[1] else (bill[1], bill[0])
    target = int(target / 2)

    if target <= wallet[0] and _else <= wallet[1]:
        return folded
    if _else <= wallet[0] and target <= wallet[1]:
        return folded
    return fold(wallet, [target, _else], folded)


def solution(wallet, bill):
    folded = 0
    res = fold(wallet, bill, folded)
    return res


if __name__ == "__main__":
    print(solution([50, 50], [100, 241]))
