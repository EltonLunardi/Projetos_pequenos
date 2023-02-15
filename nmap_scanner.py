import nmap

scanner = nmap.PortScanner()

ip_addr = input("Insira o endereço de ip: ")
print("O ip inserido foi: ", ip_addr)
type(ip_addr)

resp = input("""\nInsira o endereço de ip que quer scanear
                1:SYN ACK scan
                2:UDP scan
                3:Super scanner \n""")
print("Sua opção", resp)

if resp == '1':
    print('Versao nmap: ', scanner.nmap_version.scanner())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print('Ip status: ', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print('Portas abertas: ', scanner[ip_addr]['tcp'].keys())

elif resp == '2':
    print('Versao nmap: ', nmap_version.scanner())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print('Ip status: ', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print('Portas abertas: ', scanner[ip_addr]['udp'].keys())

elif resp == '3':
    print('Versao nmap: ', nmap_version.scanner())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -A -O')
    print(scanner.scaninfo())
    print('Ip status: ', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print('Portas abertas: ', scanner[ip_addr]['tcp'].keys())

elif resp == '4':
    print('Opção errada')
