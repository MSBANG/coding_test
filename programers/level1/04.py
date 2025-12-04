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
