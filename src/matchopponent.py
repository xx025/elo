# @File    : matchopponent.py

from random import random


def match(players):
    length = len(players)
    k = 0.1
    # 选手只与前后0.1的进行匹配
    r1 = random()

    player1 = players[round(length * r1)]
    # 随机选出一名选手
    # 再选一名
    player2=players[round(length * r1)]



    return player1, player2
