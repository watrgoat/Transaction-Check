import json
import time
import requests
import pprint
from web3 import Web3
from web3.middleware import geth_poa_middleware

low = 100
high = 200
response = requests.get('http://api.zapper.fi/v1/gas-price', 'api_key=96e0cc51-a62e-42ca-acee-910ea7d2a241')
print(response.text)

infura_url = "https://mainnet.infura.io/v3/885cab861b654087b7a6e900d415048f"
# infura_url = "https://rinkeby.infura.io/v3/885cab861b654087b7a6e900d415048f"

web3 = Web3(Web3.HTTPProvider(infura_url))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

open_sea = '0x7Be8076f4EA4A4AD08075C2508e481d6C946D12b'
open_sea_wallet = '0x5b3256965e7C3cF26E11FCAf296DfC8807C01073'
account = '0xeEb23003fdeB02c29995e861b1d31CeB7b277E78'
tx = web3.eth.get_transaction('0xaba29bdbe481df4a4f98edac2d493469bcd20cc6c956bfc98b79da538c1849a7')

print("isConnected:", web3.isConnected())

abi_endpoint = f"https://api.etherscan.io/api?module=contract&action=getabi&address={tx['to']}&apikey=EUFCYXX79P69VWPNM7REYGWRYYZ66H2G2J"
abi = json.loads(requests.get(abi_endpoint).text)

contract = web3.eth.contract(address=tx["to"], abi=abi["result"])
func_obj, func_params = contract.decode_function_input(tx["input"])


print(input)
print(dir(func_obj))
print(func_obj.fn_name)
print(func_obj)


block_count = 13122155
block = web3.eth.get_block(block_count)
transaction_count = web3.eth.get_block_transaction_count(block_count)
for trx in block['transactions']:
    transaction = web3.eth.get_transaction(trx.hex())
    if transaction['to'] == account or transaction['from'] == account:
        print(transaction)
        print('This wallet bought or sold something')
print(transaction_count)