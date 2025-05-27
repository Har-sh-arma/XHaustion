from flask import jsonify, request
from src.api import init_app
from src.core.system_state import SystemState

def create_app(system: SystemState):
    app = init_app()

    @app.route('/api/system_state', methods=['GET'])
    def get_system_state():
        return jsonify(system.get_state())

    @app.route('/api/system_state', methods=['POST'])
    def update_system_state():
        data = request.get_json()
        system.update_state(data)
        return jsonify({"status": "success"})

    @app.route('/api/config', methods=['GET'])
    def get_config():
        return jsonify(system.get_config())

    @app.route('/api/config', methods=['POST'])
    def update_config():
        data = request.get_json()
        system.update_config(data)
        return jsonify({"status": "success"})

    return app 