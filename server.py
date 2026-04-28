def do_GET(self):
    # do_GET function mein yeh add karo after health check
    if self.path == '/':
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('index.html', 'rb') as f:
            self.wfile.write(f.read())
    elif self.path == '/dashboard':
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('dashboard.html', 'rb') as f:
            self.wfile.write(f.read())