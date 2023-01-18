# UAS-FINAL-PROJECT-KELOMPOK-PHF
#PUTRI CATHALINIYA DF_21.83.0735
import socket
import pyfiglet

ascii_banner = pyfiglet.figlet_format("TRANSFER FILE by Kelompok PHF")
print(ascii_banner)

sock = socket.socket()

port = 8800
host = '192.168.56.1'

sock.connect((host, port))
sock.send('Terdapat pesan dari client'.encode())

file = open('uas.txt', 'wb')

line = sock.recv(1024)

while(line):
    file.write(line)
    line = sock.recv(1024)

print('File telah diterima.')

file.close()
sock.close()
