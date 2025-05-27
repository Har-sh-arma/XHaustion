from datetime import datetime
from src.core.mock_hardware import MockTemperatureSensor, MockGasSensor, MockFan

class SystemState:
    def __init__(self):
        self.temp_sensor = MockTemperatureSensor()
        self.gas_sensor = MockGasSensor()
        self.fan = MockFan()
        self.config = {
            'temp_threshold': 30,
            'gas_threshold': 500,
            'fan_speed_auto': True
        }

    def get_state(self):
        return {
            'temperature': self.temp_sensor.read(),
            'gas_level': self.gas_sensor.read(),
            'fan_speed': self.fan.get_speed(),
            'timestamp': datetime.now().isoformat()
        }

    def update_state(self, data):
        if 'fan_speed' in data:
            self.fan.set_speed(data['fan_speed'])

    def get_config(self):
        return self.config

    def update_config(self, data):
        self.config.update(data) 