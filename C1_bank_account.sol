// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * Practical C1: Bank Account Smart Contract
 * Group C: Blockchain (Solidity / Ethereum)
 *
 * Problem Statement:
 * Write and deploy a bank account smart contract on a test network (e.g. Sepolia or Remix VM)
 * supporting deposit, withdrawal, and balance display.
 *
 * Description:
 * A smart contract is an immutable, self-executing program deployed on a decentralized blockchain.
 * In this contract:
 * - uint balance is stored permanently on the blockchain state.
 * - deposit(amount) increases the balance (state-changing transaction; consumes gas).
 * - withdraw(amount) checks for sufficient balance using require() and reduces balance (reverts on failure).
 * - showBalance() is marked 'view', so reading current state directly costs zero gas.
 *
 * Test Sequence (Remix IDE):
 *   1. deposit(500)      -> Transaction succeeds
 *   2. showBalance()     -> Returns 500
 *   3. withdraw(200)     -> Transaction succeeds
 *   4. showBalance()     -> Returns 300
 *   5. withdraw(1000)    -> Fails and reverts: "Insufficient balance"
 *
 * Key Viva Points:
 * - view vs pure vs transaction:
 *   - 'view' reads state but does not modify it (free to call outside a tx).
 *   - 'pure' neither reads nor modifies state.
 *   - functions modifying state cost gas and must be mined into a block.
 * - require(condition, message):
 *   - If condition is false, execution halts, all state changes revert, and remaining unspent gas is refunded.
 * - Gas: Computation cost unit on Ethereum (Fee = Gas Used * Gas Price).
 */

contract Bank {
    uint balance;

    // Deposit amount into the account
    function deposit(uint amount) public {
        balance += amount;
    }

    // Withdraw amount with safety validation
    function withdraw(uint amount) public {
        require(balance >= amount, "Insufficient balance");
        balance -= amount;
    }

    // Read current balance (view: no gas cost when called externally)
    function showBalance() public view returns (uint) {
        return balance;
    }
}

/**
 * Bonus: Production / Real-ETH Version
 * If the examiner asks: "What is the limitation of the simple contract?"
 * Answer: In the basic version, balance is a single shared variable without individual account
 * separation, and no real cryptocurrency (Wei/ETH) moves.
 * Below is the production version using msg.sender, payable, and a balance mapping.
 */
contract BankRealETH {
    mapping(address => uint) private balances;

    // Accepts real testnet ETH via msg.value
    function deposit() public payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");
        balances[msg.sender] += msg.value;
    }

    // Withdraws ETH to the caller's wallet
    function withdraw(uint amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
    }

    // View caller's individual balance
    function showBalance() public view returns (uint) {
        return balances[msg.sender];
    }
}
