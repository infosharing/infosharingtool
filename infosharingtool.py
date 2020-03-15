import sys
from cryptography.fernet import Fernet
import random

print("""



		 by : pr0fh3cy and SharingTeamBogdan
		 pr0fh3cy github : https://github.com/pr0fh3cy
		 SharingTeamBogdan github : https://github.com/SharingTeamBogdan
		 ver : python3
		 SO : windows


		 
""")
d = 0
while(d != 4):
	print()
	print("1 - strong password tool")
	print("2 - encrypt tool")
	print("3 - decrypt tool")
	print("4 - exit")
	d = int(input("infosharing:-$ "))
	if(d == 1):
		h = 0
		while(h != 3):
			print()
			print("1 - password tool")
			print("3 - back")
			h = int(input("password-tool:-$ "))
			chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
			n=int(input("Number-of-characters-in-you-password?(higher than 6):-$ "))
			x=0;
			password=input("string:-$ ")
			while(x<=n):
				password+=random.choice(chars)
				x+=1
			print(password)
			if(h == 3):
				break
	if(d == 2):

		n = 0
		while(n != 3):
			print()
			print("1 - encrypt some string ")
			print("2 - encrypt some text file")
			print("3 - back")
			n = int(input("encrypt:-$ "))
			if(n == 1):
					key = Fernet.generate_key()
					data = input("string:-$ ")
					f = Fernet(key)
					encrypt = f.encrypt(data.encode())
					print("string encrypted : ", encrypt.decode())
					print("key : ",key.decode())
			elif(n == 2):
				key2 = Fernet.generate_key()
				inp = input("file-to-encrypt-path:-$ ")
				out = input("file-to-copy-encrypt-path:-$ ")
				key3 = input("file-to-copy-key-path:-$ ")
				with open(inp,'rb') as f:
					mess = f.read()
				g = Fernet(key2)
				encrypt2 = g.encrypt(mess)
				with open(out,'wb') as f:
					f.write(encrypt2)
				with open(key3,'wb') as d:
					d.write(key2)
				print("Check : ",out)
			elif(n == 3):
				break
	if(d == 3):
		print()
		print("1 - decrypt some string ")
		print("2 - decrypt some text file")
		print("3 - back")
		n = 0
		while(n != 3):
			n = int(input("decrypt:-$ "))
			if(n == 1):
					data = input("string:-$ ")
					key = input("key:-$ ")
					f = Fernet(key.encode())
					encrypt = f.decrypt(data.encode())
					print("string decrypted : ", encrypt.decode())
			elif(n == 2):
				inp = input("file-to-decrypt-path:-$ ")
				out = input("file-to-copy-decrypt-path:-$ ")
				key3 = input("file-key-path:-$ ")
				with open(inp,'rb') as f:
					mess = f.read()
				with open(key3,'rb') as j:
					key2 = j.read()
				g = Fernet(key2)
				encrypt2 = g.decrypt(mess)
				with open(out,'wb') as f:
					f.write(encrypt2)
				print("Check : ",out)
			elif(n == 3):
				break
	if(d == 4):
		print("WHY ? ... BRO")
		sys.exit()
