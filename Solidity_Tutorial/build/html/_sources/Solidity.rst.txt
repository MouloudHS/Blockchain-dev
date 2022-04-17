Introduction to Solidity
++++++++++++++++++++++++

What is Solidity ?
-------------------

- Solidity is an object-oriented, high-level language for implementing smart contracts. Smart contracts are programs which govern the behaviour of accounts within the Ethereum state.

Quick intro to coding with solidity
-----------------------------------

- **This will be a quick intro to coding with solidity before we jump to more complicated things**. 

- A program in solidity always begins with ``pragma solidity`` and then the version of solidity we're going to use.

* Example:

	* ``pragma solidity >=0.6.0 <0.9.0``; to say that the solidity version we are using is a version between 0.6.0 and 0.9.0 so we can use any compiler in this range.

	* ``pragma solidity ^0.6``; to say that we are using any 0.6 version (0.6.0 --> 0.7.0)

- The fundamental entity in any solidity program is the `contract`. It is somehow similar to a class in any object-oriented programming language. 

- Any solidity statement is ended by semi-column (;)


* Complete example 

.. code-block:: solidity

	pragma solidity >=0.6.0 <0.9.0;
	// This is a comment
	
	contract First_Example {

	}

Basic Variable types
====================

* In solidity, the basic variable types that are very common to any programming language are: ``uint`` ``int`` ``bool`` ``string`` 
* There are other types that are specific to solidity like:
	* ``address``: An Ethereum Wallet adress for example
	* ``bytes32``: any value passed here will be converted to bytes with 32 bits (Max allowed is 32 bits... we also have ``bytesN`` with N can be any number below 32)

* Complete example

.. code-block:: solidity

	pragma solidity >=0.6.0 <0.9.0;
	
	
	contract Example {
	
		uint256 favoriteNumber = 5; // integer of size 256 bits which is the most commonly used
		bool favoriteBool = true;   // boolean
		string favString = "String";
		int256 favInt = -5;
		address favAdress = 0x44Ee91Bded46d0B5B13845124ca949F4f048Ed64; // My testNet Ethereum wallet address 
		bytes32 favBytes = "cat"; // It will be stored as bytes32 
	}


.. note::
	* If we don't initialize our variables, they get automatically initialized to their corresponding null value (0 for integers for example).
	
	* If we want our variable to be visualized outside of the code, we can use the keyword ``public``: 
		* Example: ``uint256 public Nbr = 5;``

Using Functions
===============

- We will start this section by giving two examples. We will create a function that stores a number inside a ``uint256`` variable and hence changing its value, and another that retrieves it.

- In **Solidity**, a function is created using the keyword ``function``. This function can be either *public*, *private* or other types that we'll talk about later.

.. code-block:: solidity

	pragma solidity >=0.6.0 <0.9.0;
	
	contract Example {
		uint256 favNumber;
		
		// We will store a new "uint256" inside of a previously created variable called favNumber 
		function store(uint256 _newNumber) public {
			favNumber = _newNumber;
		}
	}


.. note::
	* Since favNumber has been created in the contract, it has it's scope and can hence be used anywhere in the code. Otherwise, if a variable is defined inside of a function, it has the scope of that particular function and cannot be used outside of it.

- Now we will complete our code with a ``function`` that retireves the updated number and renders it. 
	* This function needs to **return** something and that is why we will use the keyword ``returns``.
	* There is 2 keywords in solidity that define functions and overwhich we don't have to make a transaction and these keywords are ``view`` and ``pure``.     
	* We use ``view`` keyword when we want to read a state of the blockchain (A public variable is hence also a ``view`` function)
	* We use ``pure`` keyword when we want to perform pure maths whitout saving any particular state.

.. code-block:: solidity

	pragma solidity >=0.6.0 <0.9.0;
	
	contract Example {
	
		uint256 favNumber;
		
		function store(uint256 _newNumber) public {
			favNumber = _newNumber;
		}

		function retrieve() public view returns(uint256) {
			return favNumber;
		}
	}

Using Structs
=============

- ``structs`` are used to create new structures (or types or data types ...) in **solidity**.
- Suppose we want to create a ``structure`` called **People** where we store any persons's name and age. The example below illustrated how we can do this.

.. code-block:: solidity

	pragma solidity >=0.6.0 <0.9.0;
	
	contract Example {

	uint256 dummy_number;
		
	struct People {
		string name; // First index in the People struct
		uint256 age; // Second index in the People struct
	}
	
	// Now we can create a new variable using the "datatype" or the structure we created
	People public person = People({name:"Chaimae Baraki", age:25}) 
	
	}


.. note:: 

	* **Solidity** indexes its variables wrt to the order of their appearance in the code and their scope.
		- `dummy_number` in the previous code snippet for example has index 0
		- name and age have respectively indices 0 and 1 in their `People` structure



