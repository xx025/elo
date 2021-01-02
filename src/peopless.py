
class class_girls:
    def __init__(self, id_, pothopath_, score_, comNum_):
        self.id = id_
        self.pothopath = pothopath_
        self.score = score_
        self.comNum = comNum_
    def get(self):
        return self.id,self.score,self.comNum


def item_girls(peo):
    # 将数据库返回的元组封装为people类型
    return class_girls(id_=peo[0], pothopath_=peo[1], score_=peo[2], comNum_=peo[3])


