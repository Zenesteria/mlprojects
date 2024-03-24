import socketio
from time import sleep

# Choose the desired namespace (replace 'your_namespace' with the actual name)
namespace = '/gesture'

sio = socketio.Client()
server_url = 'http://localhost:3000'

sio.connect(server_url)

@sio.on('connect')
def on_connect():
    print('Connected to the server')

@sio.on('disconnect')
def on_disconnect():
    print('Disconnected from the server')

@sio.on('response')  # Assuming the response event is also in the chosen namespace
def on_response(data):
    print(data)

@sio.on('message')  # Assuming the response event is also in the chosen namespace
def on_response(data):
    print(data)

while True:
    # print('...')
    sleep(1)