Using Arrays
============

- When we used the People ``struct`` as an example, we were able to create a *person* type that contains the name and the age of a given person but nothing more. That is, if we want to create for example, a list of people, we cannot do it using ``struct``. This is where the ``array`` type comes into place. An ``array`` is created using a ``struct``. In the example below we will create an array **people** that can contain any number of persons inside it.


.. code-block:: solidity
	
	pragma solidity >=0.6.0 <0.9.0;
	
	contract Example {
	
	struct People {
		string name;
		uint256 age;
	}
	
	People[] public people; // Creating a public array called people
	}
	
- What we want to do now is filling this array. For this we will create a ``function`` **addPerson** and ``push`` the created **person** to the array inside it. 
	
.. code-block:: solidity
	
	pragma solidity >=0.6.0 <0.9.0;
	
	contract Example {
	
	struct People {
		string name;
		uint256 age;
	}
	
	People[] public people; 
	
	function addPerson(string memory _name, uint256 _age) public {
		people.push(People({name:_name, age:_age}));
		// or people.push(People({name:_name, age:_age})); (by index)
	}
	
	}
	
.. note::

	- When we crate an array using empty [ ], the array can have any size and contain any number of entries --> **It is dynamic**
	- If we want an array to contain only **N** entries we simply pass **N** to the array: People[N] = A people array with no more than 2 entries (a size 2 array). 
	
	
.. note::

	- ``memory`` keyword: In solidity, there is 2 ways to store information, we can store it in memory or in storage; When we store an object in memory, this means that it will only be stored during execution of the function. If we hold the object in storage, that piece of data will persist even after the function executes. A string in solidity is actually an object, **it is an array of bytes** and hence we have to decide whether to store it in memory or in storage. Since we need the string "_name" only during the function execution, we can have it stored in memory and when it is passed to the People array, we are guaranteed that it will be stored there forever (and hence in storage). To summarize;
		- memory = delete the variable after exectuion
		- storage =  keep it forever.
		
Using mappings
==============

- In the previous code snippet, we've created an array that can contain any number of people (dynamic array) stored by their name and age. But what if we want to know for example the age of a person given its name ? This is possible through another datastrucuture called **mappings**.

- Mappings are dictionnary like datastructures that are used to map an object to another object or value.

- In the code snippet below, we will create a dynamic People array, and a mapping of the age of each person by its name:

.. code-block:: solidity

	pragma solidity >=0.6.0 <0.9.0;
	
	contract Example {
	
		struct People {
			string name;
			uint256 age; 
		}
		
		People[] public people;
		
		// We create a mapping of the name to the age:
		mapping(string => uint256) public nameToAge;
		
		
		function addPerson(string memory _name, uint256 _age) public {
			people.push(People({name:_name, age:_age}));
			nameToAge[_name] = _age;						
		}
	}	

		
.. WARNING:: 

	**- SPDX licence identifier**: Trust in smart contract can be better established if their source code is available. Since making source code available always touches on legal problems with regards to copyright, the Solidity compiler encouranges the use of machine-readable SPDX license identifiers. Every source file should start with a comment indicating its license: **// SPDX-License-Identifier: MIT** (It means that, *Hey, everybody can use this code and, we don't care*)
	
.. note::

	- When working with **REMIX IDE**, we developp smart contracts using the javascript VM. This way, we are provided with 100 ETH test tokens for testing and deployment and so on. If we want to deploy our smart contracts to let others interact with it, then, in remix, we switch to injected web3. This way, Metamask will popup asking for authorization to use either the testnet (Rinkeby faucet for example) or the mainnet (The real account). Injected WEB3 actually means that we are taking metamask and injecting it into the source code of the browser. This means that our WEB3 provider is metamask in this case. If we want to use another web3 provider than, there is another option to do so in REMIX.
	
	
Storage Factory Example
-----------------------

Implemeting the storage factory
===============================

- Let's say now that we want to execute a contract from another contract that is written in another file. For this we use import. To illustrate this, we're gonna create a simple storage smart contract to store people by name and age and map their names to their ages and then create another contract that executes this contract.

* Simple storage contract

.. code-block:: solidity

	pragma solidity >=0.6.0 <0.9.0;
	
	contract SimpleStorage {
		
		// We will define two functions for later use
		// one to store a number and one to retrieve it
		
		uint256 favNumber;
		
		function store(uint256 _number) public {
			favNumber = _number;
		}
		
		function retrieve() public view returns(uint256) {
			return favNumber;
		}
		
		struct People {
			string name;
			uint age;			
		}
		
		People[] public people;
		mapping(string => uint256) public nameToAge;
		
		function addPerson(string memory _name, uint256 _age) public {
			people.push(People({name:_name, age:_age}));
			nameToAge[_name] = _age;
		}
	}

