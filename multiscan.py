#!/usr/bin/env python3
import socket
import signal
import sys
from colorama import Fore, Style

def signal_handler(signal, frame):
  global interrupted
  interrupted = True
  print("bye")
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

#serverliste einlesen
f = open('./serverlist.sort', 'r')
lines = f.read()
list = lines.splitlines()
ser = 0
fai = 0

inter = False

def portscan(server, port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(2)
  try:
    conn = sock.connect((server,port))
  except:
    return False
  sock.close()
  return True

interrupted = False
print("Abbruch mit Ctrl+C")
for server in list:
  ser = ser + 1
  if portscan(server,80) or portscan(server,443):
    print(Fore.GREEN + 'Server', server, 'is open')
  else:
    print(Fore.RED + 'Server', server, 'is close')
    fai = fai + 1
  if interrupted:
    break


print(Style.RESET_ALL)
print("Tests:", ser, "Fehler:", fai)
