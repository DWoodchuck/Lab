import pytest
from account import *
from pytest import *
class Test:
    def setup_method(self):
        self.p1 = Account('John')


    def teardown_method(self):
        del self.p1



    def test_init(self):
        assert self.p1.get_name() == 'John'
        assert self.p1.get_balance() == 0.0



    def test_deposit(self):
        assert self.p1.deposit(0) is False
        assert self.p1.get_balance() == pytest.approx(0.0)
        assert self.p1.deposit(-1) is False
        assert self.p1.get_balance() == pytest.approx(0.0)
        assert self.p1.deposit(1.1) is True
        assert self.p1.get_balance() == pytest.approx(1.1)


    def test_withdraw(self):
        assert self.p1.withdraw(0) is False
        assert self.p1.get_balance() == pytest.approx(0.0)
        assert self.p1.withdraw(-1) is False
        assert self.p1.get_balance() == pytest.approx(0.0)
        assert self.p1.withdraw(10) is False
        assert self.p1.get_balance() == pytest.approx(0.0)
        self.p1.deposit(1.1)
        assert self.p1.withdraw(1.0) is True
        assert self.p1.get_balance() == pytest.approx(.1)


