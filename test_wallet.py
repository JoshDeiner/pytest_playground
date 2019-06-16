''' test_wallet playing  '''
import pytest
from wallet import Wallet as ww


def test_default_initial_amount():
    ''' set initial wallet value  '''
    wallet = ww()
    assert wallet.balance == 0
    wallet.close()


def test_setting_initial_amount():
    ''' test wallet with value > 0  '''
    wallet = ww(initial_amount=100)
    assert wallet.balance == 100
    wallet.close()


def test_wallet_add_cash():
    ''' test if can add cash  '''
    wallet = ww(initial_amount=10)
    wallet.add_cash(amount=90)
    assert wallet.balance == 100
    wallet.close()


def test_wallet_spend_cash():
    ''' test spending func  '''
    wallet = ww(initial_amount=20)
    wallet.spend_cash(amount=10)
    assert wallet.balance == 10
    wallet.close()
