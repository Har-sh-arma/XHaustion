from datetime import datetime, timedelta
from src.core.mock_hardware import MockTemperatureSensor, MockGasSensor, MockFan

class SystemState:
    def __init__(self):
        self.temp_sensor = MockTemperatureSensor()
        self.gas_sensor = MockGasSensor()
        self.fan = MockFan()
        self.start_time = datetime.now()
        self.total_energy = 0
        self.config = {
            'temp_threshold': 30,
            'gas_threshold': 500,
            'fan_speed_auto': True
        }

    def get_state(self):
        # Calculate uptime
        uptime = datetime.now() - self.start_time
        hours = int(uptime.total_seconds() // 3600)
        minutes = int((uptime.total_seconds() % 3600) // 60)
        seconds = int(uptime.total_seconds() % 60)
        uptime_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        # Calculate fan efficiency based on speed
        fan_speed = self.fan.get_speed()
        fan_efficiency = min(95, 70 + (fan_speed / 4))  # Efficiency increases with speed up to 95%

        # Calculate power consumption based on speed
        power_consumption = int(50 + (fan_speed * 2.5))  # Base 50W + up to 250W at full speed

        # Update total energy (Wh)
        self.total_energy += (power_consumption / 3600)  # Convert W to Wh (assuming 1 second update)

        # Calculate AQI score based on gas level
        gas_level = self.gas_sensor.read()
        aqi_score = max(0, min(100, 100 - (gas_level / 10)))

        return {
            'temperature': self.temp_sensor.read(),
            'gas_level': gas_level,
            'fan_speed': fan_speed,
            'fan_efficiency': int(fan_efficiency),
            'power_consumption': power_consumption,
            'total_energy': int(self.total_energy),
            'aqi_score': int(aqi_score),
            'uptime': uptime_str,
            'timestamp': datetime.now().isoformat()
        }

    def update_state(self, data):
        if 'fan_speed' in data:
            self.fan.set_speed(data['fan_speed'])

    def get_config(self):
        return self.config

    def update_config(self, data):
        self.config.update(data) 