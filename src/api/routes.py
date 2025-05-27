from flask import jsonify, request, render_template
from src.api import init_app
from src.core.system_state import SystemState

def create_app(system: SystemState):
    app = init_app()

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/hoods')
    def hoods():
        return render_template('hoods.html')

    @app.route('/fan')
    def fan():
        return render_template('fan.html')

    @app.route('/help')
    def help():
        return render_template('help.html')

    @app.route('/config')
    def config():
        return render_template('config.html')

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

    @app.route('/static/css/<path:filename>')
    def serve_static(filename):
        return app.send_static_file(f'css/{filename}')

    return app 