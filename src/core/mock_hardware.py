import random
import math
from datetime import datetime

class MockTemperatureSensor:
    def read(self):
        # Simulate temperature between 20-35°C with daily pattern
        hour = datetime.now().hour
        base_temp = 25 + 5 * math.sin(hour * math.pi / 12)  # Peak at noon
        return round(base_temp + random.uniform(-1, 1), 1)

class MockGasSensor:
    def __init__(self):
        self.base_level = 100
        self.last_spike = 0

    def read(self):
        # Simulate occasional spikes in gas levels
        now = datetime.now().timestamp()
        if now - self.last_spike > 300 and random.random() < 0.1:  # 10% chance of spike every 5 minutes
            self.last_spike = now
            return round(random.uniform(500, 1000))
        return round(self.base_level + random.uniform(-50, 50))

class MockFan:
    def __init__(self):
        self.speed = 0
        self.target_speed = 0
        
    def set_speed(self, speed):
        self.target_speed = max(0, min(100, speed))
        
    def get_speed(self):
        # Smooth transition to target speed
        if self.speed < self.target_speed:
            self.speed = min(self.target_speed, self.speed + 5)
        elif self.speed > self.target_speed:
            self.speed = max(self.target_speed, self.speed - 5)
        return round(self.speed, 1) 