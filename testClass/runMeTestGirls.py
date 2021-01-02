# @File    : runMeTestGirls.py

# @File    : testELo.py
import unittest


from src.peopless import class_girls


class EloTestCase(unittest.TestCase):
    def test_ElO_E(self):
        result= class_girls(id_=1001, pothopath_=" ", score_=1400, comNum_=0).get()
        self.assertEqual(result, (1001, 1400, 0))

if __name__ == '__main__':
    unittest.main()