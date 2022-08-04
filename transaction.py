from pprint import pprint
from typing import List
from util import double_hash


class Transaction:
    def __init__(self, version_number: int, in_counter: int, list_of_inputs: List, out_counter: int,
                 list_of_outputs: List):
        self.version_number = version_number
        self.in_counter = in_counter
        self.list_of_inputs = list_of_inputs
        self.out_counter = out_counter
        self.list_of_outputs = list_of_outputs
        self.transaction_hash = self.get_transaction_hash()

    def get_transaction_hash(self):
        concat = str(self.version_number) + str(self.in_counter)

        for input in self.list_of_inputs:
            concat += input

        concat += str(self.out_counter)

        for output in self.list_of_outputs:
            concat += output

        return double_hash(concat).encode("utf-8")

    def print_transaction(self):
        pprint(vars(self))