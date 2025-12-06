"""
Level 02
https://school.programmers.co.kr/learn/courses/30/lessons/389479

[0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5]	3	5	7
"""

from math import ceil


def add_server(current_time, borrowed_server_dict: dict, server_needs, k, server_sum):
    current_server = sum(list(borrowed_server_dict.values()))
    if not current_server:
        borrowed_server_dict[current_time + k] = server_needs
    else:
        server_needs = current_server - server_needs
        if server_needs > 0:
            borrowed_server_dict[current_time + k] = server_needs
    server_sum += server_needs
    return sum(list(borrowed_server_dict.values())), server_sum


def solution(players, m, k):
    server_sum = 0
    current_server = 0
    borrowed_server_dict = {}
    for i in range(len(players)):
        if borrowed_server_dict.get(i):
            del borrowed_server_dict[i]
            current_server = len(list(borrowed_server_dict.values()))
        if players[i] >= m and not current_server:
            server_needs = ceil(players[i] / m)
            current_server, server_sum = add_server(
                i, borrowed_server_dict, server_needs, k, server_sum
            )
        elif players[i] >= m and current_server:
            max_player = m * current_server
            server_needs = ceil(max_player / players[i])
            current_server, server_sum = add_server(
                i, borrowed_server_dict, server_needs, k, server_sum
            )
        print(i + 1, players[i], borrowed_server_dict)

    return server_sum


if __name__ == "__main__":
    print(
        solution(
            [
                0,
                0,
                0,
                10,
                0,
                12,
                0,
                15,
                0,
                1,
                0,
                1,
                0,
                0,
                0,
                5,
                0,
                0,
                11,
                0,
                8,
                0,
                0,
                0,
            ],
            5,
            1,
        )
    )
