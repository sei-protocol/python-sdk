import pytest
from sei_python_sdk.client.lcd import LCDClient
from sei_python_sdk.exceptions import LCDResponseError

sei = LCDClient(
    url="http://54.183.99.245:1317",
    chain_id="sei-devnet-1",
)


# Pinned codes
def test_pinned_codes():
    result = sei.wasm.pinned_codes()
    assert result["code_ids"] is not None


# Code info
def test_code_info():
    result = sei.wasm.code_info(2)

    assert result["code_id"] == 2
    assert result["creator"] == "sei1r86enlgz53n4lla8899jvcj04dpfsxzwgc8htz"
    assert (
        result["data_hash"] == "5AE319F688CC2E9966E32BFA0CC9CAE4344F493B094E1639D415A6636EC53275"
    )


def test_code_info_with_params():
    with pytest.raises(LCDResponseError):
        sei.wasm.code_info(72, {"height": 100})


# Contract info
def test_contract_info():
    result = sei.wasm.contract_info(
        "sei13ehuhysn5mqjeaheeuew2gjs785f6k7jm8vfsqg3jhtpkwppcmzql6ap03"
    )
    assert result is not None
    assert result["code_id"] == 7
    assert result["address"] == "sei13ehuhysn5mqjeaheeuew2gjs785f6k7jm8vfsqg3jhtpkwppcmzql6ap03"
    assert result["creator"] == "sei1yfnt79y82p5k5ue3u5q9p5w2sqy2zt6g8yy48h"
    assert result["label"] == "Sei USDC"


# def test_contract_query():
#     result = sei.wasm.contract_query(
#         "sei13ehuhysn5mqjeaheeuew2gjs785f6k7jm8vfsqg3jhtpkwppcmzql6ap03",
#         {"get_count": {}},
#     )
#     assert result is not None


# def test_contract_query_with_params():
#     result = sei.wasm.contract_query(
#         "sei13ehuhysn5mqjeaheeuew2gjs785f6k7jm8vfsqg3jhtpkwppcmzql6ap03",
#         {"get_total_supply": {}},
#         {"height": 61027},
#     )
#     assert result == {"count": 0}

#     result = sei.wasm.contract_query(
#         "sei19xa33fjdjlz9qkafrw8qnrzrawc8h0vhxvfdhh6yk3f5qxuh2fps9e49zt",
#         {"get_total_supply": {}},
#         {"height": 61028},
#     )
#     assert result == {"count": 1}
