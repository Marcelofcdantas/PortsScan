import sys
import socket
import os.path


def gettingDataAndScanningPorts():
    ipAddress=str(input('Which is the IP address of the machine to be scanned? \n'))
    firstPort=int(input('Which is the first port to be scanned? \n'))
    lastPort=int(input('Which is the last port to be scanned? \n'))
    noPortsOpen = True
    print('\n Scanning \n')
    portsNumber = 0
    listOfPorts = []
    while firstPort <= lastPort:
        print(f'Scanning port {firstPort}')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if s.connect_ex((ipAddress, firstPort)) == 0:
            portOpen=(f"Port {firstPort} open!")
            print(portOpen)
            listOfPorts.append(portOpen)
            noPortsOpen = False
            s.close()
        firstPort += 1
        portsNumber += 1
    
    if noPortsOpen:
        print("\n Wasn't possible to find an opened ports between the targets \n")
    print (f'All {portsNumber} ports scanned')
    generatingReport(listOfPorts)

def generatingReport(ports):
    for port in ports:
        try:
            folderName=input('Write the path to save the file \n')
            folderExists = os.path.exists(folderName)
            if not folderExists:
                os.makedirs(folderName)
            openPortsFile = os.path.join(folderName, 'OpenPorts.txt')
            with open(openPortsFile, 'w') as f:
                f.write(f'{port} \n')
        except IOError:
            print("Path designated doesn't exist")

gettingDataAndScanningPorts()