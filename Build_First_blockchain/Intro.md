## Description

- In the following directory, we will developp a simple todo list for the sake of learning.

	- How does a todo list work as a web app ? 
		- To access the todo list, you would use a web browser that would communicate with a web server over the Internet. The server contains all of the code and data for the todo list.

		- IN the server, you would find: Client side files in HTML, CSS, and JS, Backend code responsible for the application's business logic, and a Database that stores the tasks in the todo list.

		- This server is a centralized entity that have full control over every aspect of the application. Anyone with full access to the server can change any part of the code or the data at any time.
		
	- How does a todo list work as a blockchain app ?
	
		- A blockchain application works quite differently. All of the code and the data of the todo list does not lie on a centralized server. Instead, it is distributed across the blockchain. All of the code and the data is shared and unchangeable on the blockchain.
		
		- To access the blockchain todo list, we'll use a web browser to talk to the client side application, which will be written in HTML, CSS, and JavaScript. Instead of talking to a back end web server, the client side application will talk directly to the blockchain.

## What is a blockchain

- A blockchain is a peer-to-peer network of computers (called nodes), that talk to one another. It's a distributed network where all of the participants share the responsibility of running the network. Each network participant maintains a copy of the code and the data on the blockchain. All of this data is contained in bundles of records called "blocks" which are "chained together" to make up the blockchain. All of the nodes on the network ensure that this data is secure and unchangeable, unlike a centralized application where the code and data can be changed at any time. That's what makes the blockchain so powerful! Because the blockchain is responsible for storing data, it fundamentally is a database. And because it's a network of computers that talk to one another, it's a network. You can think of it as a network and a database all in one.

- Another fundamental distinction between traditional web applications and blockchain applications is that, instead of being a user of the application itself, you are a user of the blockhain network. The application does not manage any user data. That is the responsibility of the blockchain!

## The code on the blockchain: Smart contracts

- Smart contracts are codes that run on the blockchain and they are the building blocks of blockchain applications.

- They are written in solidity programming language

- Once we deploy a code to a blockchain, it becomes immutable. That what makes the blockchain so secure.

- They are like a microservices on the web. They are always on the blockchain, they are immutable and they execute some business logic whenever called in the same way (They are trustless).


## How our simple todo list example is going to work ?

- We're gonna connect to the app with a web browser

- We're gonna build our client side app with CSS/HTML/JS

- This client side app gonna talk directly to the blockchain and that's where gonna put our smart contracts.

**We'll use the Ethereum blockchain in this tutorial, which we can access by connecting our client side application to a single Ethereum node. We'll write a smart contract in Solidity that powers the todo list, and we'll deploy it to the Ethereum blockchain. We'll also connect to the blockchain network with our personal account using an Ethereum wallet in order to interact with the todo list application.**



























