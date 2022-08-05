from typing import Optional

from block import Block
from header import Header
from transaction import Transaction

NONE_PREV_HASH = "0" * 64


class BlockChain:
    def __init__(self):
        print("Initializing block chain...")
        self.block_map = {}
        self.genesis_block = self.create_genesis_block()
        self.max_height = 0
        self.cur = self.genesis_block

    def create_genesis_block(self) -> Block:
        genesis_transactions = [
            Transaction(
                1,
                1,
                ["first input transaction for genesis block"],
                1,
                ["first output transaction for genesis block"]
            )
        ]

        genesis_header = Header(
            NONE_PREV_HASH,
            genesis_transactions
        )

        genesis_block = Block(
            genesis_header,
            genesis_transactions
        )

        self.block_map[0] = {}
        self.block_map[0][genesis_block.block_hash] = genesis_block

        print("The Genesis block hash is: " + genesis_block.block_hash)

        return genesis_block

    def list_all_blocks(self):
        print(self.block_map)

    def add_block(self, newtransactions: list) -> Block:
        newheader = Header(
            self.cur.block_hash,
            newtransactions
        )

        newblock = Block(
            newheader,
            newtransactions
        )

        self.max_height = self.max_height + 1
        self.block_map[self.max_height] = {}
        self.block_map[self.max_height][newblock.block_hash] = newblock
        self.cur = newblock

        print("new block with block hash " + newblock.block_hash + " has been appended.")

        return newblock

    def search_block_by_height_and_blockhash(self, block_height, block_hash) -> Optional[Block]:
        if block_height not in self.block_map:
            print("The height " + block_height + " does not exist.")
            return None

        if block_hash not in self.block_map[block_height]:
            print("The block hash " + block_hash + " does not exist.")
            return None

        return self.block_map[block_height][block_hash]

    def search_transaction(self, transaction_hash) -> Optional[Transaction]:
        current_block = self.cur
        current_height = self.max_height

        while current_block.block_hash != NONE_PREV_HASH:
            print("Looking for transaction ", transaction_hash, " in block ", current_block.block_hash)
            if transaction_hash in current_block.transactions:
                return current_block.transactions[transaction_hash]

            prev_block_hash = current_block.block_header.hash_prev_block
            prev_height = current_height - 1
            current_block = self.search_block_by_height_and_blockhash(prev_height, prev_block_hash)

        print("Transaction not found.")
        return None


if __name__ == '__main__':
    block_chain = BlockChain()
    print()

    print("Create transactions:")
    t1 = Transaction(1, 1, ["t1 input transaction for genesis block"], 1, ["t1 output transaction for genesis block"])
    t2 = Transaction(1, 1, ["t2 input transaction for genesis block"], 1, ["t2 output transaction for genesis block"])
    t3 = Transaction(1, 1, ["t3 input transaction for genesis block"], 1, ["t3 output transaction for genesis block"])
    t4 = Transaction(1, 1, ["t4 input transaction for genesis block"], 1, ["t4 output transaction for genesis block"])
    t5 = Transaction(1, 1, ["t5 input transaction for genesis block"], 1, ["t5 output transaction for genesis block"])
    t6 = Transaction(1, 1, ["t6 input transaction for genesis block"], 1, ["t6 output transaction for genesis block"])
    t7 = Transaction(1, 1, ["t7 input transaction for genesis block"], 1, ["t7 output transaction for genesis block"])
    t8 = Transaction(1, 1, ["t8 input transaction for genesis block"], 1, ["t8 output transaction for genesis block"])
    t9 = Transaction(1, 1, ["t9 input transaction for genesis block"], 1, ["t9 output transaction for genesis block"])
    t10 = Transaction(1, 1, ["t10 input transaction for genesis block"], 1, ["t10 output transaction for genesis block"])

    print("t1 hash is ", t1.get_transaction_hash())
    print("t2 hash is ", t2.get_transaction_hash())
    print("t3 hash is ", t3.get_transaction_hash())
    print("t4 hash is ", t4.get_transaction_hash())
    print("t5 hash is ", t5.get_transaction_hash())
    print("t6 hash is ", t6.get_transaction_hash())
    print("t7 hash is ", t7.get_transaction_hash())
    print("t8 hash is ", t8.get_transaction_hash())
    print("t9 hash is ", t9.get_transaction_hash())
    print("t10 hash is ", t10.get_transaction_hash())
    print()

    print("Create a block with the first 5 transactions and append to the Genesis block:")
    block_chain.add_block([t1, t2, t3, t4, t5])
    first_block = block_chain.cur

    print("Create a block with the first 5 transactions and append to the previous block:")
    block_chain.add_block([t6, t7, t8, t9, t10])
    second_block = block_chain.cur

    print()
    print("Testing finding block by height and block hash: ")
    block_chain.search_block_by_height_and_blockhash(2, second_block.block_hash).print_block()

    print()
    print("Testing finding transaction by transaction hash: ")
    block_chain.search_transaction(t3.get_transaction_hash()).print_transaction()
