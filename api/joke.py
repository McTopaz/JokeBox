from http.server import BaseHTTPRequestHandler
import json

# https://jokebox-k1s6it1az-mctopazs-projects.vercel.app/api/joke

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'message': 'Hello from your backend!'}).encode('utf-8'))