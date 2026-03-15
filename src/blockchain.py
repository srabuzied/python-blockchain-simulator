import hashlib
import json
from time import time


class Block:
    """Represents a single block in the blockchain."""

    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        """
        Returns the SHA-256 hash of the block contents.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    """Blockchain implementation with proof-of-work consensus."""

    difficulty = 2  # Number of leading zeros required in hash

    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """Initializes the blockchain with the genesis block."""
        genesis_block = Block(0, [], time(), "0")
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        """Adds a transaction to the unconfirmed transaction pool."""
        self.unconfirmed_transactions.append(transaction)

    def proof_of_work(self, block):
        """
        Simple proof of work algorithm:
        Increment nonce until block hash satisfies difficulty requirement.
        """
        block.nonce = 0
        computed_hash = block.compute_hash()

        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()

        return computed_hash

    def mine(self):
        """
        Attempts to mine a block containing unconfirmed transactions.
        """
        if not self.unconfirmed_transactions:
            return False

        new_block = Block(
            index=self.last_block.index + 1,
            transactions=self.unconfirmed_transactions,
            timestamp=time(),
            previous_hash=self.last_block.hash
        )

        new_block.hash = self.proof_of_work(new_block)
        self.chain.append(new_block)
        self.unconfirmed_transactions = []

        return new_block.index