from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "0.0.0.0"
PORT = 8888

class NeutralHTTP(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>HELLO I AM KAYLAN</h1></body></html>", "utf-8"))

server = HTTPServer((HOST, PORT), NeutralHTTP) 

print("Server now loading...")

server.serve_forever()
server.server_close()
print("Server stopped!")