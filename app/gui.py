import tkinter as tk
from tkinter import messagebox, scrolledtext
from src.blockchain import Blockchain
from src.wallet import Wallet
import json

# Initialize blockchain and wallets
blockchain = Blockchain()
sender_wallet = Wallet()
receiver_wallet = Wallet()


def truncate_key(key):
    """Shorten public key string for better GUI display."""
    key_str = str(key)
    return key_str[:50] + "..." + key_str[-20:]


def send_transaction():
    try:
        amount = float(amount_entry.get())
        transaction = {
            'sender': str(sender_wallet.public_key),
            'recipient': str(receiver_wallet.public_key),
            'amount': amount
        }
        signature = sender_wallet.sign_transaction(transaction)

        if sender_wallet.verify_transaction(transaction, signature):
            blockchain.add_transaction(transaction)
            blockchain.mine()
            display_chain()
            messagebox.showinfo("Success", "Transaction sent and mined.")
        else:
            messagebox.showerror("Error", "Transaction verification failed.")
    except ValueError:
        messagebox.showerror("Error", "Invalid amount.")


def display_chain():
    chain_output.delete(1.0, tk.END)
    for block in blockchain.chain:
        block_data = {
            "index": block.index,
            "transactions": block.transactions,
            "timestamp": block.timestamp,
            "previous_hash": block.previous_hash,
            "nonce": block.nonce,
            "hash": block.hash
        }
        pretty_block = json.dumps(block_data, indent=4)
        chain_output.insert(tk.END, f"Block {block.index}:\n{pretty_block}\n\n")

# GUI Layout
window = tk.Tk()
window.title("Blockchain Transaction Simulation")
window.geometry("700x600")

tk.Label(window, text="Sender Public Key:").pack()
sender_key_text = scrolledtext.ScrolledText(window, height=3, wrap=tk.WORD)
sender_key_text.insert(tk.END, truncate_key(sender_wallet.public_key))
sender_key_text.pack()

tk.Label(window, text="Receiver Public Key:").pack()
receiver_key_text = scrolledtext.ScrolledText(window, height=3, wrap=tk.WORD)
receiver_key_text.insert(tk.END, truncate_key(receiver_wallet.public_key))
receiver_key_text.pack()

tk.Label(window, text="Amount:").pack()
amount_entry = tk.Entry(window)
amount_entry.pack()

tk.Button(window, text="Send Transaction", command=send_transaction).pack(pady=10)

chain_output = scrolledtext.ScrolledText(window, height=20, wrap=tk.WORD)
chain_output.pack()

window.mainloop()