import time
from typing import List

from merkletree import hex, unhex, reverse, build_merkle_tree
from transaction import Transaction
from util import double_hash


def calculate_merkel_root(transactions: List[Transaction]):
    transaction_hashes = []

    for t in transactions:
        transaction_hashes.append(t.transaction_hash)

    formatted_transactions = {
        'leaves': [reverse(unhex(e)) for e in transaction_hashes],
    }

    root = build_merkle_tree(formatted_transactions['leaves'])

    return root


class Header:
    def __init__(self, hash_prev_block: str, transactions: List[Transaction], bits: int = "1d00ffff", nonce: int = 0,
                 version: int = 1):
        self.version = version
        self.hash_prev_block = hash_prev_block
        self.hash_merkle_root = calculate_merkel_root(transactions)
        self.timestamp = str(time.time())
        self.bits = bits
        self.nonce = nonce

    def get_header_str(self):
        root_data = (hex(reverse(self.hash_merkle_root.data)).decode("utf-8"))

        concat = self.timestamp + root_data + self.bits + str(self.nonce) + self.hash_prev_block

        return double_hash(concat)


