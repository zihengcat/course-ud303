import http.server as hs
import urllib.parse as up

class MessageHandler(hs.BaseHTTPRequestHandler):
    def do_GET(self):
        html_file = open("./message_board_part_two.html", "r")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers();
        self.wfile.write(html_file.read().encode('utf-8'))
        html_file.close()

    def do_POST(self):
        # 1. How long was the message?
        # Use the Content-Length header
        length = int(self.headers.get('Content-length', 0))
        # 2. Read the correct amount of data from the request.
        data = self.rfile.read(length).decode('utf-8')
        #print(data)
        # 3. Extract the "message" field from the request data.
        message = up.parse_qs(data)["message"][0]
        # Send the "message" field back as the response.
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = hs.HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()