- This smart contract is saved to a file called SimpleStorage.sol
	
- Now we're gonna create another smart contract. In this smart contract, we're gonna simply import our SimpleStorage smart contract.

.. code-block:: solidity

	pragma solidity >=0.6.0 <0.9.0;
	
	import "./SimpleStorage.sol";

	contract StorageFactory {

	}

- This way, we can see in REMIX that we can either deploy the imported smart contract (SimpleStorage) or the empty one (StorageFactory).

- What we wanna do is deploying the SimpleStorage smart contract from the StorageFactory smart contract. Hence, we have to create a function for that.

.. code-block:: solidity

	pragma solidity >=0.6.0 <0.9.0;
	
	import "./SimpleStorage.sol";

	contract StorageFactory {
		function createSimpleStorageContract() public {
			// We define a new variable of type SimpleStorage contract with a name (for example simpleStorage):
			SimpleStorage simpleStorage = new SimpleStorage();
		}
	}

- Using these few lines of code, we are able to deploy a smart contract from another smart contract. The only remaining issue is that, using REMIX IDE for example with a javascript VM will show us that the contracts have been created and deployed but we can't really read where those contracts are being created (Unlike if we we're using a real network or a testnet, in this case, we can see our contracts on etherscan). To keep track of the SimpleStorage contract that we've deployed, we can use an array..



.. code-block:: solidity

	//SPDX-License-Identifier: MIT
	pragma solidity >=0.6.0 <0.9.0;

	import "./SimpleStorage.sol";

	contract StorageFactory {
		
		// To keep track of created contracts
		// using REMIX IDE VM
		SimpleStorage[] public simpleStorageArray;
		
		function createSimpleStorageContract() public {
			// We define a new variable of type SimpleStorage contract with a name (for example simpleStorage):
			SimpleStorage simpleStorage = new SimpleStorage();
		
			// To keep track of created contracts
			// using REMIX IDE VM
			simpleStorageArray.push(simpleStorage);
		}	
	}

- If we run this code snippet in a REMIX IDE with a JavaScript VM environement for example, we're gonna get for each smart contract created by the `createSimpleStorageContract` an adress that the corresponding contract was deployed to. This way, we deployed a contract to the blockchain from another contract.

.. note::

	- We should always think of starting our code with a license identifier : **SPDX-License-Identifier: MIT**
	
- What we want to do in the next step is to call the function that are defined in the internal contract from the new contract. To achieve this, we have to create functions in our new contract to call other functions that are originally defined in the contract deployed contract. 

.. HINT::

	- To interact with a contract, we need two things; the adress of the contract we want to interact with and the ABI (Application Binary Interface).
	- Since we are storing our deployed contracts in an array, each contract can be pointed to by its index in the array and we can interact with it through its adress.

.. code-block:: solidity

	// SPDX-License-Identifier: MIT

	pragma solidity ^0.6.0;

	import "./SimpleStorage.sol";

	contract StorageFactory {

		SimpleStorage[] public simpleStorageArray;

		function createSimpleStorageContract() public {
			SimpleStorage simpleStorage = new SimpleStorage();
			simpleStorageArray.push(simpleStorage);
		}

		// Function to call Store function of SimpleStorage
		// we need to pass an index to point to a deployed contract in 		
		// the array where all deployed contracts are (simpleStorageArray)
		// We will also pass a number to be stored as required by
		// the SimpleStorage store function
		function sfStore(uint256 _simpleStorageIndex, uint256 _simpleStorageNumber) public {
			// We can get the adress of a contract through the
			// function adress(your_contract)
			// We create simpleStorage object that we can use to
			// call any function in the SimpleStorage contract	
			SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));	
			simpleStorage.store(_simpleStorageNumber);
		}

		function sfRetrieve(uint256 _simpleStorageIndex) public view returns(uint256) {
			SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
			return simpleStorage.retrieve();
		}
	}

Inheritance
===========

- So far, all looks good, but what if we had too many functions inside SimpleStorage contract and we wanted to use all of them inside our StorageFactory ? 

- Inheritance solves this problem: StorageFactory can inherit all the functions of SimpleStorage.

