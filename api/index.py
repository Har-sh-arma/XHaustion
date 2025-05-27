from http.server import BaseHTTPRequestHandler
import json
import time

# Simulated system state
system_state = {
    "temperature": 25.0,
    "gas_level": 100,
    "fan_speed": 60,
    "fan_efficiency": 90,
    "power_consumption": 120,
    "total_energy": 1000,
    "aqi_score": 95,
    "exhaust": 2500,
    "intake": 2000,
}

# System configuration
config = {
    "temp_threshold": 30,
    "gas_threshold": 500,
    "fan_speed_auto": True,
    "update_interval": 500,
    "exhaust_max_rpm": 3000,
    "intake_max_rpm": 2500,
    "has_intake": True
}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        if self.path.startswith('/api/system_state'):
            # Update simulated values
            system_state["temperature"] = 23.0 + (time.time() % 4)
            system_state["gas_level"] = 100 + (int(time.time() * 10) % 100)
            system_state["fan_speed"] = 60 + (int(time.time()) % 20)
            
            self.wfile.write(json.dumps(system_state).encode())
        elif self.path.startswith('/api/config'):
            self.wfile.write(json.dumps(config).encode())
        else:
            self.wfile.write(json.dumps({"error": "Invalid endpoint"}).encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length))

        if self.path.startswith('/api/system_state'):
            # Update system state
            system_state.update(post_data)
            self.wfile.write(json.dumps({"status": "success"}).encode())
        elif self.path.startswith('/api/config'):
            # Update configuration
            config.update(post_data)
            self.wfile.write(json.dumps({"status": "success"}).encode())
        else:
            self.wfile.write(json.dumps({"error": "Invalid endpoint"}).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers() 