
from web3 import Web3
from web3.auto.infura import w3




w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/<1rjIbbMJ7F40vTalf5UuN4qKeC3>'))
w3.eth.block_number