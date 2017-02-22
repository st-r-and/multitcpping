#!/usr/bin/env python3
import socket

#serverliste einlesen
f = open('./serverlist.sort', 'r')
lines = f.read()
list = lines.splitlines()
ser = 0
fai = 0

def portscan(server, port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(30)
  try:
    #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = sock.connect((server,port))
    #sock.close()
    #return True
  except:
    return False
  sock.close()
  return True

for server in list:
  ser = ser + 1
  if portscan(server,80) or portscan(server,443):
    print('Server', server, 'is open')
  else:
    print('Server', server, 'is close')
    fai = fai + 1

print(ser, fai)
