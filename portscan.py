import socket
import subprocess
from datetime import datetime
import time
import sys


def exiting():
    print('Exiting program...')
    time.sleep(2)
    sys.exit()


while True:


    print('>>>>> PORT SCANNER <<<<<')
    print('v1.0')
    print('@NaoWasTaken\n')
    print('[SCANNER] -- PORTS 1-1023 (ESSENTIAL_PROCESSES) --')
    
    start = input('[1] Start\n[2] Exit\n ')
    if start == '1':


        target = input('\nEnter the target IP address <: ')


        def port_scan(target):

            while True:
                

                try:
                    ip = socket.gethostbyname(target)

                    print(f'\nScanning the target {ip}')
                    print('Time started:', datetime.now())
                    print('')

                    for port in range(0, 10):
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(1)
                        result = sock.connect_ex((ip, port))
                        if result == 0:
                            print("Port {}: Open".format(port))
                            sock.close()

                except socket.gaierror:
                    print('Host name could not be resolved\n')
                    exiting()
                
                except socket.error:
                    print('Could not connect to the server\n')
                    exiting()
                
                again = input('Would you like to scan again? Y/N <: ').upper()
                if again == 'Y':
                    continue
                elif again =='N':
                    break
                else:
                    print('Enter a valid response')

        port_scan(target)

        new_ip = input('Would you like to scan a new ip address? Y/N <: ').upper()
        if new_ip == 'Y':
            continue

        elif new_ip =='N':
            exiting()

        else:
            print('Enter a valid response')
    

    elif start == '2':
        exiting()
    

    else:
        print('Enter a valid response')
        continue