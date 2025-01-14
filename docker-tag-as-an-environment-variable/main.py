from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os


APP_VERSION = os.getenv("APP_VERSION", "no version")


class ServiceHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = {"version": APP_VERSION}

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


host = "0.0.0.0"
port = 8080

server = HTTPServer((host, port), ServiceHandler)
print(f"Running API version '{APP_VERSION}' on http://{host}:{port}")
server.serve_forever()
