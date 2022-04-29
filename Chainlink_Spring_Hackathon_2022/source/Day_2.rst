Purpose of smart contracts
==========================

- Smart contracts are 
	- trust minimized agreements. 
	- Unbreakable promises thanks to decentralization. 
	- Superior digital agreements.

- In all our agreements today, we have this issues of trust and promises (services like bankds, lottery etc...).

- Examples of parties that broke their promises:
	
	- McDonald monopoly game to win 1M$ (No one won..)
	- Robinhood exchange stops users from trading GameStop stocks.
	
.. NOTE::
	
	**Smart contracts will solve Solciety's critical trust issues**
 	- What smart contracts do is that they move us away from this paper guarantees (brand based world) where: 
 		- Counterparty risk is high and opaque.
 		- Transparency is purposefully removed.
 		- Interest yields are low and going lower.
 		
 	to a world where we have CryptoGraphic guanrantees (Math based) where:
 		- Counterparty risk is low and transparent
 		- Transparency is unavoidably built-in
 		- interest yields are consistently high
 	
 	Smart contracts replaces trust by mathematical truth.
 	
 	*Counterparty risk: The likelihood that one of those involved in a transaction might default on its contractual obligation*

Purpose of Chainlink
====================

Reminder about blockchains
---------------------------

- Blockchains are deterministic systems and this means that they cannot connect ot the outside world natively. **Why? = Consensus**

- **What is consensus ?**: Blockchains are comprised of many nodes all around the globe and they have to agree on every calculation that they run and on the state of the blockchain, i.e. They have to reach consensus on what the state of the blockchain is.

