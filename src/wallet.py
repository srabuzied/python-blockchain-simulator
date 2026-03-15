
import rsa


class Wallet:
    """Handles public-private key generation and transaction signing."""

    def __init__(self):
        self.public_key, self.private_key = rsa.newkeys(512)

    def sign_transaction(self, transaction):
        """
        Signs a transaction using the wallet's private key.
        """
        transaction_data = str(transaction).encode('utf-8')
        return rsa.sign(transaction_data, self.private_key, 'SHA-256')

    def verify_transaction(self, transaction, signature):
        """
        Verifies the transaction signature using the public key.
        """
        transaction_data = str(transaction).encode('utf-8')
        try:
            rsa.verify(transaction_data, signature, self.public_key)
            return True
        except rsa.VerificationError:
            return False
