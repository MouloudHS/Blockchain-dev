from brownie import SimpleStorage, accounts, config

def read_contract():
	
	# Get the "first" deployed contract.
	simple_storage = SimpleStorage[0]

	# Brownie automatically knows what the ABI is 
	# and what the address of the contract is 
	# => We can directly call the functions that 
	# we need from the contract now.

	print(simple_storage.retrieve())

def main():
	read_contract()