- In order for blockchains to have more real world applications, it has to collect and use real world data. However, when a blockchain start interacting with an external API, it's no longer deterministic. 

	- Why is it no longer deterministic ?: Let's say for example that we need to to perform a simple calculation (1 + 1 = 2). It's easy for all the nodes (let's say there are 3 nodes in the blockchain) to agree on that and hence reaching consensus. Let's take now another example where the blockchain is connected to an external API (a data source outside of the system). Let's say that this API is providing ETH/USD conversion rate data. Cryptocurrency prices may be volatile, so let's say that a certain node among the three other nodes sends a request to the API to get the ETH/USD conversion rate and it finds that 1ETH = 2000USD, this is a blockchain state change, a couple of seconds later, the second node in the blockchain wants to agree on the state of the blockchain and sends a request to the API as well and we find that the ETH price is 2000.1USD. The two informations are different and hence we cannot reach consensus on the state of the blockchain.
	
- Smart contracts and blockchain are hence deterministic systems that cannot connect to real world data natively. This is the oracle problem... The oracle problem is just the smart contract connectivity problem.

.. diagram to be imported

Solving the oracle problem with Chainlink
-----------------------------------------

- Chainlink is a protocol for building decentralized oracle networks. 

- In this context, an oracle is a middleware that relates information about the real world into blockchains and smart contracts and relays info about blockchains and smart contracts back to the real world.

- There are two types of possible oracle networks, centralized oracle networks and decentralized oracle networks. If we want to get for example data about the ETH/USD conversion, we can simple use an external API to do this for us. However, this establishes what we call **a single point of failure**, that is, if an oracle provides false data to the smart contract and the smart contract executes based on that data, we have ourselves an “oracle problem”. **A centralized node defeats the whole purpose of decentralization that blockchains offer**. As it has been said in the chainlink whitepaper:
 
	- **“The security of any system is only as strong as its weakest link, so a highly trustworthy oracle is required to preserve the trustworthiness of a well-engineered blockchain.”**

.. NOTE::

	- **The solution is a decentralized oracle network: ChainLink**: Chainlink is a protocol for building modular decentralized oracle networks for whatever kind of data maybe needed for smart contracts. We can hence bring data in or trigger external computation in a decentralized way. This extends the decentralization and trust-minimization of smart contracts out to the data-delivery and data source layer.
	
	- DONs (Decentralized Oracle Networks) can be built with many or few nodes as needed.
	
Reaching consensus
-------------------

- DONs can have their own form of consensus. This is called aggregation. 

- Let's take an example where we need to get live Tesla stocks price data into a blockchain. Each node in the DON will get data on what the tesla price might be at a given time (That can be different from one node to another) but in the end, all of this is **aggregated** into a single datapoint, a single source of truth of what the price of the asset actually is which is passed to the blockchain or the smart contract.

.. diagram to be imported


Hybrid smart contracts
-----------------------

- By combining on chain contract code with off-chain ressources through oracles, we have a new type of smart contract called **Hybrid smart contracts**. 

- **Hybrid smart contracts** rely on existing on-chain code and combine it with off-chain components like data and computation and they bring the true original vision of smart contract to life. 

Chainlink data feeds and use cases
-----------------------------------

- Chainlink data feeds are pre-built DONs that are already gone through all the battle testing aand have a history and reputation of delivering secure and high quality data to blockchains for us to us for our smart contracts.

- DeFi, or Decentralized Fincance, is the most popular use case for DONs built with chainlink (Ex. Hybrid smart contracts). 

- DeFi takes traditional financial apps such as *borrowing*, *lending* and exchange of currencies etc.. and makes them decentralized smart contract applications (DApps). In order for these DeFi smart contracts to operate effectively, they all need to get price data of assets whether that is of cryptocurrenices themselves or stocks or whatever, and this is where **reference contracts** come into play.

.. note::
	
	- Reference contracts are smart contracts that DONs deliver decentralized data to so you can reference these "reference SC" to get this price data into your own smart contracts. and these can really be considered sources of truth for various currency pairs. 

.. diagram to be imported

- If we look at the diagram, on the left, we have **exchanges**, then we have **data providers** that are aggregating the price data from these exchanges, and then we have the **chainlink nodes**. Each one of the nodes can connect to multiple data providers, (and even the exchanges directly) to aggregate the price data for these price pairs at the node level. So, each node aggregates the price data individually and then communicate with each other as discussed previously and all of this is put on-chain with the reference smart contracts.


.. NOTE::
	**What if we have only one source of data ? (Goverment for example).**
		- In such a case, the source of data will become the source of truth for that data unfortuannatly. One can work on creating decentralized data sources for that source of data but either way we want the delivery layer of that data to be decentralized. Perhaps the source data is still centralized but we don't want a centralized source of data + a centralized data delivery to a decentralized blockchain. At least, with the decentralized oracle network in between, we can be assured that the data delivery layer can't be compromised and the only thing we will have to worry about is the centralized data source.
		
- Example: Check Chainlink Data feeds at: https://data.chain.link (ETH/USD for example).

.. NOTE::

	**Chainlink data feeds particularities**
		- Chainlink datafeeds covers both decentralized and centralized exchanges.
		- They can use techniques like volume based average method of aggregating data. That is, if we have for example an asset that is basically all traded on coinbase for example or binance, one really wants to wait price data coming from that exchange heavily because that's basically where all the price discovery is coming from. 
		- The feeds are live on multiple blockchains.
		- Most feeds use off-chain reporting (OCR).

.. warning::
	
	**What is OCR**
		- Each node of the DON is communicating with each other over a P2P network much like blockchains nodes do.
		- Each node aggregates their own price data, signs the final value, they deem to be the actual price of the asset.
		- This report is passed around between all the nodes.
		- A single node is elected as leader and posts the full report with all of the signed data transactions from each of the nodes on-chain. This reduce gas costs to 90%.

.. note:: 

	- Most DONs use the median value for price data. That is, the price of an asset is the median of the expected price delivered by each DON. This however can be customized if necessary. 
	- The average is not a very good choice to use in DONs because it is susceptible to outliers moving that average out. The median is more secure.
			
Chainlink VRF
-------------

- This is an abbreviation of Chainlink **V**erifiable **R**andomness **F**unction. 

- Due to the deterministic nature of blockchains, they are, along with smart contracts, bad at generating randomness (determinism is the opposite of randomness.. ).

- Even if we are able to find ways to incorportate randomness into our smart contracts and blockchains, this generated "on-chain" randomness can be easily biased by miners; Everytihng on-chain has to be deterministic by the nature of blockchains and hence, miners can predict what the randomness would be and that's how they can bias the randomness in their favor.

- What chainlink VRF does is that it provides a random number alongside a cryptographic proof that the number was indeed random. The cryptographic proof and the random number are both verified on-chain in a smart contract.

- The chainlink VRF hence provides a provably random and secure randomness to smart contracts.

.. NOTE::
	
	** Why is this important ?**
		- VRF allows provably fair outcomes where we need fair randomness like in lottery games for example.
		
Chainlink keepers
----------------- 

- *Chainlink Keepers enables smart contracts to automate key functions and event-driven tasks in a highly reliable, decentralized, and cost-efficient manner.* They are basically Chainlink nodes that call functions of your smart contract on your behalf. They do not compete with each other, rather, they take turns in executing the upkeeps.
		
Chainlink AnyAPI and Market
---------------------------

- Chainlink provides a way to connect your smart contract to any API.

- This is however not recommened for production put can be great for testing out a proof of concept.

- Chainlink has this chainlink market where we can, for any API, find a bunch of nodes that are listing their services and the jobs that they run.

Demo 
-----

** GOALS **

- Get used to using the chainlink docs (so important). http://docs.chain.link

- Build a smart contract using data feeds and deploy and interact with these contracts on-chain.

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
		        /*uint80 roundID*/,
		        int price,
		        /*uint startedAt*/,
		        /*uint timeStamp*/,
		        /*uint80 answeredInRound*/
		    ) = priceFeed.latestRoundData();
		    return price;
		}
	}

- This contract is using datafeeds through the import of chainlink's aggregatorV3Interface.sol. With that single import, the contract is able to use datafeeds.

- The contract have a constructor that sets and points to the datafeed we want. In this particular case, it points to the ETH/USD datafeed that's live on the Kovan ethereum testnet at the specified address.

- Additionally, we have a single function that gets the latest price, that is the conversion rate ETH/USD.
	
	
	
	
	
	
