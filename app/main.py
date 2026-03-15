from src.blockchain import Blockchain
from src.wallet import Wallet

# Initialize blockchain and wallets
blockchain = Blockchain()
wallet1 = Wallet()
wallet2 = Wallet()

# Create a transaction
transaction = {
    'sender': str(wallet1.public_key),
    'recipient': str(wallet2.public_key),
    'amount': 50
}

# Sign and verify
signature = wallet1.sign_transaction(transaction)
if wallet1.verify_transaction(transaction, signature):
    blockchain.add_transaction(transaction)
    blockchain.mine()

# Print the blockchain
for block in blockchain.chain:
    print(f"Block {block.index}: {block.__dict__}")
