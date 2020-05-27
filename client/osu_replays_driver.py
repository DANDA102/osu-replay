#https://blog.naver.com/no1_devicemart/221664759948
import osu_replays as o
import socket

clientSock = socket.socket()
print('connecting...')
clientSock.connect(('하마치 아이피', 31221))

print('connected, first step started')

o.username = "firo"
o.anotherUsername = "sanshin"
o.getHashes()
o.getReplays()

clientSock.send('first step finished'.encode('utf-8'))

print('first step finished')


data = clientSock.recv(1024)
print('received data: ', data.decode('utf-8'))

o.searchHashes("failed\\")

clientSock.send('third step finished'.encode('utf-8'))

print('third step finished')

data = clientSock.recv(1024)
print('received data: ', data.decode('utf-8'))