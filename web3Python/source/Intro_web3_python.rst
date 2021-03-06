Introduction to Web3.py
=======================

What is the python Web3.py package ?
------------------------------------

- Web3.py is a Python library for interacting with Ethereum.

- It’s commonly found in decentralized apps (dapps) to help with sending transactions, interacting with smart contracts, reading block data, and a variety of other use cases.

- The original API was derived from the Web3.js Javascript API, but has since evolved toward the needs and creature comforts of Python developers.

- In order to interact with a smart contract in python, we can use either Web3.py or Brownie. 

- In this tutorial, we are going to use web3.py.


First python script to deploy a smart contract
----------------------------------------------

- Let's create a python function to deploy a smart contract called **deploy.py**. 

- In order to compile a smart contract in python, we use the python package **py-solc-x**.

.. code-block:: python

	# deploy.py

	# install solidity compiler for version 0.6.0
	import solcx
	solcx.install_solc('0.6.0')

	# import the "compile" function from solcx
	from solcx import compile_standard

	# Open the solidity file and store 
	# its content as a variable
	with open("./SimpleStorage.sol", "r") as f:
		simple_storage_file = f.read()

	# Prepare for compiling solidity
	input_data = {
	"language":"Solidity",
	"sources":{"SimpleStorage.sol": {"content":simple_storage_file}}, 
	"settings":{ "outputSelection": {"*": { "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}}}
	}
	# compile and save the compiled solidity code to a variable
	compiled_sol = compile_standard(input_data, solc_version = "0.6.0")


- Now with this minimal ``deploy.py`` file, we actually opened the solidity file **"SimpleStorage.sol"**, and we compiled it but we didn't deploy it and we don't have anything returned after compilation.

- We can see that we passed some input data to the ``compile_standard`` function. In the note below we are going to explain each argument of the ``input_data`` which is a dictionnary.

.. note::

	- "language" is just the programming language that we are using in the opened file (In this case solidity).
	
	- "sources" is the dictionnary ``{"SimpleStorage.sol": {"content":simple_storage_file}`` with ``simple_storage_file`` being the variable used to store the solidity file.
	
	- settings is a dictionnary. The main key is ``outputSelection`` and it is a dictionnary with what we want to output in the form of a ``json`` file (In this case, we want to output, the metadata, the abi, the evm bytecode and the evm SourceMap) // outputSelection: ``{"*": { "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"] } }``

- Now we want to see the json file that we've created. Io order to achieve this, we will have to store compiled solidity in the format of a JSON file.


.. code-block:: python

	import solcx
	solcx.install_solc('0.6.0')

	from solcx import compile_standard
	import json

	# Open the solidity file and store 
	# its content as a variable
	with open("./SimpleStorage.sol", "r") as f:
		simple_storage_file = f.read()

	# save the compiled solidity code to a variable
	
	input_data = {
	"language":"Solidity",
	"sources":{"SimpleStorage.sol": {"content":simple_storage_file}}, 
	"settings":{ "outputSelection": {"*": { "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}}}
	}

	compiled_sol = compile_standard(input_data, solc_version = "0.6.0")

	with open("compiled_code.json", "w") as file:
		json.dump(compiled_sol, file)


- What we get as output is a JSON file, this JSON file contain the ABI, the metadata and other important stuff for deployement purposes. The ABI as we can see contain all the informations about the inputs and what are they supposed to output. 

.. code-block:: json 

	{
	    "contracts":
	    {
	        "SimpleStorage.sol":
	        {
	            "SimpleStorage":
	            {
	                "abi":
	                [
	                    {
	                        "inputs":
	                        [
	                            {
	                                "internalType": "string",
	                                "name": "_name",
	                                "type": "string"
	                            },
	                            {
	                                "internalType": "uint256",
	                                "name": "_age",
	                                "type": "uint256"
	                            }
	                        ],
	                        "name": "addPerson",
	                        "outputs":
	                        [],
	                        "stateMutability": "nonpayable",
	                        "type": "function"
	                    },
	                    {
	                        "inputs":
	                        [
	                            {
	                                "internalType": "string",
	                                "name": "",
	                                "type": "string"
	                            }
	                        ],
	                        "name": "nameToAge",
	                        "outputs":
	                        [
	                            {
	                                "internalType": "uint256",
	                                "name": "",
	                                "type": "uint256"
	                            }
	                        ],
	                        "stateMutability": "view",
	                        "type": "function"
	                    },
	                    {
	                        "inputs":
	                        [
	                            {
	                                "internalType": "uint256",
	                                "name": "",
	                                "type": "uint256"
	                            }
	                        ],
	                        "name": "people",
	                        "outputs":
	                        [
	                            {
	                                "internalType": "string",
	                                "name": "name",
	                                "type": "string"
	                            },
	                            {
	                                "internalType": "uint256",
	                                "name": "age",
	                                "type": "uint256"
	                            }
	                        ],
	                        "stateMutability": "view",
	                        "type": "function"
	                    },
	                    {
	                        "inputs":
	                        [],
	                        "name": "retrieve",
	                        "outputs":
	                        [
	                            {
	                                "internalType": "uint256",
	                                "name": "",
	                                "type": "uint256"
	                            }
	                        ],
	                        "stateMutability": "view",
	                        "type": "function"
	                    },
	                    {
	                        "inputs":
	                        [
	                            {
	                                "internalType": "uint256",
	                                "name": "_number",
	                                "type": "uint256"
	                            }
	                        ],
	                        "name": "store",
	                        "outputs":
	                        [],
	                        "stateMutability": "nonpayable",
	                        "type": "function"
	                    }
	                ],
	                "evm":
	                {
	                    "bytecode":
	                    {
	                        "linkReferences":
	                        {},
	                        "object": "608060405234801561001057600080fd5b506105aa806100206000396000f3fe608060405234801561001057600080fd5b50600436106100575760003560e01c80632e64cec11461005c5780636057361d1461007a5780636f760f41146100a857806390c3ee4d1461016d5780639e7a13ad1461023c575b600080fd5b6100646102ea565b6040518082815260200191505060405180910390f35b6100a66004803603602081101561009057600080fd5b81019080803590602001909291905050506102f3565b005b61016b600480360360408110156100be57600080fd5b81019080803590602001906401000000008111156100db57600080fd5b8201836020820111156100ed57600080fd5b8035906020019184600183028401116401000000008311171561010f57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290803590602001909291905050506102fd565b005b6102266004803603602081101561018357600080fd5b81019080803590602001906401000000008111156101a057600080fd5b8201836020820111156101b257600080fd5b803590602001918460018302840111640100000000831117156101d457600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f8201169050808301925050505050505091929192905050506103d8565b6040518082815260200191505060405180910390f35b6102686004803603602081101561025257600080fd5b8101908080359060200190929190505050610406565b6040518080602001838152602001828103825284818151815260200191508051906020019080838360005b838110156102ae578082015181840152602081019050610293565b50505050905090810190601f1680156102db5780820380516001836020036101000a031916815260200191505b50935050505060405180910390f35b60008054905090565b8060008190555050565b6001604051806040016040528084815260200183815250908060018154018082558091505060019003906000526020600020906002020160009091909190915060008201518160000190805190602001906103599291906104cf565b50602082015181600101555050806002836040518082805190602001908083835b6020831061039d578051825260208201915060208101905060208303925061037a565b6001836020036101000a0380198251168184511680821785525050505050509050019150509081526020016040518091039020819055505050565b6002818051602081018201805184825260208301602085012081835280955050505050506000915090505481565b6001818154811061041357fe5b9060005260206000209060020201600091509050806000018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156104bf5780601f10610494576101008083540402835291602001916104bf565b820191906000526020600020905b8154815290600101906020018083116104a257829003601f168201915b5050505050908060010154905082565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061051057805160ff191683800117855561053e565b8280016001018555821561053e579182015b8281111561053d578251825591602001919060010190610522565b5b50905061054b919061054f565b5090565b61057191905b8082111561056d576000816000905550600101610555565b5090565b9056fea26469706673582212200123e4930113309f464cbb148407bc4273fef984586e62238fb3054b55d5afed64736f6c63430006000033",
	                        "opcodes": "PUSH1 0x80 PUSH1 0x40 MSTORE CALLVALUE DUP1 ISZERO PUSH2 0x10 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH2 0x5AA DUP1 PUSH2 0x20 PUSH1 0x0 CODECOPY PUSH1 0x0 RETURN INVALID PUSH1 0x80 PUSH1 0x40 MSTORE CALLVALUE DUP1 ISZERO PUSH2 0x10 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH1 0x4 CALLDATASIZE LT PUSH2 0x57 JUMPI PUSH1 0x0 CALLDATALOAD PUSH1 0xE0 SHR DUP1 PUSH4 0x2E64CEC1 EQ PUSH2 0x5C JUMPI DUP1 PUSH4 0x6057361D EQ PUSH2 0x7A JUMPI DUP1 PUSH4 0x6F760F41 EQ PUSH2 0xA8 JUMPI DUP1 PUSH4 0x90C3EE4D EQ PUSH2 0x16D JUMPI DUP1 PUSH4 0x9E7A13AD EQ PUSH2 0x23C JUMPI JUMPDEST PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH2 0x64 PUSH2 0x2EA JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 DUP3 DUP2 MSTORE PUSH1 0x20 ADD SWAP2 POP POP PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST PUSH2 0xA6 PUSH1 0x4 DUP1 CALLDATASIZE SUB PUSH1 0x20 DUP2 LT ISZERO PUSH2 0x90 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST DUP2 ADD SWAP1 DUP1 DUP1 CALLDATALOAD SWAP1 PUSH1 0x20 ADD SWAP1 SWAP3 SWAP2 SWAP1 POP POP POP PUSH2 0x2F3 JUMP JUMPDEST STOP JUMPDEST PUSH2 0x16B PUSH1 0x4 DUP1 CALLDATASIZE SUB PUSH1 0x40 DUP2 LT ISZERO PUSH2 0xBE JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST DUP2 ADD SWAP1 DUP1 DUP1 CALLDATALOAD SWAP1 PUSH1 0x20 ADD SWAP1 PUSH5 0x100000000 DUP2 GT ISZERO PUSH2 0xDB JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST DUP3 ADD DUP4 PUSH1 0x20 DUP3 ADD GT ISZERO PUSH2 0xED JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST DUP1 CALLDATALOAD SWAP1 PUSH1 0x20 ADD SWAP2 DUP5 PUSH1 0x1 DUP4 MUL DUP5 ADD GT PUSH5 0x100000000 DUP4 GT OR ISZERO PUSH2 0x10F JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST SWAP2 SWAP1 DUP1 DUP1 PUSH1 0x1F ADD PUSH1 0x20 DUP1 SWAP2 DIV MUL PUSH1 0x20 ADD PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP1 SWAP4 SWAP3 SWAP2 SWAP1 DUP2 DUP2 MSTORE PUSH1 0x20 ADD DUP4 DUP4 DUP1 DUP3 DUP5 CALLDATACOPY PUSH1 0x0 DUP2 DUP5 ADD MSTORE PUSH1 0x1F NOT PUSH1 0x1F DUP3 ADD AND SWAP1 POP DUP1 DUP4 ADD SWAP3 POP POP POP POP POP POP POP SWAP2 SWAP3 SWAP2 SWAP3 SWAP1 DUP1 CALLDATALOAD SWAP1 PUSH1 0x20 ADD SWAP1 SWAP3 SWAP2 SWAP1 POP POP POP PUSH2 0x2FD JUMP JUMPDEST STOP JUMPDEST PUSH2 0x226 PUSH1 0x4 DUP1 CALLDATASIZE SUB PUSH1 0x20 DUP2 LT ISZERO PUSH2 0x183 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST DUP2 ADD SWAP1 DUP1 DUP1 CALLDATALOAD SWAP1 PUSH1 0x20 ADD SWAP1 PUSH5 0x100000000 DUP2 GT ISZERO PUSH2 0x1A0 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST DUP3 ADD DUP4 PUSH1 0x20 DUP3 ADD GT ISZERO PUSH2 0x1B2 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST DUP1 CALLDATALOAD SWAP1 PUSH1 0x20 ADD SWAP2 DUP5 PUSH1 0x1 DUP4 MUL DUP5 ADD GT PUSH5 0x100000000 DUP4 GT OR ISZERO PUSH2 0x1D4 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST SWAP2 SWAP1 DUP1 DUP1 PUSH1 0x1F ADD PUSH1 0x20 DUP1 SWAP2 DIV MUL PUSH1 0x20 ADD PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP1 SWAP4 SWAP3 SWAP2 SWAP1 DUP2 DUP2 MSTORE PUSH1 0x20 ADD DUP4 DUP4 DUP1 DUP3 DUP5 CALLDATACOPY PUSH1 0x0 DUP2 DUP5 ADD MSTORE PUSH1 0x1F NOT PUSH1 0x1F DUP3 ADD AND SWAP1 POP DUP1 DUP4 ADD SWAP3 POP POP POP POP POP POP POP SWAP2 SWAP3 SWAP2 SWAP3 SWAP1 POP POP POP PUSH2 0x3D8 JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 DUP3 DUP2 MSTORE PUSH1 0x20 ADD SWAP2 POP POP PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST PUSH2 0x268 PUSH1 0x4 DUP1 CALLDATASIZE SUB PUSH1 0x20 DUP2 LT ISZERO PUSH2 0x252 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST DUP2 ADD SWAP1 DUP1 DUP1 CALLDATALOAD SWAP1 PUSH1 0x20 ADD SWAP1 SWAP3 SWAP2 SWAP1 POP POP POP PUSH2 0x406 JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 DUP1 PUSH1 0x20 ADD DUP4 DUP2 MSTORE PUSH1 0x20 ADD DUP3 DUP2 SUB DUP3 MSTORE DUP5 DUP2 DUP2 MLOAD DUP2 MSTORE PUSH1 0x20 ADD SWAP2 POP DUP1 MLOAD SWAP1 PUSH1 0x20 ADD SWAP1 DUP1 DUP4 DUP4 PUSH1 0x0 JUMPDEST DUP4 DUP2 LT ISZERO PUSH2 0x2AE JUMPI DUP1 DUP3 ADD MLOAD DUP2 DUP5 ADD MSTORE PUSH1 0x20 DUP2 ADD SWAP1 POP PUSH2 0x293 JUMP JUMPDEST POP POP POP POP SWAP1 POP SWAP1 DUP2 ADD SWAP1 PUSH1 0x1F AND DUP1 ISZERO PUSH2 0x2DB JUMPI DUP1 DUP3 SUB DUP1 MLOAD PUSH1 0x1 DUP4 PUSH1 0x20 SUB PUSH2 0x100 EXP SUB NOT AND DUP2 MSTORE PUSH1 0x20 ADD SWAP2 POP JUMPDEST POP SWAP4 POP POP POP POP PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST PUSH1 0x0 DUP1 SLOAD SWAP1 POP SWAP1 JUMP JUMPDEST DUP1 PUSH1 0x0 DUP2 SWAP1 SSTORE POP POP JUMP JUMPDEST PUSH1 0x1 PUSH1 0x40 MLOAD DUP1 PUSH1 0x40 ADD PUSH1 0x40 MSTORE DUP1 DUP5 DUP2 MSTORE PUSH1 0x20 ADD DUP4 DUP2 MSTORE POP SWAP1 DUP1 PUSH1 0x1 DUP2 SLOAD ADD DUP1 DUP3 SSTORE DUP1 SWAP2 POP POP PUSH1 0x1 SWAP1 SUB SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 PUSH1 0x2 MUL ADD PUSH1 0x0 SWAP1 SWAP2 SWAP1 SWAP2 SWAP1 SWAP2 POP PUSH1 0x0 DUP3 ADD MLOAD DUP2 PUSH1 0x0 ADD SWAP1 DUP1 MLOAD SWAP1 PUSH1 0x20 ADD SWAP1 PUSH2 0x359 SWAP3 SWAP2 SWAP1 PUSH2 0x4CF JUMP JUMPDEST POP PUSH1 0x20 DUP3 ADD MLOAD DUP2 PUSH1 0x1 ADD SSTORE POP POP DUP1 PUSH1 0x2 DUP4 PUSH1 0x40 MLOAD DUP1 DUP3 DUP1 MLOAD SWAP1 PUSH1 0x20 ADD SWAP1 DUP1 DUP4 DUP4 JUMPDEST PUSH1 0x20 DUP4 LT PUSH2 0x39D JUMPI DUP1 MLOAD DUP3 MSTORE PUSH1 0x20 DUP3 ADD SWAP2 POP PUSH1 0x20 DUP2 ADD SWAP1 POP PUSH1 0x20 DUP4 SUB SWAP3 POP PUSH2 0x37A JUMP JUMPDEST PUSH1 0x1 DUP4 PUSH1 0x20 SUB PUSH2 0x100 EXP SUB DUP1 NOT DUP3 MLOAD AND DUP2 DUP5 MLOAD AND DUP1 DUP3 OR DUP6 MSTORE POP POP POP POP POP POP SWAP1 POP ADD SWAP2 POP POP SWAP1 DUP2 MSTORE PUSH1 0x20 ADD PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 KECCAK256 DUP2 SWAP1 SSTORE POP POP POP JUMP JUMPDEST PUSH1 0x2 DUP2 DUP1 MLOAD PUSH1 0x20 DUP2 ADD DUP3 ADD DUP1 MLOAD DUP5 DUP3 MSTORE PUSH1 0x20 DUP4 ADD PUSH1 0x20 DUP6 ADD KECCAK256 DUP2 DUP4 MSTORE DUP1 SWAP6 POP POP POP POP POP POP PUSH1 0x0 SWAP2 POP SWAP1 POP SLOAD DUP2 JUMP JUMPDEST PUSH1 0x1 DUP2 DUP2 SLOAD DUP2 LT PUSH2 0x413 JUMPI INVALID JUMPDEST SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 PUSH1 0x2 MUL ADD PUSH1 0x0 SWAP2 POP SWAP1 POP DUP1 PUSH1 0x0 ADD DUP1 SLOAD PUSH1 0x1 DUP2 PUSH1 0x1 AND ISZERO PUSH2 0x100 MUL SUB AND PUSH1 0x2 SWAP1 DIV DUP1 PUSH1 0x1F ADD PUSH1 0x20 DUP1 SWAP2 DIV MUL PUSH1 0x20 ADD PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP1 SWAP3 SWAP2 SWAP1 DUP2 DUP2 MSTORE PUSH1 0x20 ADD DUP3 DUP1 SLOAD PUSH1 0x1 DUP2 PUSH1 0x1 AND ISZERO PUSH2 0x100 MUL SUB AND PUSH1 0x2 SWAP1 DIV DUP1 ISZERO PUSH2 0x4BF JUMPI DUP1 PUSH1 0x1F LT PUSH2 0x494 JUMPI PUSH2 0x100 DUP1 DUP4 SLOAD DIV MUL DUP4 MSTORE SWAP2 PUSH1 0x20 ADD SWAP2 PUSH2 0x4BF JUMP JUMPDEST DUP3 ADD SWAP2 SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 JUMPDEST DUP2 SLOAD DUP2 MSTORE SWAP1 PUSH1 0x1 ADD SWAP1 PUSH1 0x20 ADD DUP1 DUP4 GT PUSH2 0x4A2 JUMPI DUP3 SWAP1 SUB PUSH1 0x1F AND DUP3 ADD SWAP2 JUMPDEST POP POP POP POP POP SWAP1 DUP1 PUSH1 0x1 ADD SLOAD SWAP1 POP DUP3 JUMP JUMPDEST DUP3 DUP1 SLOAD PUSH1 0x1 DUP2 PUSH1 0x1 AND ISZERO PUSH2 0x100 MUL SUB AND PUSH1 0x2 SWAP1 DIV SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 PUSH1 0x1F ADD PUSH1 0x20 SWAP1 DIV DUP2 ADD SWAP3 DUP3 PUSH1 0x1F LT PUSH2 0x510 JUMPI DUP1 MLOAD PUSH1 0xFF NOT AND DUP4 DUP1 ADD OR DUP6 SSTORE PUSH2 0x53E JUMP JUMPDEST DUP3 DUP1 ADD PUSH1 0x1 ADD DUP6 SSTORE DUP3 ISZERO PUSH2 0x53E JUMPI SWAP2 DUP3 ADD JUMPDEST DUP3 DUP2 GT ISZERO PUSH2 0x53D JUMPI DUP3 MLOAD DUP3 SSTORE SWAP2 PUSH1 0x20 ADD SWAP2 SWAP1 PUSH1 0x1 ADD SWAP1 PUSH2 0x522 JUMP JUMPDEST JUMPDEST POP SWAP1 POP PUSH2 0x54B SWAP2 SWAP1 PUSH2 0x54F JUMP JUMPDEST POP SWAP1 JUMP JUMPDEST PUSH2 0x571 SWAP2 SWAP1 JUMPDEST DUP1 DUP3 GT ISZERO PUSH2 0x56D JUMPI PUSH1 0x0 DUP2 PUSH1 0x0 SWAP1 SSTORE POP PUSH1 0x1 ADD PUSH2 0x555 JUMP JUMPDEST POP SWAP1 JUMP JUMPDEST SWAP1 JUMP INVALID LOG2 PUSH5 0x6970667358 0x22 SLT KECCAK256 ADD 0x23 0xE4 SWAP4 ADD SGT ADDRESS SWAP16 CHAINID 0x4C 0xBB EQ DUP5 SMOD 0xBC TIMESTAMP PUSH20 0xFEF984586E62238FB3054B55D5AFED64736F6C63 NUMBER STOP MOD STOP STOP CALLER ",
	                        "sourceMap": "57:621:0:-:0;;;;8:9:-1;5:2;;;30:1;27;20:12;5:2;57:621:0;;;;;;;"
	                    }
	                },
	                "metadata": "{\"compiler\":
	                {\"version\":\"0.6.0+commit.26b70077\"},\"language\":\"Solidity\",\"output\":{\"abi\":
	                [{\"inputs\":[{\"internalType\":\"string\",\"name\":\"_name\",\"type\":\"string\"},{\"internalType\":\"uint256\",\"name\":\"_age\",\"type\":\"uint256\"}],\"name\":\"addPerson\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"string\",\"name\":\"\",\"type\":\"string\"}],\"name\":\"nameToAge\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"name\":\"people\",\"outputs\":[{\"internalType\":\"string\",\"name\":\"name\",\"type\":\"string\"},{\"internalType\":\"uint256\",\"name\":\"age\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"retrieve\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"_number\",\"type\":\"uint256\"}],\"name\":\"store\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"}],\"devdoc\":{\"methods\":{}},\"userdoc\":{\"methods\":{}}},\"settings\":{\"compilationTarget\":{\"SimpleStorage.sol\":\"SimpleStorage\"},\"evmVersion\":\"istanbul\",\"libraries\":{},\"metadata\":{\"bytecodeHash\":\"ipfs\"},\"optimizer\":{\"enabled\":false,\"runs\":200},\"remappings\":[]},\"sources\":{\"SimpleStorage.sol\":{\"keccak256\":\"0xb11711c64caefb78b120cd8256db30671152a5d3876985bb4ca130279483606a\",\"urls\":[\"bzz-raw://5f997a4db547a6d33f142503a952bbe1a790ea9f8688a33396ca61b6a2a5cca2\",\"dweb:/ipfs/QmUWGUYe32RLXvryLXgjBTTQdFK9CGVDjwP1C7kRBrMgvN\"]}},\"version\":1}"
	            }
	        }
	    },
	    "sources":
	    {
	        "SimpleStorage.sol":
	        {
	            "id": 0
	        }
	    }
	}

Deploying in python
====================

- In order to deploy a smart contract in python, we first have to get the **bytecode** and the **abi**. We can check the **JSON** compiled code to see how we can access both of them.


.. code-block:: python

	import solcx
	solcx.install_solc('0.6.0')

	from solcx import compile_standard
	import json

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

- Now that we have both the bytecode and the abi, we are ready to deploy this smart contract to a blockchain. However, in REMIX IDE, we were used to work with either a testnet or a simulated VM. How can we do this same thing outside of REMIX ? 

- This is where **Ganache** comes into play !

.. NOTE::

	- Ganache is a simulated (fake) blockchain that  we can use to deploy our smart contracts to and have it interact like it's a real blockchain.

	- Ganache creates a local blockchain, meaning that this blockchain isn't connected to any other blockchain out there but it will act like a blockchain which will make it faster than us interacting with a testnet.

	- With Ganache, we have control over the entire blockchain as we are the only node.

	- There are 2 modes that can be used to work with **Ganache**, either a command line mode or an interface mode.

Connecting to ganache: Web3.py
------------------------------

- In order to connect to Ganache blockchain, we need an HTTP provider. In ganache UI, we have an HTTP RPC server on top. This is the server where the fake ganache blockchain is. The url provided there is gonna be used to connect to the blockchain.

- In REMIX, our HTTP Provider is Metamask in case we were using a testnet for example.

- Syntax to connect to ganache blockchain:

.. code-block:: python
	
	# RPC Server
	w3 = Web3(Web3.HTTPProvider("url_provided_by_ganache"))

- We also need a ChainId, or the network ID: In my particular case, the ganache chain ID is "1337".

.. code-block:: python
	
	# RPC Server and chain Id
	w3 = Web3(Web3.HTTPProvider("url_provided_by_ganache"))
	chainId = 1337

- We also gonna need an address to deploy from. In a javascript VM in REMIX, we were also given a bunch of addresses that we can use similarly to what ganache provides.

.. code-block:: python
	
	# RPC Server and chain Id and Address
	w3 = Web3(Web3.HTTPProvider("url_provided_by_ganache"))
	chainId = 5777
	my_address = "0x454C2e1AaF628A6F5e368Cd2926DAafa83DAf8D2"

- We need the **private key** corresponding to this address to sign our transactions. **It should always begin with 0x so ADD IT if it wasn't there,** because Python will always look for the hexadecimal version of the private key. 

.. code-block:: python
	
	# RPC Server and chain Id and Address
	w3 = Web3(Web3.HTTPProvider("url_provided_by_ganache"))
	chainId = 5777
	my_address = "0x454C2e1AaF628A6F5e368Cd2926DAafa83DAf8D2"
	private_key = "0x8ac4ac7d9003b1fd2afbaf30476699fb14f81918caae4ca47591b920d612d8d2"


.. warning::

	**PRIVATE KEYS MANAGEMENT**

	- In order to protect our private key and since we are working with a conda dev environement, we can set the private key as an env-variable like this: 

	.. code-block:: bash

		export PRIVATE_KEY = "0x0000000000000000000000"
		
	- If we want our private key to be printed on terminal, we can type: 

	.. code-block:: bash

		echo $PRIVATE_KEY

	- Then is we want to call this variable from python: ``os.getenv("PRIVATE_KEY")``


	- Alternatively, we can create a .env file and store the environement variables in this file. Then we can use the **dotenv** python package to load environement vars directly from the ``.env`` file. In case we did this, we can perhaps accidentaly push our .env to a github repo and if the private key was in the ".env" file, then we will be doing a huge mistake by giving everyone our private key. So, to prevent this accidental push, we should create in the same directory as .env and the rest of the project, a **.gitignore** file and add **.env** to that file. The syntax to be used in this case is: 

	.. code-block:: python

		# Assuming we have .env file with a PRIVATE_KEY variable:
		# we load_dotenv:
		from dotenv import load_dotenv
		load_dotenv() 

		# This command automatically looks for .env file and 
		# loads the env variables that are thereon when called.
		# We load our private key the usual way:
		private_key = os.getenv("PRIVATE_KEY")

	- We will include a **.env** example file in the bottom of this page.

- Now we have to create our contract and deploy it to ganache
- In order to deploy the smart contract, we need to:
	- 1. build the transaction
	- 2. sign the transaction
	- 3. send the transaction

- A transaction is a change of the state of the blockchain. So, each time we want to do change the state of the blockchain, we have to do it in a transaction.

- We are also going to need to the nonce. The nonce is actually just the number of transactions that our account have actually made. Everytime we make a new transaction, our transaction is hashed with a new nonce.

.. code-block:: python
	
	# RPC Server and chain Id and Address
	w3 = Web3(Web3.HTTPProvider("url_provided_by_ganache"))
	chainId = 5777
	my_address = "0x454C2e1AaF628A6F5e368Cd2926DAafa83DAf8D2"
	private_key = "0x8ac4ac7d9003b1fd2afbaf30476699fb14f81918caae4ca47591b920d612d8d2"

	# Create the contract instance given an abi and a bytecode
	SimpleStorage = w3.eth.contract(abi=abi,bytecode=bytecode)

	# get the nonce of the transaction 
	# ( = the latest transaction count)
	nonce = w3.eth.getTransactionCount(my_address)

	# Create the transaction object
	transaction_parameters = {"chainId":chainId, "from":my_address, "nonce":nonce}
	transaction = SimpleStorage.constructor().buildTransaction(transaction_parameters)

	"""
	Importante note:
	
	SimpleStorage doesn't actually have a constructor ! 
	Every contract however technically have a constructor.
	
	The FundMe example does have a constructor but for the 
	sake of simplicity, the SimpleStorage.sol contract is 
	blank and doesn't have a constructor.

	In addition, when creating the transaction object, we 
	always have to pass some transaction parameters in web3.py
	which are the chainId, the adress of the sender, and the 
	nonce 
	"""

	# Once we create the transaction object which we can print
	# and see, we should sign the transaction.

	signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key) 

	# Note: The private key should be protected and not hardcoded 
	# the way we did here.

- In the following, we are going to use the ".env" private key storing method in our python script, but, in case we are using real money, no digital storing is recommended.

.. code-block:: python
	
	# RPC Server and chain Id and Address
	w3 = Web3(Web3.HTTPProvider("url_provided_by_ganache"))
	chainId = 5777
	my_address = "0xd13b9C18ef6376069bCB44f5878bfd8FbDe2dDC2"
	private_key = os.getenv("PRIVATE_KEY")

	SimpleStorage = w3.eth.contract(abi=abi,bytecode=bytecode)

	nonce = w3.eth.getTransactionCount(my_address)

	# Create the transaction object
	transaction_parameters = {"chainId":chainId, "from":my_address, "nonce":nonce}
	transaction = SimpleStorage.constructor().buildTransaction(transaction_parameters)

	signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key) 

	# Send the signed transaction to the blockchain
	tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransation)


- Another good practice is waiting for block confirmations to happen. In order to do so, we can use the ``wait_for_transaction_receipt`` method.
	
.. code-block:: python
	
	# RPC Server and chain Id and Address
	w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
	chainId = 1337
	my_address = os.getenv("PUBLIC_KEY")
	private_key = os.getenv("PRIVATE_KEY")

	SimpleStorage = w3.eth.contract(abi=abi,bytecode=bytecode)

	nonce = w3.eth.getTransactionCount(my_address)

	# Create the transaction object
	transaction_parameters = {"gasPrice": w3.eth.gas_price, "chainId":chainId, "from":my_address, "nonce":nonce}
	transaction = SimpleStorage.constructor().buildTransaction(transaction_parameters)

	# Sign the transaction
	signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key) 

	# Send the signed transaction to the blockchain
	tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

	# Waiting for block confirmations:
	tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)


Interacting with the contract after deployment
==============================================

- In order to interact with a contract, we need the contract ABI and the contract address. We can initialize our **deployed** contract like so:

.. code-block:: python
	
	simple_storage = w3.eth.contract(address = tx_receipt.contractAddress, abi=abi)

- We must note here that we can access the contract address through ``tx_receipt``.

- Now we can interact with all the functions that are defined inside the deployed contract. In REMIX IDE, when we deploy a contract, we get buttons corresponding to the different public variables and functions. As a reminder, a blue button correponds to a view function, an orange function correponds to a function that we can transact on, and a red button corresponds to a payable function.

- In Python, we don't have buttons. Instead, we can use a function of the smart contract by using either a call method (if it was a view function) or a transact method (if it was a function that will change the state of a blockchain).

- Example for the view function "retrieve()":

.. code-block:: python
	
	retrieve_output = simple_storage.functions.retrieve().call()
	print(retrieve_output)

- Example for the transaction function "store()".

.. code-block:: python
	
	store_value = simple_storage.functions.store(15).buildTransaction(transaction_parameters)

- At this point, the transaction didn't go through yet. We need to sign it, then we need to send it. Only then we can retrieve the stored value. One important note is that the nonce should be the next ``nonce``, that is ``nonce + 1`` in the transaction parameters, as it is obvious that the nonce can be defined in a unique way to every signle transactionand no two transactions can have the same nonce. 


.. code-block:: python

	# Now let's store a value and try to retrieve it:
	transaction_parameters = {"gasPrice": w3.eth.gas_price, "chainId":chainId, "from":my_address, "nonce":nonce+1}

	# we use nonce + 1 bcs nonce has already been used
	store_value = simple_storage.functions.store(15).buildTransaction(transaction_parameters)
	signed_store_value = w3.eth.account.sign_transaction(store_value, private_key=private_key)
	store_value_hash = w3.eth.send_raw_transaction(signed_store_value.rawTransaction)
	store_value_receipt = w3.eth.wait_for_transaction_receipt(store_value_hash)

	output_retrieve = simple_storage.functions.retrieve().call() # we use call as it is a view function
	print(output_retrieve)

- We conclude this part giving the whole code:

.. code-block:: python

	"""
	deploy_simple_storage_UI.py
	Author = "Mouloud Bahae eddine"
	"""

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
	w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
	chainId = 1337
	my_address = os.getenv("PUBLIC_KEY")
	private_key = os.getenv("PRIVATE_KEY")

	SimpleStorage = w3.eth.contract(abi=abi,bytecode=bytecode)

	nonce = w3.eth.getTransactionCount(my_address)

	# Create the transaction object
	transaction_parameters = {"gasPrice": w3.eth.gas_price, "chainId":chainId, "from":my_address, "nonce":nonce}
	transaction = SimpleStorage.constructor().buildTransaction(transaction_parameters)

	# Sign the transaction
	signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key) 

	# Send the signed transaction to the blockchain
	tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

	# Waiting for block confirmations:
	tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

	# define the compiled smart contract to strat interacting with it:
	# we need the contract address and its abi
	simple_storage = w3.eth.contract(tx_receipt.contractAddress, abi = abi)

	# output the resukt of the retrieve() function of simple storage for example:
	output_retrieve = simple_storage.functions.retrieve().call() # we use call as it is a view function
	print(output_retrieve)

	# Now let's store a value and try to retrieve it:
	transaction_parameters = {"gasPrice": w3.eth.gas_price, "chainId":chainId, "from":my_address, "nonce":nonce+1}
	# we use nonce + 1 bcs nonce has already been used
	store_value = simple_storage.functions.store(15).buildTransaction(transaction_parameters)
	signed_store_value = w3.eth.account.sign_transaction(store_value, private_key=private_key)
	store_value_hash = w3.eth.send_raw_transaction(signed_store_value.rawTransaction)
	store_value_receipt = w3.eth.wait_for_transaction_receipt(store_value_hash)

	output_retrieve = simple_storage.functions.retrieve().call() # we use call as it is a view function
	print(output_retrieve)



Ganache in command line mode
============================

- Ganache UI is good, but ganache-cli (which is the command line version) is even better. We can install ganache-cli in linux in the following steps:

	- ``sudo apt install nodejs`` ---> This will install nodejs package.
	- ``sudo apt install npm`` --> This will install npm.
	- ``sudo npm install --global yarn`` --> This will install yarn package.
	- ``sudo yarn global add ganache-cli`` --> This will install ganache-cli with yarn.

- Now we can run a local blockchain from the command line. To do so, we run ``ganache-cli``. This will provide us with a local blockchain that runs in our local machine via the terminal with all what we need to deploy contracts and interact with them such as the available accounts, the private keys etc...

- An additional feature in the command line mode is that, we can fix the addresses and private keys. These are randomely generated when calling Ganache, but if we want to always fix them to certain values so that we don't update our code each time with new addresses and private keys, we can do so by calling ganache in the following way: ``ganache-cli --deterministic`` or ``ganache-cli -d``.

- Now we can run the same "depoly" script to start interacting with the smart contract. All we have to change is the HTTP provider to be that of the localhost provided by the cli and the address and private key.

.. code-block:: python

	# deploy_simple_storage_ganache-cli.py

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
	HTTP_PROVIDER = os.getenv("HTTP_PROVIDER")
	w3 = Web3(Web3.HTTPProvider(HTTP_PROVIDER))
	chainId = 1337
	my_address = os.getenv("PUBLIC_KEY")
	private_key = os.getenv("PRIVATE_KEY")

	SimpleStorage = w3.eth.contract(abi=abi,bytecode=bytecode)

	nonce = w3.eth.getTransactionCount(my_address)

	# Create the transaction object
	transaction_parameters = {"gasPrice": w3.eth.gas_price, "chainId":chainId, "from":my_address, "nonce":nonce}
	transaction = SimpleStorage.constructor().buildTransaction(transaction_parameters)

	# Sign the transaction
	signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key) 

	# Send the signed transaction to the blockchain
	tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

	# Waiting for block confirmations:
	tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

	# define the compiled smart contract to strat interacting with it:
	# we need the contract address and its abi
	simple_storage = w3.eth.contract(tx_receipt.contractAddress, abi = abi)

	# output the resukt of the retrieve() function of simple storage for example:
	output_retrieve = simple_storage.functions.retrieve().call() # we use call as it is a view function
	print(output_retrieve)

	# Now let's store a value and try to retrieve it:
	transaction_parameters = {"gasPrice": w3.eth.gas_price, "chainId":chainId, "from":my_address, "nonce":nonce+1}
	# we use nonce + 1 bcs nonce has already been used
	store_value = simple_storage.functions.store(15).buildTransaction(transaction_parameters)
	signed_store_value = w3.eth.account.sign_transaction(store_value, private_key=private_key)
	store_value_hash = w3.eth.send_raw_transaction(signed_store_value.rawTransaction)
	store_value_receipt = w3.eth.wait_for_transaction_receipt(store_value_hash)

	output_retrieve = simple_storage.functions.retrieve().call() # we use call as it is a view function
	print(output_retrieve)

- We can also connect to a testnet or a mainnet, all we have to do is setting the appropriate HTTP provider, the address, the private key as well as the chainId. We have many options here, we can either run a local node and connect to it => We can run our own blockchain (difficult to do). Or, we can use third-party clients to run a blockchain for us (like infura.io or alchemy.com).

- If we're going to use Infura for example, we first have to create an account, then, infura will provide us with the necessary http url of a blockchain. [HTTP ✔✔]

- Any chainID can be found in the **chainlist.org** website. For a **Rinkeby testnet** for example, the chainID is 4. [chainid ✔✔]

- We need the public and private keys in order to interact with a test or mainnet => We can simply get them from Metamask [keys ✔✔]

- Example script with an infura provided blockchain with a Rinkeby testnet.

.. code-block:: python

	# deploy_infura.py

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

Example files
==============

".env" example file
-------------------

.. code-block:: bash

	# Example working with ganache
	PUBLIC_KEY = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"
	PRIVATE_KEY = "0x4f3edf983ac636a65a842ce7c78d9aa706d3b113bce9c46f30d7d21715b23b1d"
	HTTP_PROVIDER = "http://127.0.0.1:8545"
	GANACHE_CHAIN_ID = 1337

	# Example working with infura
	HTTP_PROVIDER_INFURA = "https://rinkeby.infura.io/v3/74eec412a7cb4c378ee826ae699dc7bc"
	RINKEBY_CHAIN_ID = 4
	PUBLIC_KEY_RINKEBY_METAMASK = "0x44Ee91Bded46d0B5B13845124ca949F4f048Ed64" # FROM METAMASK
	PRIVATE_KEY_RINKEBY_METAMASK = "0xd96878979409f342bae19f4d68c293e108c9c67db0a92c4183bc624e574d4987"# FROM METAMASK

".gitignore" example file
-------------------------

.. code-block:: bash

	.env

Conclusion
==========

- **Web3.py** is indeed a good python package to compile, deploy and interact with smart contracts. However, it seems like it's a lot of work having to do everything from scratch all on our own. Plus, what if we want to interact with a contract that we deployed in the past ? The way we have developped in here works fine with a new contract that we want to deploy and interact with it but it isn't the best option if we want to interact with an already deployed contract. A solution, a very good solution indeed is using another python-based developpement and testing frameword for smart contracts targeting the EVM called "brownie".

Brownie 🥧
==========

- Brownie is currently the most populat smart contract developpment plateform built based on python. It is used by DeFi giants such as `yearn.finance`, `curve.fi`, `badger.finance` etc... Brownie is built on top of Web3.py.

- In order to install ``brownie``, the most recommened way is to use "pipx":

	- ``pipx`` installs Brownie into a virtual environment and makes it available directly from the commandline. Once installed, you will never have to activate a virtual environment prior to using Brownie.
	``python3 -m pip install --user pipx``
	``python3 -m pipx ensurepath``.

	- When we are done with these two, we can close and reopen the terminal and type: 
	``pipx install eth-brownie``.

	- We close and reopen the terminal and now everything is well established.

- In order to initialize a project in brownie, we create a directory for our project and we type in the terminal: ``brownie init``. This will create a bunch of directories inside the directory we're currently in:

	- "build" directory: keeps track of all the interfaces we are working with (through the `interfaces` subdir), all of our deployments across different chains (through the `deployments` subdir) and it's gonna store all of the compiled code (through the `contracts` subdir).

	- "contracts" directory: where we're gonna store our solidity contracts.

	- "Interfaces" directory: It is where we are going to store our interfaces

	- "scripts" directory is where we store our scripts that automate tasks.

	- "tests" directory: For performing tests.

- Brownie can be used from the terminal as well as from python scripts. 

- Compiling a smart contract

	- As an example, if we take our ``simple_storage.sol`` and save it into the **contracts** folder, we can run ``brownie compile`` from the terminal. Brownie will automatically read the version of solidity and then store all of the compile information in the build folder.

- Deployment:

	- In order to deploy to the blockchain, we have to write a script that will allow us to do whatever we want and we will have to store it in the scripts directory. 

	- Brownie runs a script from terminal with ``brownie run scripts/file.py``.

	- Brownie will automatically spin up a local ganache chain by default to deploy to and turn it off at the end of the script if we don't give him a network to use. A local Ganache-cli blockchain is the default blockchain that brownie uses.

	- A good tip here is to put the logic of our deployment in terms of functions.

	- We must retrieve our account information, the public and private keys in order to do the deployment.

- Working with accounts:

	- Brownie has a native way to work with accounts through the ``accounts`` module and it is fantastic !

		- If and only if we are working with ganache-CLI, we don't need to pass any public and private key as brownie natively understands what account we want to work with simply by passing its index in ganache:

		.. code-block:: python 

			# import accounts module
			from brownie import accounts

			# Select an account to work with
			def deploy_simple_storage():
				account = accounts[0] # the account at the 0-th index of ganache-cli
				print(account)

			# The function to be executed 
			def main():
				deploy_simple_storage()

		- A second method is to define a new account in brownie through the commandline and then use it. Syntax: ``brownie accounts new account_1``. This method allow us to use not only ganache-cli but also Metamask accounts and password-encrypts the Private-Key !! **AND THIS IS THE MOST SECURE METHOD OF DEALING WITH PRIVATE KEYS**. Once created, we can list all of our accounts using ``brownie accounts list``. If we want to delete an account, we can use ``brownie accounts delete account_name``

		.. code-block:: python

			# import accounts module
			from brownie import accounts

			# Select an account to work with
			def deploy_simple_storage():
				account = accounts.load("account_name")
				
				# This time, this is a password encrypted account,
				# When we will compile this script, it will 
				# ask us for a password 
				print(account) 
				
			# The function to be executed 
			def main():
				deploy_simple_storage()

		- The third method is to use a brownie ``brownie-config.yaml`` file. This is a special file that brownie will always look for to grab information about where you gonna build, deploy and grab things. In this case, we need to tell ``brownie-config.yaml`` to look for the private key inside a specific``.env`` file.

		.. code-block:: yaml

			dotenv: .env 
			# This will tell brownie that this is the right 
			# location where you can grab your informations 
			# from. 

		.. code-block:: python

			# To call the Private_key that is stored inside of
			# the ``.env`` file for example, we use:
			account = accounts.add(os.getenv("PRIVATE_KEY"))

- The third method can be further improved, we can add in our ``brownie-config.yaml`` a wallets definition that have keys that point out to our differents private keys defined in .env environement:
		
	.. code-block:: yaml

		dotenv: .env
		wallets:
			from_key: ${PRIVATE_KEY} 
			# Note that the indentation is using spaces as 
			# tabs are not allowed in a yaml file


	.. code-block:: python

		# To call the Private_key, we access it through:
		from brownie import config
		account = accounts.add(config["wallets"]["from_key"])
		print(account)

Deployment in Brownie
----------------------

- Brownie makes it very easy to deploy a smart contract to the blockchain. We can literally just import our smart contract directly from Brownie, and use the ``deploy()`` method that acts on imported contracts.

- In the following example, we illustrate the use of the ``deploy()`` method.

.. code-block:: python

	# Brownie can import the solidity contract (SimpleStorage) directly !
	from brownie import accounts, SimpleStorage

	# Select an account to work with
	def deploy_simple_storage():
		account = accounts[0] # the first account in the local ganache chain
		simple_storage = SimpleStorage.deploy({"from":account})
		print(simple_storage) # a contract object deployed from the account "account"

	# The function to be executed 
	def main():
		deploy_simple_storage()

- As we can see, we don't need to specify the many things we specified when we used ``web3.py``. Plus, Brownie undertands directly whether the function we will execute is a ``transact`` function (that makes a state change to the blockchain) or a ``call`` function.

- The ``{"from":account}`` is only needed when a function that we are using is a transact function.

- Now we will redo exactly what we did using ``web3.py`` in **brownie**. 

.. code-block:: python

	from brownie import accounts, SimpleStorage

	def deploy_simple_storage():
		account = accounts[0]
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

- As we can see, we can use the created ``simple_storage`` (contract) variable directly. the functions defined in the solidity smart contract are just methods wrt the ``simple_storage`` variable. 

- ``transaction.wait(1)`` => Waiting for 1 block confirmation. 

.. Note:: 

	**What are block confirmations ?**
	- The act of a transaction being included on a block on the blockchain.

Testing contracts response with Brownie
----------------------------------------

- Learning how to test smart contracts and automating tests is crucial to becoming a good smart contract developper.

- **Brownie** offers the possibility to write tests directly in the `tests` folder that is initialized with the rest of the project's folders.

- When we create a test script, it should be in the test folder and should always begin with `test_`.


- The setup that we use for testing is as follwing:
	- Arranging: Setting up all the pieces that we need.
	- Acting: Deploy the smart contract and make some function calls and define the expectations (It's better to make unit tests instead of testing everything in the same script... We'll come back later to unit testing).
	- Asserting: Compare the expectation with the the actual value to be outputted.

**Example:**

.. code-block:: python

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


- Let's now try to test updating the simple_storage contract.

.. code-block:: python

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
		expected = 15
		
		# Assert
		assert expected == simple_storage.retrieve()

- When we run ``brownie test tests/test_simple_storage.py``, it will test all the functions that begin with ``test_``. There are a couple of keyboard shortcuts from some specific tasks:

	- We can test only specific functions with ``-k`` flag: 
		** Example:``brownie test -k test_update_simple_storage``

	- We can use the ``--pdb`` flag if we want to open a python shell to interact with the script and change variables etc.. to debug the script. 

	- When we have more than one function test, we cannot know which of them has successfully been tested and those who weren't. In this case, we can use ``-s`` if we want to be more robust: ``brownie test -s``. This will show us each function test result.

- All the flags and tools that are useful for testing come from ``pytest``. Hence, we can use its flags and tools in brownie easily.

Deploying to a testnet with Brownie
------------------------------------

- Brownie comes packaged with a list of networks that is compatible with. We can list all these nets by running:  ``brownie networks list``. A minimal list of networks that is provided by brownie is below:

.. code-block:: json

	Ethereum
	  ├─Mainnet (Infura): mainnet
	  ├─Ropsten (Infura): ropsten
	  ├─Rinkeby (Infura): rinkeby
	  ├─Goerli (Infura): goerli
	  └─Kovan (Infura): kovan

	Ethereum Classic
	  ├─Mainnet: etc
	  └─Kotti: kotti

	Arbitrum
	  └─Mainnet: arbitrum-main

	Avalanche
	  ├─Mainnet: avax-main
	  └─Testnet: avax-test

	Aurora
	  ├─Mainnet: aurora-main
	  └─Testnet: aurora-test

	Binance Smart Chain
	  ├─Testnet: bsc-test
	  └─Mainnet: bsc-main

	Fantom Opera
	  ├─Testnet: ftm-test
	  └─Mainnet: ftm-main

	Harmony
	  └─Mainnet (Shard 0): harmony-main

	Moonbeam
	  └─Mainnet: moonbeam-main

	Optimistic Ethereum
	  ├─Mainnet: optimism-main
	  └─Kovan: optimism-test

	Polygon
	  ├─Mainnet (Infura): polygon-main
	  └─Mumbai Testnet (Infura): polygon-test

	XDai
	  ├─Mainnet: xdai-main
	  └─Testnet: xdai-test

	Development
	  ├─Ganache-CLI: development
	  ├─Geth Dev: geth-dev
	  ├─Hardhat: hardhat
	  ├─Hardhat (Mainnet Fork): hardhat-fork
	  ├─Ganache-CLI (Mainnet Fork): mainnet-fork
	  ├─Ganache-CLI (BSC-Mainnet Fork): bsc-main-fork
	  ├─Ganache-CLI (FTM-Mainnet Fork): ftm-main-fork
	  ├─Ganache-CLI (Polygon-Mainnet Fork): polygon-main-fork
	  ├─Ganache-CLI (XDai-Mainnet Fork): xdai-main-fork
	  ├─Ganache-CLI (Avax-Mainnet Fork): avax-main-fork
	  └─Ganache-CLI (Aurora-Mainnet Fork): aurora-main-fork

- We can see that brownie already comes with different networks, the last set of nets is for development nets. BY default, when we run our scripts without specifying a specific account, brownie spins up a ganache-cli development network. But we can see that there are many other development networks that we can use. 

- Development networks are temporary networks, that is, the contracts and transactions sent on these blockchains are deleted after our script completes.

- Ethereum networks for example (Mainnet, rinkeby, kovan etc....) are persistent networks. So, brownie will keep track of anything that happens when we use a persistent network.

- If we want to work with a mainnet or a testnet (Rinkeby for example). We have to call a third-party client to run a blockchain for us like Infura or Alchemy... In this example, we will use infura. In this case, we'll have to provide the account Private key and the Project ID. 

- The private key is stored for example in the ``.env`` file, but the Project ID must be passed to the ``.env`` file in the follwing way:

.. code-block:: bash

	WEB3_INFURA_PROJECT_ID = "652sdfdfsdfv6d2ds3..."


- The following is a code-snippet for implementing a deployment to a testnet. We have created a function ``get_account()`` to easily switch between the ganache-cli and the rinkeby testnet we're gonna be using.

- To run this script with the rinkeby testnet, we should specify the netowrk when we run brownie: 

	- Example: ``brownie run scripts/deploy.py --network rinkeby``

.. code-block:: python

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

- Once we deploy to our blockchain, the deployments folder in our build directory will have a new deployment folder (The name of the folder is equal to the network_id, in the case of Rinkeby, it is 4).

- The deployments folder keeps track of deployments on testnets and mainents.


- We can now interact with our deployed contract easily. Let's define a simple function that will read from our contract.

**scripts/read_value.py**

.. code-block:: python

	from brownie import SimpleStorage, accounts, config

	def read_contract():
		
		# Get the "first" deployed contract.
		simple_Storage = SimpleStorage[0]

		# Brownie automatically knows what the ABI is 
		# and what the address of the contract is 
		# => We can directly call the functions that 
		# we need from the contract now.

		print(simple_storage.retrieve())

	def main():
		read_contract()

- Now we might want to interact very often with contracts, and running scripts this way can slow us down a bit. Brownie has another feature which is ``brownie console``. Brownie will kick us off to a console where a gnache-cli is active and where all the contracts and everything are already imported (This means that all the imports in the files that are under the **scripts** folder are imported to the console and can be used).