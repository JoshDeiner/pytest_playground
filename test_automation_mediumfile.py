''' more pytest automation  '''
import pytest


class CheckClass:
    def one_check(self):
        x = "this"
        assert "h" in x

    def two_check(self):
        x = "hello"
        assert hasattr(x, 'check')
