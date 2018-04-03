import unittest
import AplusB


class testAplusB(unittest.TestCase):
    def test1_123p456(self):
        """
        AplusB函数测试
        """
        self.assertEqual(579, AplusB.aplusb(123, 456))

    def test2_5299p8456(self):
        """
        AplusB函数测试
        """
        self.assertEqual(13755, AplusB.aplusb(5299, 8456))


if __name__ == "__main__":
    unittest.main(verbosity=2)
