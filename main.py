import time
from web3 import Web3
from web3.middleware import geth_poa_middleware

low = 100


infura_url = "https://mainnet.infura.io/v3/885cab861b654087b7a6e900d415048f"
# infura_url = "https://rinkeby.infura.io/v3/885cab861b654087b7a6e900d415048f"

web3 = Web3(Web3.HTTPProvider(infura_url))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

test_address = Web3.toChecksumAddress("0xB3b7874F13387D44a3398D298B075B7A3505D8d4")

print("isConnected:", web3.isConnected())

# balance = web3.eth.getBalance(test_address)
# balance = web3.eth.get_balance(test_address)
# print("balance", web3.fromWei(balance, "ether"))

latest_block = web3.eth.get_block('latest')

print(latest_block['baseFeePerGas']/10**9)

# for count, transaction_hex in enumerate(latest_block['transactions']):
#     print()
#     print(f"transaction num {count}: {transaction_hex}")

for i in range(10):
    transaction = web3.eth.get_transaction_by_block('latest', i)
    print("\n", transaction)

# while True:
#    gas_price = web3.eth.gas_price
#    print(f"Gas price in gwei: {round(gas_price/1000000000, 2)}")
#    time.sleep(10)

# transaction = web3.eth.get_transaction("0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060")
# or line in transaction:
    # print(f"{line}: {transaction[line]}")