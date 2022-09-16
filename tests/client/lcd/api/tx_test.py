from sei_python_sdk.client.lcd import LCDClient
from sei_python_sdk.client.lcd.params import PaginationOptions

sei = LCDClient(
    url="http://54.183.99.245:1317",
    chain_id="sei-devnet-1",
)

pagOpt = PaginationOptions(limit=2, count_total=True)


# Test txn info - this is a MsgDelegate tx
def test_tx_info():
    result = sei.tx.tx_info("AFF0D5F96DDC166AF36C047F48A723B2D7DE85367AD342F3A31FEB3585935F06")
    print("---------------------------")
    print("this is result txhash: ", result.txhash)
    assert result is not None
    assert result.txhash == "AFF0D5F96DDC166AF36C047F48A723B2D7DE85367AD342F3A31FEB3585935F06"


# Testing searching by block height and sender
def test_search():
    result = sei.tx.search(
        [
            ("tx.height", 7442303),
            ("message.sender", "sei16935dh0m43f3htk00wtrq0an2vetkrg020zkq2"),
        ]
    )

    assert len(result["txs"]) > 0
    assert (
        result["txs"][0].txhash
        == "AFF0D5F96DDC166AF36C047F48A723B2D7DE85367AD342F3A31FEB3585935F06"
    )


## TODO: update msgs so parsing can work correctly


# def test_tx_infos_by_height():
#     result = sei.tx.tx_infos_by_height()
#     assert result is not None


# def test_tx_infos_by_height_with_height():
#     result = sei.tx.tx_infos_by_height(1)
#     assert result is not None
