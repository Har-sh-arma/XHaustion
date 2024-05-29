# write the http server using Python SimpleHTTPServer base class
import http.server
import socketserver
import json



PORT = 8000
DIRECTORY = "src"

def api_req(request) -> bool:
    if request.path.split("/")[1] != "api":
        return False
    return True

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    #add a get method to serve when super returns 404 (not found)
    def do_GET(self):
        print(self.path.split("/"))
        if(not api_req(self)):
            super().do_GET()
            return
        # Get reqs for information from the system
        print("api request")
        self.send_response(200)
        self.end_headers()
        return
    def do_POST(self):
        if(self.path.split("/")[2] == "config"):
            pass
        self.send_response(200)
        self.end_headers()
        return


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()