- In solidity, we simply define our StorageFactory to be of "contract" SimpleStorage. (similar to saying of "type" or of "class" in any other programming language). To do so, we use **is** ``contract StorageFactory is SimpleStorage { // lines-of-code; }``. This is enough to have all the functions that are defined in SimpleStorage imported in the StorageFactory and ready to be used.

- The code becomes;

.. code-block:: solidity

	// SPDX-License-Identifier: MIT

	pragma solidity ^0.6.0;

	import "./SimpleStorage.sol";

	contract StorageFactory is SimpleStorage{

		SimpleStorage[] public simpleStorageArray;

		function createSimpleStorageContract() public {
			SimpleStorage simpleStorage = new SimpleStorage();
			simpleStorageArray.push(simpleStorage);
		}

		// Function to call Store function of SimpleStorage
		// we need to pass an index to point to a deployed contract in 		
		// the array where all deployed contracts are (simpleStorageArray)
		// We will also pass a number to be stored as required by
		// the SimpleStorage store function
		function sfStore(uint256 _simpleStorageIndex, uint256 _simpleStorageNumber) public {
			// We can get the adress of a contract through the
			// function adress(your_contract)
			// We create simpleStorage object that we can use to
			// call any function in the SimpleStorage contract	
			SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));	
			simpleStorage.store(_simpleStorageNumber);
		}

		function sfRetrieve(uint256 _simpleStorageIndex) public view returns(uint256) {
			SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
			return simpleStorage.retrieve();

		}

	}

- **That was all for the storage example.**

Fund Me
-------

A simple function to fund your smart contract
=============================================

- In case we want to create payable functions, we should use the keyword ``payable``.

- The code below is a simple implementation of a payable function.

.. code-block:: solidity

	// SPDX-Licence-Identifier: MIT

	pragma solidity ^0.6.0;

	contract FundMe {

		function fund() public payable {
		}
	}

- Let's say for example that we want to keep track of who sent us funding using this contract: To do so, we can create a mapping between adresses and value.

.. code-block:: solidity

	// SPDX-Licence-Identifier: MIT

	pragma solidity ^0.6.0;

	contract FundMe {

		mapping(address => uint256) public adressToAmountFunded;
		function fund() public payable {
			// msg.sender is the sender of the function call.
			// msg.value is how much they sent.
		    // += to cumulate the amounts sent
		    adressToAmountFunded[msg.sender] += msg.value;
		}
	}

Getting external data with chainlink
====================================

- Blockchains being deterministic systems, we may encounter a slight problem. Let's say that we want for example to receive our funds in USDT or any other currency instead of Ether. What we need is a conversion rate between Ether and this whatever currency. However, blockchains by themselves cannot interact with the real world and this is where oracles come into place.

.. note::
	- Smart contracts are unable to connect with external systems, data feeds, APIs, existing payment systems or any other off-chain ressources on their own and cannot do external computations which makes them deterministic systems (wall garded).
	
- There are two types of oracles, centralized oracles and decentralized oracles (like chainlink). If we count on centralized oracles to provide us with necessary data (like currency conversion rates), we will be going to ruin all the decentrality as if this centralized entity decides to stop feeding the smart contract with data, then, all our work will go to waste. The purpose of blockchain is that not a single entity can restict our freedom to interact with each other.

.. note::
- CHAINLINK is a modular oracle network that allows us to get data and do external computation in a highly sybil-resistant decentralized manner.

- Let's **Get the latest price feed**. We can use chainlink's ``get latest price feed`` contract (`Get latest price <https://docs.chain.link/docs/get-the-latest-price/>`_).

- There is a Remix button that takes us directly to REMIX IDE. 
- When following the previous link, we get to see a foler created in REMIX with the following code and other things as well:

.. code-block:: solidity

	// SPDX-License-Identifier: MIT
	pragma solidity ^0.8.7;

	import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

	contract PriceConsumerV3 {

		AggregatorV3Interface internal priceFeed;

		/**
		 * Network: Kovan
		 * Aggregator: ETH/USD
		 * Address: 0x9326BFA02ADD2366b30bacB125260Af641031331
		 */
		constructor() {
		    priceFeed = AggregatorV3Interface(0x9326BFA02ADD2366b30bacB125260Af641031331);
		}

		/**
		 * Returns the latest price
		 */
		function getLatestPrice() public view returns (int) {
		    (
		        /*uint80 roundID*/, // Defines how many times this price was updated
		        int price, // The actual conversion rate
		        /*uint startedAt*/, // Defines where this was last updated
		        /*uint timeStamp*/,
		        /*uint80 answeredInRound*/
		    ) = priceFeed.latestRoundData();
		    return price;
		}
	}

- As we can see, this contract requires a kovan faucet so in REMIX IDE, we should switch to injected web3 in order to use this contract and we should make sure that our connected wallet from metamask is a kovan testnet wallet.

- Once we deploy this, we can have live conversion rates through ``get_latest_price`` function of this contract. 

- The reason why we cannot use a local network (simulated VM) and we use testnets is that, in a testnet, there is a network of nodes looking at this testnet and delivering data onto this testnet unlike in a simulated VM where there are no nodes. (However, we should note that there are ways to mock these interactions and mock a chainlink node returning data onto our blockchain.)


