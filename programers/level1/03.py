"""
LEVEL01
https://school.programmers.co.kr/learn/courses/30/lessons/42627

이때, 작업의 소요시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것 순으로 우선순위가 높습니다

요청시점, 소요시간              평균 소요시간 (종료시점 - 요청시점) / len(jobs)
[[0, 3], [1, 9], [3, 5]]	8
"""

import sys

sys.setrecursionlimit(10**6)


def solution(jobs: list):
    _jobs = []
    for index, job in enumerate(jobs):
        _jobs.append([index, job[0], job[1]])

    # 요청시점으로 정렬
    # 최초 인덱스, 요청시점, 소요시간
    _jobs.sort(key=lambda x: x[1])
    time = _jobs[0][1]
    res_list = []
    while True:
        executable_list = [x for x in _jobs if x[1] <= time]
        try:
            execute_target = min(executable_list, key=lambda x: (x[2], x[1], x[0]))
        except:
            time = _jobs[0][1]
            continue

        time += execute_target[2]
        res_list.append(time - execute_target[1])
        _jobs.remove(execute_target)
        if len(res_list) == len(jobs):
            break
    answer = sum(res_list) / len(res_list)
    return int(answer)


if __name__ == "__main__":
    print(solution([[7, 8], [3, 5], [9, 6]]))
