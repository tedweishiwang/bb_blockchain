from typing import List
from pprint import pprint
from header import Header
from transaction import Transaction


def build_transaction_map(transactions: List[Transaction]):
    transaction_map = {}
    for transaction in transactions:
        transaction_map[transaction.get_transaction_hash()] = transaction

    return transaction_map


class Block:
    def __init__(self, header: Header, transactions: List[Transaction]):
        self.magic_number: int = 0xD9B4BEF9
        self.block_size: int = 0
        self.block_header: Header = header
        self.transaction_counter: int = len(transactions)
        self.transactions: dict = build_transaction_map(transactions)
        self.block_hash: str = header.get_header_str()

    def print_block(self):
        pprint(vars(self))