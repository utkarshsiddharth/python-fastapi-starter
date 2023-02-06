import socketio

sio_server = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=[]
)

sio_app = socketio.ASGIApp(
    socketio_server=sio_server,
)


@sio_server.event
async def connect(sid, environ, auth):
    print(f"{sid} Client Connected")

@sio_server.event 
async def disconnect(sid):
    print(f"{sid} Client Disconnect")

@sio_server.event 
async def greeting():
    sio_server.emit('Hi there cliet :)')
