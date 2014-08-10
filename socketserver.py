import socket, select
import sys
from thread import *

clientlist = []
host = ''
port = 8888

def broadcast(sender, message):
    for client in clientlist:
        if (client != sender) and (client != server_socket):
            try:
                client.send(message)
            except:
                client.close()
                if client in clientlist:
                    clientlist.remove(client)

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM); #TCP socket
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
except socket.error,msg:
    print 'socket error with msg ', msg
    sys.exit()
try:
    server_socket.bind((host,port))
except socket.error, msg:
    print 'bind error'
    sys.exit()
print 'socket bind complete'
server_socket.listen(10)
clientlist.append(server_socket)
print 'listening'

while True:
    read_sockets, write_sockets, error_sockets = select.select(clientlist, [], []);
    for client in read_sockets:
        if (client == server_socket):
            conn, addr = server_socket.accept() #conn is the socket file descriptor of the new client
            clientlist.append(conn)
            print 'New client added: ', addr
            broadcast(conn, 'new client (%s, %s) joined\n' % addr)
        else:
            try:
                message = client.recv(1024)
                if message:
                    broadcast(client, "\r" + '<' + str(client.getpeername()) + '> ' + message)
                # continue
            except:
                # I want to detect when client is closed
                # broadcast(client, 'client (%s, %s) might be leaving now.\n' % addr)
                print 'client (%s, %s) might be leaving now.' % addr
                client.close()
                if client in clientlist:
                    clientlist.remove(client)
                continue

server_socket.close()