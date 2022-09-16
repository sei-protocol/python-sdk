import pytest

from sei_python_sdk.core import Coin, Coins


def test_clobbers_similar_denom():
    coins1 = Coins([Coin("ukrw", 1000), Coin("usei", 1000), Coin("usei", 1000)])

    coinKRW = coins1["ukrw"]
    coinLUNA = coins1["usei"]

    assert coinKRW.amount == 1000
    assert coinLUNA.amount == 2000


def test_converts_dec_coin():
    c1 = Coins(usei=1000, ukrw=1.234)
    c2 = Coins(usei=1000, ukrw=1234)

    assert all(c.is_dec_coin() for c in c1)
    assert not all(c.is_dec_coin() for c in c2)


def test_from_str():
    int_coins_string = "5ukrw,12usei"
    dec_coins_string = "2.3ukrw,1.45usei"
    neg_dec_coins_string = "-1.0ukrw,2.5usei"

    int_coins = Coins(ukrw=5, usei="12")
    dec_coins = Coins(
        ukrw=2.3,
        usei="1.45",
    )

    neg_dec_coins = Coins(
        ukrw="-1.0",
        usei=2.5,
    )

    assert Coins.from_str(int_coins_string) == int_coins
    assert Coins.from_str(dec_coins_string) == dec_coins
    assert Coins.from_str(neg_dec_coins_string) == neg_dec_coins
