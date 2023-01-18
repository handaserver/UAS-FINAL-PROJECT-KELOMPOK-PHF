# UAS-FINAL-PROJECT-KELOMPOK-PHF
#PUTRI CATHALINIYA_21.83.0735
import socket
import pyfiglet

ascii_banner = pyfiglet.figlet_format("TRANSFER FILE by Kelompok PHF")
print(ascii_banner)

sock = socket.socket()

port = 8800
host = ''

sock.bind((host, port))

sock.listen(10)

while True:
    con, addr = sock.accept()

    data = con.recv(1024)
    print(data.decode())
    file = open('uas.txt', 'rb')
    line = file.read(1024)
    while(line):
        con.send(line)
        line = file.read(1024)
    
    file.close()
    print('File telah dikirim.')

    con.close()

