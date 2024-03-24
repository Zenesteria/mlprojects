
import socketio
import eventlet

sio = socketio.Server(async_mode='eventlet',cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('Client connected with session ID:', sid)
    sio.emit('message', 'Welcome to the server!')

@sio.event
def message(sid, data):
    print('Message received from client', sid, ':', data)
    formattedData = f'Message: {data}'
    print(formattedData)
    sio.emit('response', data)

@sio.event
def temperature(sid,data):
    print(data)
    sio.emit("temp",data)

@sio.event
def video(sid,data):
    print(data)
    sio.emit("vid",data)

@sio.event
def disconnect(sid):
    print('Client', sid, 'disconnected')

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 3000)), app)