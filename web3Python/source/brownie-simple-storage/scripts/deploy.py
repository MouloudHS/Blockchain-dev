# import accounts module
from brownie import accounts, SimpleStorage, network, config

def get_account():

	if (network.show_active() == "development"):
		print("development network ON !")
		return accounts[0]

	else:
		print("This is a TestNet !")
		return accounts.add(config["wallets"]["from_key"])


# Deploy
def deploy_simple_storage():
	account = get_account()
	simple_storage = SimpleStorage.deploy({"from":account})
	stored_value = simple_storage.retrieve()
	print("Retrieve function call: value = ", stored_value)

	transaction = simple_storage.store(15, {"from":account})
	transaction.wait(1)
	stored_value_update = simple_storage.retrieve()
	print("Retrieve function call: value = ", stored_value_update)

# The function to be executed 
def main():
	deploy_simple_storage()
