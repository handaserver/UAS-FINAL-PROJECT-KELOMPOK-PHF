# UAS-FINAL-PROJECT-KELOMPOK-PHF
#FENELLA CLARESTA_21.83.0757
import pyfiglet
import sys
import socket
from datetime import datetime
  
ascii_banner = pyfiglet.figlet_format("PORT SCANNER by Kelompok PHF")
print(ascii_banner)

target = input(str("Masukkan Target IP: "))

# Tambahkan Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)
  
try:

    # Melakukan scan pada setiap port yang menjadi target IP
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
         
        # Kembali ke port yang terbuka
        result = s.connect_ex((target,port))
        if result ==0:
            print("[+] Port {} terbuka".format(port))
        s.close()
         
except KeyboardInterrupt:
        print("\n Keluar dari program !")
        sys.exit()
except socket.gaierror:
        print("\n Host tidak merespon !")
        sys.exit()
