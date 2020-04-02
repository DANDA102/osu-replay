#https://blog.naver.com/no1_devicemart/221664759948
import osu_replays_server as o
import socket
import time

#server part
serverSock = socket.socket()
serverSock.bind(('', 31221))
print("server open")
serverSock.listen(1)

connectionSock, addr = serverSock.accept()

print(str(addr),'connected')

#execute part
data = connectionSock.recv(1024)
print('received data: ', data.decode('utf-8'))

o.username = "firo"
o.anotherUsername = "sanshin"
o.checker()
o.saveHash()
o.sendHash()

time1 = time.time()

while time1 + 5 > time.time():
    pass

connectionSock.send('second step finished'.encode('utf-8'))
print('second step finished')


data = connectionSock.recv(1024)
print('received data: ', data.decode('utf-8'))

o.sendMapList()
o.sendMissingMaps()
o.getMissingMaps()
o.sendMapList()

connectionSock.send('last step finished'.encode('utf-8'))
print('last step finished')