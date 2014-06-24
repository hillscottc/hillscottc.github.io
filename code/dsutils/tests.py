import unittest

import sample_data as sd
from traversals import bft, dft


class TestDsUtils(unittest.TestCase):

    def test_bft(self):
        res = bft(sd.ADJL_1, 'A')
        exp_res = ['A', 'B', 'C', 'D', 'E']
        self.assertEqual(res, exp_res)

        res = bft(sd.ADJL_2, 'A')
        exp_res = ['A', 'B', 'E', 'C', 'D']
        self.assertEqual(res, exp_res)

    def test_dft(self):
        res = dft(sd.ADJL_1, 'A')
        exp_res = ['A', 'B', 'D', 'C', 'E']
        self.assertEqual(res, exp_res)

        res = dft(sd.ADJL_2, 'A')
        exp_res = ['A', 'B', 'C', 'D', 'E']
        self.assertEqual(res, exp_res)

if __name__ == '__main__':
    unittest.main()
