"""
LEVEL 01
https://school.programmers.co.kr/learn/courses/30/lessons/12981
    1:1      2:1      3:1     1:2       2:2     3:2     1:3        2:3      3:3
3	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	[3,3]

"""

from math import ceil


def failed(words):
    for i in range(len(words)):
        if i == 0:
            continue
        if words[i][0] != words[i - 1][-1]:
            return i + 1
        elif words[i] in words[:i]:
            return i + 1
        continue


def solution(n, words):
    failed_index = failed(words)
    if not failed_index:
        return [0, 0]

    sequence = ceil(failed_index / n)
    failed_man = failed_index % n
    return [failed_man if failed_man else n, sequence]