- **In order to incorporate this ethusd conversion rate datafeed into our code**, we have to import the chainlink **eth-usd** datafeed from the npm package ``@chainlink/contracts``:
		
		- Syntaxe: 	``import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface"``
		
- As we can see, the imported is actually an interfaceand not a contract. To learn about interfaces, we will copy paste the interface code ``AggregatorV3Interface.sol`` from the github repository rather than simply importing it in a one line of code.
	

Working with interfaces 
------------------------

- The following is an example of an interface, this is ``AggregatorV3Interface.sol`` interface. 

.. code-block:: solidity

	// SPDX-License-Identifier: MIT
	pragma solidity ^0.8.0;

	interface AggregatorV3Interface {
	  function decimals() external view returns (uint8);

	  function description() external view returns (string memory);

	  function version() external view returns (uint256);

	  // getRoundData and latestRoundData should both raise "No data present"
	  // if they do not have data to report, instead of returning unset values
	  // which could be misinterpreted as actual reported values.
	  function getRoundData(uint80 _roundId)
		external
		view
		returns (
		  uint80 roundId,
		  int256 answer,
		  uint256 startedAt,
		  uint256 updatedAt,
		  uint80 answeredInRound
		);

	  function latestRoundData()
		external
		view
		returns (
		  uint80 roundId,
		  int256 answer,
		  uint256 startedAt,
		  uint256 updatedAt,
		  uint80 answeredInRound
		);
	}

.. note::

	- An interface starts with ``interface`` keyword rather than ``contract``. 

	- They are a minimalistic view into another contract and have function declarations and their return types only. They are similar to header files in C.
	
	- Interfaces generally contains empty "external" functions that we can call from another contract.

	- Solidity doesn't natively understands how to interact with another contract. We have to tell Solidity what functions can be called on another contract.
	
	- Interface compile down to ABI (Application binary interface). The ABI tells solidity what functions can be called on another contract. 
	
	- Anytime we need to interact with an **already deployed contract**, we need that contract's ABI to do so.

- In the following example, we're going to interact, from a contract, with the previously defined interface.

.. code-block:: solidity

	// SPDX-License-Identifier: MIT
	pragma solidity ^0.8.0;

	interface AggregatorV3Interface {
		function decimals() external view returns (uint8);

		function description() external view returns (string memory);

		function version() external view returns (uint256);

		// getRoundData and latestRoundData should both raise "No data present"
		// if they do not have data to report, instead of returning unset values
		// which could be misinterpreted as actual reported values.
		function getRoundData(uint80 _roundId)
		external
		view
		returns (
		    uint80 roundId,
		    int256 answer,
		    uint256 startedAt,
		    uint256 updatedAt,
		    uint80 answeredInRound
		);

		function latestRoundData()
		external
		view
		returns (
		    uint80 roundId,
		    int256 answer, // latest price
		    uint256 startedAt,
		    uint256 updatedAt,
		    uint80 answeredInRound
		);
	}

	contract FundMe {
		
		
		mapping(address => uint256) public addressToAmountFunded;
		function fund() public payable {
		    addressToAmountFunded[msg.sender] += msg.value;
		}    

		// Calling "version" function "referenced ?" in the
		// interface (and hence already alive in a deployed smart 
		// contract that is going to provide us with the eth/usd 
		// conversion rate) inside the contract.
		function getVersion() public view returns(uint256) {
		    
		    // Same as arrays, structs etc: ...
		    // It's like defining a type
		    // public isn't necessary here as we already are in
		    // a public function
		    // We're gonna use rinkeby testnet in this example
		    // the address that we're going to pass to AggregatorV3Interface
		    // is a rinkeby testnet eth/usd pricefeed address  
		        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
		        return priceFeed.version();
		}
		
		// Let's create now a function called getPrice to get the latest price 
		// of ETH in usd, that is the eth/usd conversion rate.
		// This time, the latestRoundData function returns a tuple (See the note 
		// below the code snippet)
		function getPrice() public view returns(uint256) { 
		    AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
		    (   
		    uint80 roundId, 
		    int256 answer, 
		    uint256 startedAt,
		    uint256 updatedAt, 
		    uint80 answeredInRound 
		    ) = priceFeed.latestRoundData();

		    // Since answer is int256, we will do a typecasting to get over the 
		    // compiling error saying that we cannot return uint256 since 
		    // answer is int256 
		    return uint256(answer);

		    /* Note: there are alot of unused variables (roundId etc....) which causes
		    compiling errors... In order to be able to compile correctly, one has to 
		    use a slighlty different syntax, namely, we can simply return blanks for
		    each unused variable:
		    (,int256 answer,,,) = priceFeed.latestRoundData();
		    */ 
		}

		}

