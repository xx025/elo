# ELO算法

def E(RA, RB):
    # 棋手的得分期望值
    P = (RB - RA) / 400
    EA = 1 / (1 + 100 ** P)
    EB = 1 / (1 + 100 ** (-P))
    return EA, EB


def elo(RA, RB, SA, SB):
    # 根据棋手的期望得分对得分进行调整
    '''
        R’=R+K(S-E)
        S:在一场比赛中的实际得分
        E:对于一场比赛的期望得分
        R:在比赛前的已有分值（起始值置1400）
        R':重新计算的分值
        K:根据分值截断可做调整
    '''
    K = 16
    EA, EB = E(RA, RB)
    RA_ = RA + K * (SA - EA)
    RB_ = RB + K * (SB - EB)
    return RA_, RB_
