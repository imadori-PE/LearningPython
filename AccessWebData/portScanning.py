import socket

def port_scanner(target,ports):
    strIP = socket.gethostbyname(target)
    # * The socket.gethostbyname method in Python is used to get the IP address of a host given its name
    print(f'scanning {target} ({strIP})')
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((strIP, port)) 
        if result == 0:
            print(f'Port {port} : Open')
        else:
            print(f'Close port {port}')
    
# ? example usage
target = 'dr-chuck.com'
ports = [22,80,443,8080]
port_scanner(target,ports)