.. note::

	- A tuple is, in solidity, a list of objects that are potentially of different types. To define tuples, we use brackets.
	
- To wrap this up, and since we learned now how to deal with interfaces, we can clean our code a bit to look much nicer by simply importing the AggregatorV3Interface from chainlink npm package and ignoring the unused vars in the latestRoundData() method. The code will look like this:

.. code-block:: solidity

	// SPDX-License-Identifier: MIT
	pragma solidity ^0.8.0;

	import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

	contract FundMe {

		mapping(address => uint256) public amountToaddress;
		function fund() public payable {
		    amountToaddress[msg.sender] += msg.value;
		}

		function getPrice() public view returns(uint256) {
		    AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
		    (,int256 answer,,,) = priceFeed.latestRoundData();
		    return uint256(answer);
		}
	}

Matching units
---------------

- When we work with smart contracts, we generally encounter some issues regarding the units when we do some conversions. That being said, it's preferable to work with units of ether like **Wei** and **Gwei**. In the last contract for example, we may want to multiply our answer by a power of 10 so that we make sure to always have 18 decimal places. (4,5454,4554 -> 4,5454,4554 * 1,0000,0000,00 = 4,5454,4554,0000,0000,00 => (18 decimal places) which is 4.5 ether in wei (divide by 10^18 and you'll get it)).

- Let's define a ``getConversionRate()`` function. 

.. code-block:: solidity

	// SPDX-License-Identifier: MIT
	pragma solidity ^0.8.0;

	import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

	contract FundMe {

		mapping(address => uint256) public amountToaddress;
		function fund() public payable {
		    amountToaddress[msg.sender] += msg.value;
		}

		function getPrice() public view returns(uint256) {
		    AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
		    (,int256 answer,,,) = priceFeed.latestRoundData();
		    return uint256(answer * 10000000000);
		}

		function getConversionRate(uint256 ethAmount) public view returns(uint256) {
		    // get Eth price:
		    uint256 ethPrice = getPrice();
		    // Convert **without forgetting to match all units
		    // with wei [ Divide by 10^18 (10^8 from 
		    // ethAmount and 10^10 from ethPrice) ]**
		    uint256 ethAmountToUSD = (ethPrice*ethAmount)/1000000000000000000;
		    
		    return ethAmountToUSD;
		}
	}

.. WARNING::

	- Solidity has a pitfall when it comes to maths. For example, a uint8 has as maximum 255, if we define a uint8 that is equal to 255 + 1, Solidity will wrap around once we reach the maximum cap, so we get: 255 + 1 = 0, 255 + 55 = 54 and so on... which is actually wrong. This is what we call overflow in solidity and we should really be careful with it.
	
.. note::

	- There is a library in chainlink called **SafeMathChainlink.sol** that implements some math operations to be used to render warning messages when we encounter overflows. It should be used very often. However, Starting from Solidity v0.8, we no longer need SafeMath packages.


- In the example below, we use Chainlink's SafeMath library for uint256 varibale types only:
	
.. code-block:: solidity

	// SPDX-License-Identifier: MIT
	pragma solidity ^0.6.0;

	import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

	import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

	contract FundMe {
		
		using SafeMathChainlink for uint256;
		mapping(address => uint256) public amountToaddress;
		function fund() public payable {
		    amountToaddress[msg.sender] += msg.value;
		}

		function getPrice() public view returns(uint256) {
		    AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
		    (,int256 answer,,,) = priceFeed.latestRoundData();
		    return uint256(answer * 10000000000);
		}

		function getConversionRate(uint256 ethAmount) public view returns(uint256) {

		    uint256 ethPrice = getPrice();
		    uint256 ethAmountToUSD = (ethPrice*ethAmount)/1000000000000000000;
		    
		    return ethAmountToUSD;
		}
	}
		
.. note::

	- The directive ``using A for B`` can be used to attach library functions (from the library A) to any type (B) in the context of a contract.

Thresholding
------------

- Let's set a threshold to the amount of Eth the sender sends us through this contract.

- In order to do so, we have 2 options; 
	- Use ``require`` keyword which is highly recommended: ``if (getConversionRate(msg.value) < minUSD) { revert? };``
	
	- Use ``if - revert``: 	``require(getConversionRate(msg.value) >= minUSD);``
	
- These 2 lines are equivalent, they both stop the contract from executing if the requirement isn't satisfied and revert the transaction => The user is going to receive his money back as well as any unspent gas.

- We can add a revert error message: ``require(getConversionRate(msg.value) >= minUSD, "You need to spend more ETH !");``

