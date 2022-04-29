from brownie import SimpleStorage, accounts

def test_deploy_simple_storage():
	
	# Arrange
	account = accounts[0]

	# Act
	simple_storage = SimpleStorage.deploy({"from": account})
	starting_value = simple_storage.retrieve()
	expected = 0

	# Assert
	assert starting_value == expected


def main():
	test_deploy_simple_storage()


def test_update_simple_storage():
	
	# Arrange
	account = accounts[0]

	# Act
	simple_storage = SimpleStorage.deploy({"from":account})
	simple_storage.store(15, {"from":account})

	updated_value = simple_storage.retrieve() 
	expected = 15
	
	# Assert
	assert updated_value == expected

