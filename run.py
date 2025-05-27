from src.core.system_state import SystemState
from src.api.routes import create_app

def main():
    system = SystemState()
    app = create_app(system)
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    main() 