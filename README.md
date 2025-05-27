# XHaustion - Smart Kitchen Exhaust Monitoring System

XHaustion is a modern web-based monitoring and control system for kitchen exhaust systems. It provides real-time monitoring of temperature, gas levels, fan speeds, and overall system performance.

## Features

- **Real-time Dashboard**: Monitor temperature, gas levels, fan speed, and air quality
- **Hood Management**: Control multiple hood zones with individual temperature and airflow monitoring
- **Fan Control**: Adjust fan speeds, monitor performance metrics, and view historical data
- **Responsive Design**: Modern, mobile-friendly interface built with Tailwind CSS
- **API Integration**: RESTful API endpoints for system state and configuration

## Tech Stack

- HTML5/CSS3/JavaScript
- Tailwind CSS for styling
- Chart.js for data visualization
- Python backend API
- Vercel for deployment

## Project Structure

```
XHaustion/
├── api/
│   ├── index.py          # Python API handler
│   └── requirements.txt  # Python dependencies
├── src/
│   ├── static/          # Static assets (CSS, JS)
│   └── templates/       # HTML templates
│       ├── index.html   # Dashboard
│       ├── hoods.html   # Hood management
│       ├── fan.html     # Fan control
│       ├── help.html    # Help documentation
│       └── config.html  # System configuration
├── vercel.json          # Vercel deployment config
└── .vercelignore       # Vercel ignore patterns
```

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/XHaustion.git
   cd XHaustion
   ```

2. Install dependencies:
   ```bash
   # For Python API
   cd api
   pip install -r requirements.txt
   ```

3. Run locally:
   ```bash
   # Using Vercel CLI
   vercel dev
   ```

4. Deploy to Vercel:
   ```bash
   vercel
   ```

## API Endpoints

- `GET /api/system_state` - Get current system state
- `POST /api/system_state` - Update system state
- `GET /api/config` - Get system configuration
- `POST /api/config` - Update system configuration

## Version History

### v1.0
- Initial release
- Modern UI with responsive design
- Real-time monitoring dashboard
- Hood zone management
- Fan control system
- Help documentation
- System configuration

## License

MIT License - See LICENSE file for details
