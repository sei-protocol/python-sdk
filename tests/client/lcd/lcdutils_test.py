from sei_python_sdk.client.lcd import LCDClient

sei = LCDClient(
    url="http://54.183.99.245:1317",
    chain_id="sei-devnet-1",
)


def test_validators_with_voting_power():
    validators_with_voting_power = sei.utils.validators_with_voting_power()
    print(validators_with_voting_power)
    assert validators_with_voting_power is not None
