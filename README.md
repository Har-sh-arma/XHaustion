# XHaustion - Smart Kitchen Exhaust Control System

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Flask Version](https://img.shields.io/badge/flask-3.0%2B-green)

XHaustion is an intelligent kitchen ventilation control system designed to optimize air quality, reduce fire hazards, and improve energy efficiency. Originally designed for Raspberry Pi, this demo version simulates the hardware interactions for demonstration purposes.

## 🌟 Features

### Core Functionality
- Real-time temperature and gas level monitoring
- Automated fan speed control with fuzzy logic
- Manual and automatic operation modes
- Energy consumption tracking
- Air quality assessment

### Technical Features
- Modern web-based dashboard
- Real-time data visualization
- RESTful API
- Secure authentication system
- Comprehensive logging system

## 🛠️ Technology Stack

### Backend
- Python 3.8+
- Flask 3.0+
- Flask-CORS
- Flask-JWT-Extended
- Pydantic

### Frontend
- HTML5/CSS3
- JavaScript
- Chart.js
- Tailwind CSS

### Deployment
- Vercel (Demo)
- NGINX (Production)
- Gunicorn

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Node.js and npm (for development)

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Har-sh-arma/XHaustion.git
   cd XHaustion
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

5. Access the dashboard at `http://localhost:5000`

## 🏗️ Project Structure

```
XHaustion/
├── src/                # Source code directory
├── config/            # Configuration files
├── logs/             # System logs
├── powerLogs/        # Power consumption logs
├── service/          # Service related files
├── splash/           # Splash screen assets
├── temp_test/        # Testing files
├── SystemClasses.py  # Core system classes
├── Sensor.py         # Sensor implementations
├── actuator.py       # Actuator control
├── server.py         # Web server
├── main.py           # Main application
└── requirements.txt   # Python dependencies
```

## 🔌 API Endpoints

### System State
- `GET /api/system_state` - Get current system state
- `POST /api/system_state` - Update system state

### Configuration
- `GET /api/config` - Get system configuration
- `POST /api/config` - Update system configuration

## 📊 Dashboard Features

- Real-time temperature and gas level monitoring
- Interactive fan speed control
- System status indicators
- Historical data visualization
- Performance metrics
- Energy consumption tracking

## 🔐 Security

- JWT-based authentication
- API rate limiting
- CORS protection
- Input validation
- Error handling

## 🔄 Hardware Simulation

The demo version includes simulated hardware components:
- Temperature sensor (20-35°C range)
- Gas sensor (0-1000 ppm)
- Exhaust fan with variable speed
- Power consumption monitoring

## 📈 Performance

- Real-time updates (500ms refresh rate)
- Smooth data transitions
- Responsive design
- Optimized for mobile devices

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- Harsh Sharma - *Initial work* - [Har-sh-arma](https://github.com/Har-sh-arma)

## 📄 Documentation

For detailed documentation and system requirements specification, please refer to our [SRS Document](https://docs.google.com/document/d/1cHztWfM1maviUGyw1m9Zhh6XxKp-vSWppw0n4d6HxLQ/edit?usp=sharing)

## 🙏 Acknowledgments

- Chart.js for data visualization
- Flask community for the excellent framework
- All contributors who helped in testing and development

## 📞 Contact

- Project Link: [https://github.com/Har-sh-arma/XHaustion](https://github.com/Har-sh-arma/XHaustion)

---
⭐️ If you find this project useful, please consider giving it a star!
