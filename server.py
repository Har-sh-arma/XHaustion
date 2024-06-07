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
    
    #add a get method to serve when super returns 404 (not found)
    def do_GET(self):
        # print(self.path.split("/"))
        if(not api_req(self)):
            super().do_GET()
            return
        # Get reqs for information from the system
        if(self.path.split("/")[2] == "config"):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            config = json.load(open("./config/config.json"))
            self.wfile.write(json.dumps(config).encode("utf-8"))
            return
        if(self.path.split("/")[2] == "system_state"):
            print(system_state)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(shared_memory_dict.serializers.JSONSerializer().dumps(str(system_state).replace("'", '"')))
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
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
