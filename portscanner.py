from time import sleep
import socket
from colorama import *
import colorama
import subprocess
import sys
from datetime import datetime



def progress(count, total):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...\r' % (bar, percents, '%'))
    sys.stdout.flush() 

def portscan():
    total = port_end
    i = port_start


    while i < int(total):
        try:
            for port in range(int(port_start), int(port_end)):
                progress(i, total)
                i += 1
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remoteServerIP, port))
                if result == 0:
                    print (Fore.RED + "[ - ] " + Fore.GREEN + " Port {}: 	Open".format(port))
                sock.close()

        except KeyboardInterrupt:
            print (Fore.RED + "\n\n[ * ] Quitting")
            sys.exit()

        except socket.gaierror:
            print (Fore.RED + "\n\n[ * ] Error, could not find hostname " + remoteServer + " Exiting")
            sys.exit()

        except socket.error:
            print (Fore.RED + "[ * ] Error, Couldn't connect to server")
            sys.exit()



subprocess.call('clear', shell=True)
colorama.init()
intro = Fore.BLUE + " -----[ Portscanner 2.0 ]-----"
for items in intro:
    print(items, end="")
    sys.stdout.flush()
    sleep(0.1)


remoteServer = str(input(Fore.RED + "\n[ * ] " + Fore.YELLOW + "Enter a remote host to scan: "))
remoteServerIP = socket.gethostbyname(remoteServer)
port_start = float(input(Fore.RED + "\n[ * ] " + Fore.YELLOW + "Enter start port : "))
port_end = float(input(Fore.RED + "[ * ] " + Fore.YELLOW + "Enter last port : "))
print (Fore.YELLOW + "-" * 61)
print (Fore.RED + "[ - ] " + Fore.YELLOW + "Please wait, scanning remote host", remoteServerIP + "\n")

t1 = datetime.now()

portscan()
t2 = datetime.now()
total =  t2 - t1
print (Fore.RED +'[ - ] ' + Fore.YELLOW + '\n\nScanning Completed in: ', total)
