
import unittest
from src.blockchain import Blockchain


class TestBlockchain(unittest.TestCase):
    def test_blockchain_initialization(self):
        blockchain = Blockchain()
        self.assertEqual(len(blockchain.chain), 1)

    def test_add_transaction(self):
        blockchain = Blockchain()
        tx = {'sender': 'A', 'recipient': 'B', 'amount': 100}
        blockchain.add_transaction(tx)
        self.assertEqual(len(blockchain.unconfirmed_transactions), 1)

    def test_mining(self):
        blockchain = Blockchain()
        tx = {'sender': 'A', 'recipient': 'B', 'amount': 50}
        blockchain.add_transaction(tx)
        blockchain.mine()
        self.assertEqual(len(blockchain.chain), 2)


if __name__ == '__main__':
    unittest.main()
