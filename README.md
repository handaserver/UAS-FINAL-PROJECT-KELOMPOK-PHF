# UAS-FINAL-PROJECT-KELOMPOK-PHF
#PUTRYLIA HANDAYANI_21.83.0739
import subprocess
import pyfiglet

ascii_banner = pyfiglet.figlet_format("format")
print(ascii_banner)

nw = subprocess.check_output(['netsh','wlan','show','network'])
decoded_nw= nw.decode('ascii')
print(decoded_nw)
