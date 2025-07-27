import socket
import threading

clients = []

def handle(client, other):
  while True:
    try:
      data = client.recv(1024)
      if other:
        other.send(data)
    except:
      break

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 10000))
server.listen(2)
print("Relay server running on port 10000...")

while True:
  conn, addr = server.accept()
  print(f"Connected: {addr}")
  clients.append(conn)
  if len(clients) == 2:
    threading.Thread(target=handle, args=(clients[0], clients[1])).start()
    threading.Thread(target=handle, args=(clients[1], clients[0])).start()
    clients = []
