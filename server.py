# write the http server using Python SimpleHTTPServer base class
import http.server
import socketserver
import json
from shared_memory_dict import SharedMemoryDict
import shared_memory_dict
import shared_memory_dict.serializers


system_state = None
PORT = 8000
DIRECTORY = "src"

def api_req(request) -> bool:
    if request.path.split("/")[1] != "api":
        return False
    return True



'''
Shared memory manipulation works only on the higher level so pull the dict modify and push it back
'''

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
   
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super(Handler, self).end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()


    #add a get method to serve when super returns 404 (not found)
    def do_GET(self):
        # print(self.path.split("/"))
        if (self.path == "/raspi"):
            self.send_response(200)
            self.end_headers()
            return 
        if(not api_req(self)):
            super().do_GET()
            return
        # Get reqs for information from the system
        if(self.path.split("/")[2] == "config"):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            config = json.load(open("./config/config.json"))
            data = json.dumps(config).encode("utf-8")
            self.send_header("Content-Length", len(data))
            self.end_headers()
            self.wfile.write(data)
            return
        if(self.path.split("/")[2] == "system_state"):
            print(system_state)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            data = shared_memory_dict.serializers.JSONSerializer().dumps(str(system_state).replace("'", '"'))
            self.send_header("Content-Length", len(data))
            self.end_headers()
            self.wfile.write(data)
            return
        self.send_response(404)
        self.end_headers()
        return
    
    def do_POST(self):
        # Secure this part
        if(self.path.split("/")[2] == "config"):
            req = self.rfile.read(int(self.headers['Content-Length'])).decode("utf-8")
            config = json.loads(req)
            json.dump(config, open("./config/config.json", "w"))

                
        elif(self.path.split("/")[2] == "system_state"):
            req = self.rfile.read(int(self.headers['Content-Length'])).decode("utf-8")
            new_state = json.loads(req)
            for key in system_state:
                system_state[key] = new_state[key]

        self.send_response(200)
        self.end_headers()
        return



if __name__ == "__main__":
    system_state = SharedMemoryDict('system_state', 1024)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
