from Crypto.Cipher import AES

key = bytes.fromhex('8e29bd9f7a4f50e2485acd455bd6595ee1c6d029c8b3ef82eba0f28e59afcf9f')
cipher = AES.new(key, AES.MODE_ECB)

test = bytes.fromhex('abcdd57efb034baf82fc1920a618e6a7fa496e319b4db1746b7d7e3d1198f64f')
c = cipher.decrypt(test)
print(c)