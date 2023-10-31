from unittest import TestCase
from main import checkWin


class Test(TestCase):
    def test_check_win1(self):
        self.assertEqual(
            checkWin(
                [1, 1, 1,
                 0, 0, 0,
                 0, 0, 0],
                [0, 0, 0,
                 1, 1, 0,
                 0, 0, 0],
            ), 1
        )

    def test_check_win2(self):
        self.assertEqual(
            checkWin(
                [1, 1, 0,
                 0, 0, 0,
                 0, 0, 1],
                [0, 0, 0,
                 1, 1, 1,
                 0, 0, 0],
            ), 0
        )

    def test_check_exception(self):
        self.assertRaises(
                Exception,
                checkWin,
                [
                    1, 0, 0,
                    1, 0, 0,
                    1, 0, 0
                ],
                [0, 0, 1,
                 0, 0, 1,
                 0, 0, 1]
        )

    def test_check_exception2(self):
        self.assertRaises(
                Exception,
                checkWin,
                [
                    1, 0, 0,
                    1, 0, 0,
                    1, 0, 0
                ],
                [1, 0, 0,
                 1, 0, 0,
                 1, 0, 0]
        )

