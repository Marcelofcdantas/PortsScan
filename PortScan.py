import socket
import os.path

def howmanyIPAdresses():
    answer=input('How many IP addresses do you want to check the ports? ')
    if answer < 1:
        print('Invalid number')
        howmanyIPAdresses()
    else:
        gettingDataAndScanningPorts(answer)
        

def gettingDataAndScanningPorts(numberOfIPS):
    if numberOfIPS == 1:
        ipAddress=str(input('Which is the IP address of the machine to be scanned? \n'))
    else:
        firstIP=str(input('Which is the IP address of the first machine to be scanned? \n'))
        lastIP=str(input('Which is the IP address of the last machine to be scanned? \n'))
        ipInArray = dividingIPs(firstIP, lastIP)
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

def dividingIPs(firstIP, lastIP):
    for item in firstIP:
        tempIP = ''
        if item != '.':
            tempIP += item
            firstIP = firstIP.replace(item, '')
        else:
            firstIP.replace(item, '')
    

'''
def dividingIPs(firstIP, lastIP):
    IpPart = 1
    for character in firstIP:
        if (character != ".") and (IpPart == 1):
            IP1ClassA += character
        elif (character != ".") and (IpPart == 2):
            IP1ClassB += character
        elif (character != ".") and (IpPart == 3):
            IP1ClassC += character
        else:
            IP1ClassC += character
        IpPart +=1
    ipInArray.append(IP1ClassA)
    ipInArray.append(IP1ClassB)
    ipInArray.append(IP1ClassC)
    ipInArray.append(IP1ClassD)
    IpPart = 1
    for character in lastIP:
        if (character != ".") and (IpPart == 1):
            IP2ClassA += character
        elif (character != ".") and (IpPart == 2):
            IP2ClassB += character
        elif (character != ".") and (IpPart == 3):
            IP2ClassC += character
        elif (character != ".") and (IpPart == 4):
            IP2ClassC += character
        IpPart +=1
    ipInArray.append(IP2ClassA)
    ipInArray.append(IP2ClassB)
    ipInArray.append(IP2ClassC)
    ipInArray.append(IP2ClassD)
    listOfIps = creatingIpArrays(ipInArray)
    return ipInArray


def creatingIpArrays(ipInArray):
    listOfIps = []
    firstArray = 0
    secondArray = 4
    classAIP = separatingIpParts(ipInArray[firstArray], ipInArray[lastArray])
    firstArray += 1
    lastArray += 1
    classBIP = separatingIpParts(ipInArray[firstArray], ipInArray[lastArray])
    firstArray += 1
    lastArray += 1
    classCIP = separatingIpParts(ipInArray[firstArray], ipInArray[lastArray])
    firstArray += 1
    lastArray += 1
    classDIP = separatingIpParts(ipInArray[firstArray], ipInArray[lastArray])
    return generatingIps(classAIP, classBIP, classCIP, classDIP)

def generatingIps(classAIP, classBIP, classCIP, classDIP):
    

def separatingIpParts(A, B):
    while A <= B:
        classIp.append(A)
        A+= 1
    return classIp
'''

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