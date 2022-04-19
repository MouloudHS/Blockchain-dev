import solcx, os
solcx.install_solc('0.6.0')

from solcx import compile_standard
import json
from web3 import Web3

from dotenv import load_dotenv
load_dotenv()

# Open the solidity file and store 
# its content as a variable
with open("./SimpleStorage.sol", "r") as f:
	simple_storage_file = f.read()

# save the compiled solidity code to a variable
input_data = {"language":"Solidity", 
			  "sources":{"SimpleStorage.sol": {"content":simple_storage_file}}, 
			  "settings":{

			  "outputSelection": {"*": { "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"] } }
						 }
			 }
compiled_sol = compile_standard(input_data, solc_version = "0.6.0")

with open("compiled_code.json", "w") as file:
	json.dump(compiled_sol, file)

# Get the bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]  

# Get the abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# RPC Server and chain Id and Address
HTTP_PROVIDER = os.getenv("HTTP_PROVIDER_INFURA")
w3 = Web3(Web3.HTTPProvider(HTTP_PROVIDER))
chainId = int(os.getenv("RINKEBY_CHAIN_ID"))
my_address = os.getenv("PUBLIC_KEY_RINKEBY_METAMASK")
private_key = os.getenv("PRIVATE_KEY_RINKEBY_METAMASK")

SimpleStorage = w3.eth.contract(abi=abi,bytecode=bytecode)

nonce = w3.eth.getTransactionCount(my_address)

# Create the transaction object
transaction_parameters = {"gasPrice": w3.eth.gas_price, "chainId":chainId, "from":my_address, "nonce":nonce}
transaction = SimpleStorage.constructor().buildTransaction(transaction_parameters)

# Sign the transaction
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key) 

print("Deploying the contract...")
# Send the signed transaction to the blockchain
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

# Waiting for block confirmations:
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print("Contract deployed...")
# define the compiled smart contract to strat interacting with it:
# we need the contract address and its abi
simple_storage = w3.eth.contract(tx_receipt.contractAddress, abi = abi)

print("\nA view function call (must return 0 in this case).... ")
# output the resukt of the retrieve() function of simple storage for example:
output_retrieve = simple_storage.functions.retrieve().call() # we use call as it is a view function
print("output of retrieve function: ", output_retrieve)


# Now let's store a value and try to retrieve it:
transaction_parameters = {"gasPrice": w3.eth.gas_price, "chainId":chainId, "from":my_address, "nonce":nonce+1}
# we use nonce + 1 bcs nonce has already been used
store_value = simple_storage.functions.store(15).buildTransaction(transaction_parameters)
signed_store_value = w3.eth.account.sign_transaction(store_value, private_key=private_key)

print("\nsending a transaction to store a value...")
store_value_hash = w3.eth.send_raw_transaction(signed_store_value.rawTransaction)
store_value_receipt = w3.eth.wait_for_transaction_receipt(store_value_hash)

print("Transaction sent: Success...")

print("\nA view function call (must return 15 in this case): ")
# output the resukt of the retrieve() function of simple storage for example:
output_retrieve = simple_storage.functions.retrieve().call() # we use call as it is a view function
print("output of retrieve function: ", output_retrieve)
print("\n\nSuccess 🏆 ... You can check on Rinkeby etherscan and your metamask wallet.... ")