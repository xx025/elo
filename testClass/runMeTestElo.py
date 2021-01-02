# @File    : testELo.py
import unittest

from src.elo_rating_system import ELO
from src.peopless import class_girls


class EloTestCase(unittest.TestCase):
    def test_ElO_E(self):
        result = ELO.E(1400, 1400)
        self.assertEqual(result, (0.5, 0.5))

    def test_ElO_elo(self):
        girls1 = class_girls(id_=1001, pothopath_=" ", score_=1400, comNum_=0)
        girls2 = class_girls(id_=1002, pothopath_=" ", score_=1400, comNum_=0)
        con = [girls1, girls2]
        add_score = (0.5, 0.5)
        ELO.elo(con=con, add_score=add_score)
        result = (con[0].score, con[1].score)
        self.assertEqual(result, (1400, 1400))


if __name__ == '__main__':
    unittest.main()
