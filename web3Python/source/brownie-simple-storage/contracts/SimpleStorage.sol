//SPDX_License_Identifier: MIT

pragma solidity ^0.6.0;

contract SimpleStorage {

	// Simply store a number an retrieve it:

	uint256 number;

	function store(uint256 _number) public {
		number = _number;
	}

	function retrieve() public view returns(uint256) {
		return number;
	}

	// Store a list of people by name and age:

	struct People {
		string name;
		uint256 age;
	}

	People[] public people;

	// Create a mapping: 
	// given the name, give me the age
	mapping(string => uint256) public nameToAge;

	// Create an addPerson function:
	function addPerson(string memory _name, uint256 _age) public {
		people.push(People(_name, _age));
		nameToAge[_name] = _age;	
	}

}