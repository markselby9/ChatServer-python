__author__ = 'fengchaoyi'
import sys,string,select,socket

def prompt():
    sys.stdout.write('You said: ')
    sys.stdout.flush()

if (len(sys.argv)!=3):
    print 'usage: python selectclient.py <address> <port>'
    sys.exit()
hostaddr = sys.argv[1]
port = int(sys.argv[2]) #need int here

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(5)
try:
    client_socket.connect((hostaddr, port))
except:
    print 'connect error with ', hostaddr, port
    sys.exit()

print 'client successfully connected to server'
prompt()

while True:
    server_socketlist = [sys.stdin, client_socket] #read server socket list
    read_sockets, write_sockets, error_sockets = select.select(server_socketlist, [], [])
    for client in read_sockets:
        if (client == client_socket):
            data = client.recv(1024)
            if not data:
                print 'Disconnected from server'
                sys.exit()
            else:
                sys.stdout.write(data)
                prompt()
        else:
            message = sys.stdin.readline()
            client_socket.send(message)
            prompt()