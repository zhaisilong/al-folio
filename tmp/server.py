# server.py
from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Hello, World!")
        else:
            self.send_error(404, "File Not Found")

if __name__ == "__main__":
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    print("Starting HTTP server on port 8080")
    httpd.serve_forever()