.. code-block:: solidity

	// SPDX-License-Identifier: MIT
	pragma solidity ^0.6.0;

	import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

	import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

	contract FundMe {
		
		using SafeMathChainlink for uint256;
		
		mapping(address => uint256) public amountToaddress;
		function fund() public payable {
		    uint256 minUSD = 50 * 10**18;
		    require(getConversionRate(msg.value) >= minUSD, "You need to spend at least 50 dollars in ETH !");
		    amountToaddress[msg.sender] += msg.value;
		}

		function getPrice() public view returns(uint256) {
		    AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
		    (,int256 answer,,,) = priceFeed.latestRoundData();
		    return uint256(answer * 10000000000);
		}

		function getConversionRate(uint256 ethAmount) public view returns(uint256) {

		    uint256 ethPrice = getPrice();
		    uint256 ethAmountToUSD = (ethPrice*ethAmount)/1000000000000000000;
		    
		    return ethAmountToUSD;
		}
	}

- We can also add a function to withdraw the funds which is also a ``payable`` function. The keywords and functions that we are going to need are:

	- ``transfer()``: a method to transfer funds between two addresses.
	- ``this`` to refer to the current contract.
	- ``balance`` attribute to see the balance in ether of a contract. (In this example, we are going to withdraw all of the contract's funds hence the ``balance`` attribute.)
	
	- Putting everything together: ``msg.sender.transfer(address(this).balance)``-- This line of code means; **whoever is calling the withdraw method (which is msg.sender), transfer them all of the contract's code.**
		
.. code-block:: solidity

	// SPDX-License-Identifier: MIT
	pragma solidity ^0.6.0;

	import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

	import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

	contract FundMe {
		
		using SafeMathChainlink for uint256;
		
		mapping(address => uint256) public amountToaddress;
		function fund() public payable {
		    uint256 minUSD = 50 * 10**18;
		    require(getConversionRate(msg.value) >= minUSD, "You need to spend at least 50 dollars in ETH !");
		    amountToaddress[msg.sender] += msg.value;
		}

		function getPrice() public view returns(uint256) {
		    AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
		    (,int256 answer,,,) = priceFeed.latestRoundData();
		    return uint256(answer * 10000000000);
		}

		function getConversionRate(uint256 ethAmount) public view returns(uint256) {

		    uint256 ethPrice = getPrice();
		    uint256 ethAmountToUSD = (ethPrice*ethAmount)/1000000000000000000;
		    
		    return ethAmountToUSD;
		}

		function withdraw() public payable {
		    msg.sender.transfer(address(this).balance);

		}
	}

Ownership 
----------

- It is a **very bad idea** to define a contract with a public withdrawal function. Only the owner should be able to withdraw funds from a smart contract. We hence have to declare an "owner".

- In order to declare an owner to this smart contract, we maybe have to create a ``createOwner`` function to do the trick for us. However, this function can be called once the contract is deployed, so, if someone calls this function before we do once it is deployed, we are no longer the owners. Therefore, we need some sort of function that executes once the contract is deployed, and that's what a ``contructor`` is ! It is what constructs the smart contruct.

- We can hence, declare a variable called ``owner``, and use the constructor to define the owner to be us, thus, ``msg.sender`` as **the first** ``msg.sender`` is whoever deployed the contract which in this case is us.

- Once we define the owner, we can set a requirement through ``require()`` in the withdraw function.


.. code-block:: solidity

	// SPDX-License-Identifier: MIT
	pragma solidity ^0.6.0;

	import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

	import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

	contract FundMe {
		
		using SafeMathChainlink for uint256;
		
		mapping(address => uint256) public amountToaddress;
		address public owner;

		constructor() public {
		    owner = msg.sender;
		}


		function fund() public payable {
		    uint256 minUSD = 50 * 10**18;
		    require(getConversionRate(msg.value) >= minUSD, "You need to spend at least 50 dollars in ETH !");
		    amountToaddress[msg.sender] += msg.value;
		}

		function getPrice() public view returns(uint256) {
		    AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
		    (,int256 answer,,,) = priceFeed.latestRoundData();
		    return uint256(answer * 10000000000);
		}

		function getConversionRate(uint256 ethAmount) public view returns(uint256) {

		    uint256 ethPrice = getPrice();
		    uint256 ethAmountToUSD = (ethPrice*ethAmount)/1000000000000000000;
		    
		    return ethAmountToUSD;
		}

		function withdraw() public payable {
		    require(msg.sender == owner);
		    msg.sender.transfer(address(this).balance);

		}
	}

Modifiers and resetting
-----------------------

- Let's say we have many contracts to be run and many functions that are only for the owner to use. Do we have to repeat this require statement each time ? The answer is no, but instead we can use a ``modifier``.

.. note::

	- A modifier is used to change the behavior of a function in a declarative way.

- In the example below, we are going to modify our last code to use a modifier:

.. code-block:: solidity

	// SPDX-License-Identifier: MIT
	pragma solidity ^0.6.0;

	import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

	import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

	contract FundMe {
		
		using SafeMathChainlink for uint256;
		
		mapping(address => uint256) public amountToaddress;
		address public owner;

		constructor() public {
		    owner = msg.sender;
		}


		function fund() public payable {
		    uint256 minUSD = 50 * 10**18;
		    require(getConversionRate(msg.value) >= minUSD, "You need to spend at least 50 dollars in ETH !");
		    amountToaddress[msg.sender] += msg.value;
		}

		function getPrice() public view returns(uint256) {
		    AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
		    (,int256 answer,,,) = priceFeed.latestRoundData();
		    return uint256(answer * 10000000000);
		}

		function getConversionRate(uint256 ethAmount) public view returns(uint256) {

		    uint256 ethPrice = getPrice();
		    uint256 ethAmountToUSD = (ethPrice*ethAmount)/1000000000000000000;
		    
		    return ethAmountToUSD;
		}


		modifier onlyOwner {
			require(msg.sender == owner);
			-;
		}
		function withdraw() public onlyOwner payable {
		    msg.sender.transfer(address(this).balance);

		}
	}



.. note::

	- The code says; before you run the withdraw function, do the **onlyOwner** statement first, and then, wherever you have ``-;`` in the ``modifer`` you can run the rest of the code. 

.. code-block:: solidity

	// SPDX-License-Identifier: MIT
	pragma solidity ^0.6.0;

	import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

	import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

	contract FundMe {
		
		using SafeMathChainlink for uint256;
		
		mapping(address => uint256) public amountToaddress;
		address public owner;

		constructor() public {
		    owner = msg.sender;
		}


		function fund() public payable {
		    uint256 minUSD = 50 * 10**18;
		    require(getConversionRate(msg.value) >= minUSD, "You need to spend at least 50 dollars in ETH !");
		    amountToaddress[msg.sender] += msg.value;
		}

		function getPrice() public view returns(uint256) {
		    AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
		    (,int256 answer,,,) = priceFeed.latestRoundData();
		    return uint256(answer * 10000000000);
		}

		function getConversionRate(uint256 ethAmount) public view returns(uint256) {

		    uint256 ethPrice = getPrice();
		    uint256 ethAmountToUSD = (ethPrice*ethAmount)/1000000000000000000;
		    
		    return ethAmountToUSD;
		}


		modifier onlyOwner {
			require(msg.sender == owner);
			_;
		}
		function withdraw() public onlyOwner payable {
		    msg.sender.transfer(address(this).balance);
		}
	}

- One thing that is missing in this contract is the balance **resetting**. When we withdraw funds from this contract, we should also update the funders' sent amounts. For that;

	+ We first create an array of addresses (called funders for example) to keep track of which addresses funded the smart contract.

	+ When we withdraw the funds that are in the smart contract (defined by its address) to the owner's wallet (defined by the address passed to the constructor which is also the first address in the funders array), we must reset all the "balances" to zero. To achieve this, we have to loop over all the addresses in the funders array and set their balances to zero.
	
.. code-block:: solidity

	// SPDX-License-Identifier: MIT
	pragma solidity ^0.6.0;

	import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

	import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

	contract FundMe {
		
		using SafeMathChainlink for uint256;
		
		mapping(address => uint256) public amountToaddress;
		address[] public funders;
		address public owner;

		constructor() public {
		    owner = msg.sender;
		}


		function fund() public payable {
		    uint256 minUSD = 50 * 10**18;
		    require(getConversionRate(msg.value) >= minUSD, "You need to spend at least 50 dollars in ETH !");
		    amountToaddress[msg.sender] += msg.value;
            funders.push(msg.sender);
        }

		function getPrice() public view returns(uint256) {
		    AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
		    (,int256 answer,,,) = priceFeed.latestRoundData();
		    return uint256(answer * 10000000000);
		}

		function getConversionRate(uint256 ethAmount) public view returns(uint256) {

		    uint256 ethPrice = getPrice();
		    uint256 ethAmountToUSD = (ethPrice*ethAmount)/1000000000000000000;
		    
		    return ethAmountToUSD;
		}


		modifier onlyOwner {
			require(msg.sender == owner);
			_;
		}
		function withdraw() public onlyOwner payable {
		    msg.sender.transfer(address(this).balance);
            for(uint256 fundersIndex = 0; fundersIndex <= funders.length; fundersIndex++) {
                address funder = funders[fundersIndex];
                amountToaddress[funder] = 0;
            
            funders = new address[](0); // reset the funders array to an empty array of addresses
            }
        
        }
	}

Conclusion
-------------
