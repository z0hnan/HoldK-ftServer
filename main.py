#pip install playsound
try:
    from playsound import playsound
except ImportError:
    import os
    os.system('pip install playsound==1.2.2')
    from playsound import playsound
from http.server import BaseHTTPRequestHandler, HTTPServer
from os import system, name


class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        command = post_data.decode()

        if command == "play":
            playsound('shutup.mp3')


        #Svarer tilbage
        response = command
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response.encode())

#Start serveren
def run(server_class=HTTPServer, handler_class=RequestHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting server...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()