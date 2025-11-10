
"""Wallet class and creation"""
import secrets
class Wallet:
    def __init__(self):
        self.private = secrets.token_hex(32)
        self.public = secrets.token_hex(32)
def create_wallet_set(n=5):
    master = Wallet()
    subs = [Wallet() for _ in range(n)]
    return {'master': master, 'subs': subs}
if __name__ == '__main__':
    ws = create_wallet_set(3)
    print(f"Master: {ws['master'].public} Sub wallets: {[w.public for w in ws['subs']]}")
