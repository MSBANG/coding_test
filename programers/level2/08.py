"""
LEVEL 02
https://school.programmers.co.kr/learn/courses/30/lessons/388353

["AZWQY", "CAABX", "BBDDA", "ACACA"]	["A", "BB", "A"]	11

AZWQY
CAABX
BBDDA
ACACA
"""


def move_stuff(loc, garage):
    if not loc or not garage:
        return

    if (loc[0] == 0 or loc[0] == len(garage[0])) or (
        loc[1] == 0 or loc[1] == len(garage)
    ):
        print("loc: ", loc)
        print("loc0 loc1:", loc[0], loc[1])
        garage[loc[0]][loc[1]] = None
        return

    # 왼
    left = garage[loc[0]][loc[1] - 1]
    print("left", left)
    right = garage[loc[0]][loc[1] + 1]
    print("right", right)
    up = garage[loc[0] + 1][loc[1]]
    print("up", up)
    down = garage[loc[0] - 1][loc[1]]
    print("down", down, loc[0] - 1, loc[1])

    if not left:
        return move_stuff([[loc[0]], [loc[1] - 1]], garage)

    # 오
    elif not right:
        return move_stuff([[loc[0]], [loc[1] + 1]], garage)

    # 위
    elif not up:
        return move_stuff([[loc[0] + 1], [loc[1]]], garage)

    # 아
    elif not down:
        return move_stuff([[loc[0] - 1], [loc[1]]], garage)

    else:
        return


def solution(storage, requests):
    storage.reverse()
    garage = [list(a) for a in storage]

    for request in requests:
        if len(request) == 1:
            for y in range(0, len(garage)):
                for x in range(0, len(garage[y])):
                    if garage[y][x] == request:
                        move_stuff([y, x], garage)
        else:
            # 크레인
            for y in range(0, len(garage)):
                for x in range(0, len(garage[y])):
                    if garage[y][x] == request[0]:
                        garage[y][x] = None
    answer = 0
    for g in garage:
        for x in g:
            if x is not None:
                answer += 0

    return answer


if __name__ == "__main__":
    solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"])
