# PortsScan
App developed to practice scanning ports of a computer to discover which of them (between the selected) are opened.
This app requests how many IP addresses will be checked, the number of IP address(es) to scan their open ports, the number of the first port to be scanned, and the last one. After this, it will return which port is being scanned. Finally, it requests a path to save the txt file with the opened ports, and checks if it exists. If it doesn't exist, it will create the folder and save the file in the chosen folder.

- Updates made in which it is possible to call the file with the flags *IP*, *first Port*-*last Port*, and it won't be necessary to fill these pieces of information on the menu.
- New update allows using the flag "-all" to check all ports instead of writing 1-65353.

    
 E.g. `python PortScan.py 10.0.0.2 80-90`

 
 E.g. `python PortScan.py 10.0.0.2 -all`

![Screenshot_2024-10-02_23_26_50](https://github.com/user-attachments/assets/0e730884-c134-41ef-afde-db2837f6bb21)


![image](https://github.com/Marcelofcdantas/PortsScan/assets/65692996/ba2aa6a2-714e-4a4a-8a49-109aa7a2945c)


![image](https://github.com/Marcelofcdantas/PortsScan/assets/65692996/bb32a127-f34c-4aa7-bbf3-cc73e5555d3c)

