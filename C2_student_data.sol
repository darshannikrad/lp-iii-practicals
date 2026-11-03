// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * Practical C2: Student Data Smart Contract (Structures and Arrays)
 * Group C: Blockchain (Solidity / Ethereum)
 *
 * Problem Statement:
 * Write and deploy a Solidity student-data smart contract using structures and arrays;
 * observe transaction fee and gas values upon state writes versus reads.
 *
 * Description:
 * Demonstrates data modeling using custom structs and dynamic arrays in Ethereum:
 * - struct Student groups id, name, and marks.
 * - Student[] public students maintains an on-chain dynamic record array.
 * - addStudent(...) appends records using .push(). Since it modifies contract storage,
 *   it triggers a state transaction and consumes gas.
 * - getStudent(index) and totalStudents() are view functions; calling them directly
 *   from an off-chain client (e.g. Remix IDE) costs zero gas.
 * - receive() and fallback() functions handle incoming plain ETH or non-matching calls.
 *
 * Test Sequence (Remix IDE):
 *   1. addStudent(1, "Amit", 85)   -> Transaction succeeds (record gas used)
 *   2. addStudent(2, "Riya", 92)   -> Transaction succeeds (compare gas with step 1)
 *   3. totalStudents()             -> Returns 2 (view, 0 gas)
 *   4. getStudent(0)               -> Returns (1, "Amit", 85) (0 gas)
 *   5. getStudent(1)               -> Returns (2, "Riya", 92) (0 gas)
 *   6. getStudent(5)               -> Reverts with array out-of-bounds error
 *
 * Observing Gas & Transaction Fees:
 * - Gas: Unit of computational work.
 * - Gas Limit: Maximum amount of gas user is willing to spend.
 * - Gas Price: Fee per unit of gas in Gwei (1 Gwei = 10^-9 ETH).
 * - Total Fee = Gas Used * Gas Price.
 * - Storage vs Memory vs Calldata:
 *   - 'storage': Permanent on-chain state (most expensive opcode: SSTORE).
 *   - 'memory': Temporary, modifiable memory during function execution.
 *   - 'calldata': Read-only, non-modifiable input parameters (cheapest).
 * - Fallback vs Receive:
 *   - receive(): Executes when plain ETH is transferred with empty calldata.
 *   - fallback(): Executes when called function does not exist or invalid data is provided.
 */

contract StudentData {
    // Custom structure grouping student fields
    struct Student {
        uint id;
        string name;
        uint marks;
    }

    // Dynamic array stored in contract storage (permanent on blockchain)
    Student[] public students;

    // Adds a new student record to dynamic array (Costs gas: storage write)
    function addStudent(uint _id, string memory _name, uint _marks) public {
        students.push(Student(_id, _name, _marks));
    }

    // Retrieves student data by index (Free: read-only view function)
    function getStudent(uint index)
        public
        view
        returns (uint, string memory, uint)
    {
        require(index < students.length, "Index out of bounds");
        Student memory s = students[index];
        return (s.id, s.name, s.marks);
    }

    // Returns the total count of registered students
    function totalStudents() public view returns (uint) {
        return students.length;
    }

    // Fallback: Triggered when no matching function signature is found
    fallback() external payable {}

    // Receive: Triggered on plain ETH transfers with empty calldata
    receive() external payable {}
}
