import pyaes
import base64
import os
from dotenv import load_dotenv


load_dotenv()
SECRET = os.getenv("SECRET")

flag=open("flag.txt").read()

aes = pyaes.AESModeOfOperationCTR(SECRET.encode())
ciphertext = aes.encrypt(flag)
base_cipher = base64.b64encode(ciphertext)

with open("flag.bin","wb") as file:
  file.write(base_cipher)
