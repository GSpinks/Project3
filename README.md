# Project3: Stock Data Visualizer

A Flask-based web application that visualizes stock market data using data from Alpha Vantage API. The application is containerized using Docker for easy deployment and consistency across different environments.

## Features

* Interactive web interface for stock data visualization
* Support for multiple chart types (Bar and Line)
* Various time series options (Intraday, Daily, Weekly, Monthly)
* Date range selection for customized data viewing
* Pre-populated stock symbol selection from S&P 500
* Real-time data fetching from Alpha Vantage API
* Interactive charts generated using Pygal
* Containerized application using Docker

## Prerequisites

* Docker and Docker Compose installed on your system
* Internet connection for accessing Alpha Vantage API
* Web browser for accessing the application

## Installation & Setup

1. Clone the repository to your local machine:
```
git clone -b 3a-update https://github.com/GSpinks/Project3.git
cd Project3
```

2. Build and run the Docker container:
```
docker-compose up --build
```

3. Access the application:
    * Open your web browser
    * Navigate to `http://localhost:5000`

## Usage

1. Select a stock symbol from the dropdown menu
2. Choose the chart type (Bar or Line)
3. Select the time series (Intraday, Daily, Weekly, Monthly)
4. Enter the start and end dates for the data range
5. Click "Generate Chart" to view the visualization

## Project Structure

```
Project3/
├── Templates/
│   └── index.html           # HTML template for web interface
├── __pycache__/
│   └── Dockerfile           # Docker configuration
│   └── Project3.py          # Stock data processing logic
│   └── README.md            # Project documentation
│   └── app.py               # Main Flask application
│   └── chart.svg            # Generated stock visualization output
│   └── docker-compose.yaml  # Docker Compose configuration
│   └── requirements.txt     # Dependencies
│   └── stocks.csv           # Stock symbols database
```

## Technical Details

* **Framework**: Flask 3.0.3
* **Visualization**: Pygal 3.0.4
* **Data Source**: Alpha Vantage API
* **Container**: Python 3.8 slim-buster base image
* **Dependencies**: See requirements.txt for complete list

## Error Handling

The application includes error handling for:
* Invalid date ranges
* API connection issues
* Invalid chart type selections
* Data processing errors

## Acknowledgments

* Alpha Vantage for providing the stock market data API
* Pygal for the charting library
* Flask for the web framework
* Docker for containerization
