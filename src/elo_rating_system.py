'''
ELO算法
'''
from random import random

from src.inti_seting import con_db
from src.peopless import item_girls


class ELO:
    @staticmethod
    def E(a_score, b_score):
        # 计算选手的得分期望值
        P = (b_score - a_score) / 400
        a_e = 1 / (1 + 100 ** P)
        b_e = 1 / (1 + 100 ** (-P))
        return a_e, b_e

    @staticmethod
    def elo(contestants, add_score):
        # 根据选手的期望得分对得分进行调整
        '''
            R’=R+K(S-E)
            S:在一场比赛中的实际得分（默认胜1负0,平局0.5），此处排除平均情况
            E:对于一场比赛的期望得分
            R:在比赛前的已有分值（起始值置1400）
            R':重新计算的分值
            K:根据分值截断可做调整
        '''
        K = 16
        EA, EB = ELO.E(contestants[0].score, contestants[1].score)
        contestants[0].score = contestants[0].score + K * (add_score[0] - EA)
        contestants[1].score = contestants[1].score + K * (add_score[1] - EB)



# 选取选手，和匹配选手
class competition:
    def __init__(self):
        con_db.getcon()
        self.contestants = {}
        self.contestants[0] = self.get_contestant()
        self.contestants[1] = self.match_opponent()
        con_db.close()

    def get_contestant(self):
        sql = 'select * from girls order by comNum  asc '
        return item_girls(con_db.get_all(sql)[0])

    def match_opponent(self):
        while True:
            symbol,flag=('>',-1) if random() > 0.5 else ('<',0)
            sql = 'select * from girls where score{}={} and id!={} order by score desc'. \
                format(symbol, self.contestants[0].score, self.contestants[0].id)
            lis = con_db.get_all(sql)
            if lis.__len__() == 0:
                continue  # 没取到一个对手
            else:
                '''
                已得到一个对手，结束循环
                在降序排序情况下，大于要选择最后一项，小于要选择第一项
                '''
                peo = lis[flag]
                break
        return item_girls(peo)

    def update_db(self):
        con_db.getcon()
        for i in self.contestants.values():
            sql = 'update girls SET score = {},comNum={} WHERE id = {}'.format(i.score, i.comNum + 1, i.id)
            con_db.edit(sql)
        con_db.close()

