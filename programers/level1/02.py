"""
LEVEL01
https://school.programmers.co.kr/learn/courses/30/lessons/250137

[5, 1, 5]	30	[[2, 10], [9, 15], [10, 5], [11, 5]]	5
[3, 2, 7]	20	[[1, 15], [5, 16], [8, 6]]	-1
[4, 2, 7]	20	[[1, 15], [5, 16], [8, 6]]	-1
[1, 1, 1]	5	[[1, 2], [3, 2]]	3
"""


def attack(health, damage):
    return health - damage


def heal(health, heal_time, heal_amount, extra_heal_amount, max_health, max_heal_time):
    heal_time -= 1
    health += heal_amount
    if heal_time <= 0:
        health += extra_heal_amount
        heal_time = max_heal_time
    if health >= max_health:
        return max_health, heal_time
    return health, heal_time


def solution(bandage, health, attacks):
    max_health = health
    max_heal_time = bandage[0]
    heal_time, heal_amount, extra_heal_amount = bandage
    max_time = attacks[-1][0]
    attack_dict = {}
    for k, v in attacks:
        attack_dict[k] = v

    for i in range(1, max_time + 1):
        print(i, health, heal_time, attack_dict.get(i))
        if attack_dict.get(i) is not None:
            health = attack(health=health, damage=attack_dict[i])
            heal_time = bandage[0]
            if health <= 0:
                return -1
            continue
        else:
            health, heal_time = heal(
                health,
                heal_time,
                heal_amount,
                extra_heal_amount,
                max_health,
                max_heal_time,
            )

    return health


if __name__ == "__main__":
    print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))
