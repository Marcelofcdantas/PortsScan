import socket
import os.path
import sys
import re
import asyncio


def selectIpOption():
    print ('Choose a number between the options below:')
    print ('1 - If you wanna scan just one IP address.')
    print ('2 - If you wanna scan many IP addresses inserting one by one.')
    print ('3 - If you wanna scan many IP addresses inserting the IP range')
    selectedOption=int(input())
    checkingSelectedOption(selectedOption)


def checkValidIP(IP):
    match = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", IP)
    return (bool(match))


def checkingSelectedOption(selectedOption):
    if selectedOption == 1:
        gettingDataAndPorts(selectedOption)
    elif selectedOption == 2:
        howmanyIPAdresses() 
    elif selectedOption == 3:
        getIpRange()
    else:
        selectIpOption()


def howmanyIPAdresses():
    answer=int(input('How many IP addresses do you want to check the ports? '))
    if answer < 1:
        print('Invalid number')
        howmanyIPAdresses()
    else:
        gettingDataAndScanningPorts(answer)
        

def dividingIPs(firstIP, lastIP):
    firtIP_divided = firstIP.split(".")
    lastIP_divided = lastIP.split(".")
    return firtIP_divided, lastIP_divided


def getIpRange():
    firstIP=(input('Which is the first IP address of the machine to be scanned? \n'))
    lastIP=(input('Which is the last IP address of the machine to be scanned? \n'))
    resultFirstIP = checkValidIP(firstIP)
    resultLastIP = checkValidIP(lastIP)
    if not resultFirstIP or not resultLastIP:
        print('An invalid IP addresses was inserted')
        getIpRange()
    else:
        firstIP_divided, lastIP_divided = dividingIPs(firstIP, lastIP)
        firstIP_part_1 = int(firstIP_divided[0])
        firstIP_part_2 = int(firstIP_divided[1])
        firstIP_part_3 = int(firstIP_divided[2])
        firstIP_part_4 = int(firstIP_divided[3])
        lastIP_part_1 = int(lastIP_divided[0])
        lastIP_part_2 = int(lastIP_divided[1])
        lastIP_part_3 = int(lastIP_divided[2])
        lastIP_part_4 = int(lastIP_divided[3])
        firstIP = int(firstIP_part_1), int(firstIP_part_2), int(firstIP_part_3), int(firstIP_part_4)
        lastIP = int(lastIP_part_1), int(lastIP_part_2), int(lastIP_part_3), int(lastIP_part_4)
        firstPort=int(input('Which is the first port to be scanned? \n'))
        lastPort=int(input('Which is the last port to be scanned? \n'))
        noPortsOpen = True
        portsNumber = 0
        listOfPorts = []
        while firstIP <= lastIP:
            TempFirstPort = firstPort
            TempFirstIP = "{}.{}.{}.{}".format(firstIP_part_1, firstIP_part_2, firstIP_part_3, firstIP_part_4)
            print('\n Scanning {}\n'.format(TempFirstIP))
            while TempFirstPort <= lastPort:
                print(f'Scanning port {TempFirstPort}')
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if s.connect_ex((TempFirstIP, TempFirstPort)) == 0:
                    portOpen=(f"Port {TempFirstPort} open!")
                    print(portOpen)
                    listOfPorts.append(f'{TempFirstIP}, {portOpen}')
                    noPortsOpen = False
                    s.close()
                TempFirstPort += 1
                portsNumber += 1
            firstIP_part_4 += 1
            if firstIP_part_4 > 255:
                firstIP_part_4 = 0
                firstIP_part_3 += 1
                if firstIP_part_3 > 255:
                    firstIP_part_3 = 0
                    firstIP_part_2 += 1
                    if firstIP_part_2 > 255:
                        firstIP_part_2 = 0
                        firstIP_part_1 += 1
            firstIP = int(firstIP_part_1), int(firstIP_part_2), int(firstIP_part_3), int(firstIP_part_4)


def gettingDataAndPorts(numberOfIPS):
    if numberOfIPS == 1:
        ipAddress=[(input('Which is the IP address of the machine to be scanned? \n'))]
        resulttIP = checkValidIP(ipAddress[0])
        if not resulttIP:
            print('An invalid IP addresses was inserted')
        gettingDataAndPorts(numberOfIPS)
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
    openPorts = len(listOfPorts)
    print(f' {openPorts} open')
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


if sys.argv[1] and sys.argv[2]:
    ip = sys.argv[1]
    resulttIP = checkValidIP(ip)
    if not resulttIP:
        print('An invalid IP addresses was inserted')
        exit
    ports = sys.argv[2].split('-')
    firstPort = int(ports[0])
    lastPort = int(ports[1])
    TempFirstPort = firstPort
    print(f'\n Scanning {ip}\n')
    listOfPorts = []
    portsNumber = 0
    noPortsOpen = True
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

else:
    selectIpOption()
