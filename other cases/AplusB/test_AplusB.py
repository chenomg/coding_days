import pytest
from AplusB.AplusB import Solution


class Test_AplusB:
    Testsolution = Solution()

    def test_123p456(self):
        """
        AplusB函数测试
        """
        assert 579 == self.Testsolution.aplusb(123, 456)

    def test_5299p8456(self):
        """
        AplusB函数测试
        """
        assert 13755 == self.Testsolution.aplusb(5299, 8456)

    def test_0p123(self):
        """
        AplusB函数测试
        """
        assert 123 == self.Testsolution.aplusb(0, 123)

    def test_10pn123(self):
        """
        AplusB函数测试
        10 + (-123) = -113
        """
        assert -113 == self.Testsolution.aplusb(10, -123)

    def test_100pn100(self):
        """
        AplusB函数测试
        100 + (-100) = 0
        """
        assert 0 == self.Testsolution.aplusb(100, -100)
