from aiohttp import web

# We kick off our server
from sockets.socketio_server import app

if __name__ == '__main__':
    print("")
    web.run_app(app, port=9999)
