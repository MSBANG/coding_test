"""
LEVEL01
https://school.programmers.co.kr/learn/courses/30/lessons/12985

8	4	7	3
"""


def solution(n, a, b):
    round = 1
    while True:
        _list = [a, b]
        _list.sort()
        if _list[-1] % 2 == 0 and _list[-1] - _list[0] == 1:
            return round
        for i in range(len(_list)):
            if _list[i] % 2 == 0:
                _list[i] = int(_list[i] / 2)
            else:
                _list[i] = int(_list[i] / 2) + 1
        a, b = _list
        round += 1


#
