import json
import time
import requests
import pprint
from web3 import Web3
from web3.middleware import geth_poa_middleware

low = 100
high = 200


infura_url = "https://mainnet.infura.io/v3/885cab861b654087b7a6e900d415048f"
# infura_url = "https://rinkeby.infura.io/v3/885cab861b654087b7a6e900d415048f"

web3 = Web3(Web3.HTTPProvider(infura_url))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

open_sea = '0x7Be8076f4EA4A4AD08075C2508e481d6C946D12b'
open_sea_wallet = '0x5b3256965e7C3cF26E11FCAf296DfC8807C01073'
account = ''
tx = web3.eth.get_transaction('0x0cac3eef53ad85432d1c3cc4f417eb3b7362953fc891e756f1c8951053fc09aa')

print("isConnected:", web3.isConnected())

abi_endpoint = f"https://api.etherscan.io/api?module=contract&action=getabi&address={tx['to']}&apikey=EUFCYXX79P69VWPNM7REYGWRYYZ66H2G2J"
abi = json.loads(requests.get(abi_endpoint).text)

contract = web3.eth.contract(address=tx["to"], abi=abi["result"])
func_obj, func_params = contract.decode_function_input(tx["input"])

pprint.pprint(func_params)

# balance = web3.eth.getBalance(test_address)
# balance = web3.eth.get_balance(test_address)
# print("balance", web3.fromWei(balance, "ether"))

# latest_block = web3.eth.get_block('latest')
#
# for count, transaction_hex in enumerate(latest_block['transactions']):
#     print()
#     print(f"transaction num {count}: {transaction_hex}")

# block_count = web3.eth.block_number-1
# transaction_count = web3.eth.get_block_transaction_count(block_count)
# print(transaction_count)
# for i in range(transaction_count):
#     transaction = web3.eth.get_transaction_by_block(block_count, i)
#     if transaction['to'] == open_sea or transaction['to'] == open_sea_wallet:
#         print(f"\n {i} https://etherscan.io/tx/{transaction['hash'].hex()}")
#         print(transaction)
# print(transaction_count)


# def get_gas_price(low, high):
#     while True:
#         gas_price = round(web3.eth.gas_price/1000000000, 2)
#         if gas_price < low:
#             return f"Gas is low. lowest gas for transaction from latest block: {gas_price} Gwei"
#         if gas_price > high:
#             return f"Gas is high. lowest gas for transaction from latest block: {gas_price} Gwei"
#         else:
#             return f"Gas is medium. lowest gas for transaction from latest block: {gas_price} Gwei"
#         time.sleep(10)
#
#
# print(get_gas_price(low, high))


# transaction = web3.eth.get_transaction("0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060")
# or line in transaction:
# print(f"{line}: {transaction[line]}")
