import asyncio
import socket
import os.path

def howmanyIPAdresses():
    answer=int(input('How many IP addresses do you want to check the ports? '))
    if answer < 1:
        print('Invalid number')
        howmanyIPAdresses()
    else:
        gettingDataAndScanningPorts(answer)
        

def gettingDataAndScanningPorts(numberOfIPS):
    if numberOfIPS == 1:
        ipAddress=[(input('Which is the IP address of the machine to be scanned? \n'))]
    else:
        ipAddress=[]
        for number in range(numberOfIPS):
            tempIp=(input('Insert the ip number \n'))
            ipAddress.append(tempIp)
    firstPort=int(input('Which is the first port to be scanned? \n'))
    lastPort=int(input('Which is the last port to be scanned? \n'))
    noPortsOpen = True
    portsNumber = 0
    listOfPorts = []
    for ip in ipAddress:
        TempFirstPort = firstPort
        print(f'\n Scanning {ip}\n')
        while TempFirstPort <= lastPort:
            print(f'Scanning port {TempFirstPort}')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if s.connect_ex((ip, TempFirstPort)) == 0:
                portOpen=(f"Port {TempFirstPort} open!")
                print(portOpen)
                listOfPorts.append(f'{ip}, {portOpen}')
                noPortsOpen = False
                s.close()
            TempFirstPort += 1
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


howmanyIPAdresses()