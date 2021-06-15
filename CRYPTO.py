#cryptograph entire folder 
from cryptography.fernet import Fernet
from glob import glob
import os

class Encryptor:
    def __init__(self):
        self.path = input("Enter the path to your folder>> ")
        self.op = int(input("1.Encrypt\n2.Decrypt\n>>"))
        self.create_key()

    def create_key(self):
        try:
            k_file = open("secret.key","rb")
            self.key = k_file.read()
        except FileNotFoundError:
            self.key = Fernet.generate_key()
            k_file = open("secret.key","wb")
            k_file.write(self.key)

    def encrypt(self, data):
        f_key = Fernet(self.key)
        enc_data = f_key.encrypt(data)
        return enc_data

    def decrypt(self, data):
        f_key = Fernet(self.key)
        dec_data = f_key.decrypt(data)
        return dec_data

    def run(self):
        for file in glob(self.path+"/*"):
            if self.op == 1:
                try:
                    data = open(file,"rb").read()
                except:
                    continue
                enc_data = self.encrypt(data)
                f = open(file+".aes","wb")
                f.write(enc_data)
                os.remove(file)
            elif self.op == 2:
                try:
                    data = open(file, "rb").read()
                except:
                    continue
                dec_data = self.decrypt(data)
                f = open(file[:-4], "wb")
                f.write(dec_data)
                os.remove(file)

crypto = Encryptor()
crypto.run()
