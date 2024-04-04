import sys
import socket

ipAddress=str(input('Which is the IP address of the machine to be scanned? \n'))
firstPort=int(input('Which is the first port to be scanned? \n'))
lastPort=int(input('Which is the last port to be scanned? \n'))

noPortsOpen = True
print('\n Scanning \n')
portsNumber = 0
while firstPort <= lastPort:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if s.connect_ex((ipAddress, firstPort)) == 0:
        print(f"Port {firstPort} open!")
        noPortsOpen = False
        s.close()
    firstPort += 1
    portsNumber += 1
    print(f'port scanned {firstPort}')

if noPortsOpen:
    print("\n Wasn't possible to find an opened ports between the targets \n")
print (f'All {portsNumber} scanned')