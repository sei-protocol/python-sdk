from sei_python_sdk.client.lcd import LCDClient, PaginationOptions
from sei_python_sdk.core import Coins

sei = LCDClient(
    url="http://54.183.99.245:1317",
    chain_id="sei-devnet-1",
)


# Basic account info
def test_account_info():
    # base_account
    result = sei.auth.account_info("sei1fegapd4jc3ejqeg0eu3jk4hvr74hg660nkejzv")

    assert result.address == "sei1fegapd4jc3ejqeg0eu3jk4hvr74hg660nkejzv"
    assert result.account_number == 551
