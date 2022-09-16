# import asynctest
# from aioresponses import aioresponses

# from sei_python_sdk.client.lcd import AsyncLCDClient, LCDClient

# """
# class TestDoSessionGet(asynctest.TestCase):
#     @aioresponses()
#     def test_makes_request_to_expected_url(self, mocked):
#         mocked.get(
#             "http://54.183.99.245:1317/cosmos/base/tendermint/v1beta1/node_info",
#             status=200,
#             body='{"response": "test"}',
#         )
#         sei = LCDClient(chain_id="sei-devnet-1", url="http://54.183.99.245:1317")

#         resp = sei.tendermint.node_info()
#         assert resp == {"response": "test"}
#         sei.session.close()

#     @aioresponses()
#     async def test_makes_request_to_expected_url_async(self, mocked):
#         mocked.get(
#             "http://54.183.99.245:1317/cosmos/base/tendermint/v1beta1/node_info",
#             status=200,
#             body='{"response": "test"}',
#         )
#         sei = AsyncLCDClient(chain_id="sei-devnet-1", url="http://54.183.99.245:1317")

#         resp = await sei.tendermint.node_info()
#         print(resp)
#         assert resp == {"response": "test"}
#         sei.session.close()


# if __name__ == "__main__":
#     asynctest.main()
# """
