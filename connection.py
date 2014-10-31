from Crypto.PublicKey import RSA
import socket
import sys


class serverConnection:
    def __init__(self):
        self.RSAServer = RSA.importKey(b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCniHbdv+321GAunHmPZ03DtFDL\nQKu26VyDrUsNYbZgLcnGhm6/itLRMuKaGhCnin55om4JR+awPQegUgxwJBTvk9rL\ng2Ax0UdYw2LG4S2YnTjKsQ8qfqwroTkRQNddBfj/VDNTrk1YF+/32uDvSQZlJhZo\nlq6BMu8VpDo0clid9wIDAQAB\n-----END PUBLIC KEY-----')
        self.RSALocal = RSA.importKey(open("local.key", "r").read())
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(("localhost", 3636))
        data = self.RSALocal.publickey().exportKey("PEM")
        self.sock.sendall(data)

    def transact(self, fr_id, next_seed, amount, last_seed):
        data = "%s,5,%s,%s,%s" % (fr_id, amount, last_seed,next_seed)
        msg = self.RSAServer.encrypt(data.encode("utf8"), None)
        self.sock.sendall(msg[0])
        return self.RSALocal.decrypt(self.sock.recv(4096))
