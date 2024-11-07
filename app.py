from flask import Flask, render_template, request, flash, url_for
from markupsafe import Markup
import csv
from datetime import datetime
import Project3
import os
from time import time

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "your secret key"


def get_stock_symbols():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    stock_symbols = []
    with open('stocks.csv', newline='') as csvfile:
        stockreader = csv.DictReader(csvfile)
        for row in stockreader:
            stock_symbols.append(row['Symbol'])
    return stock_symbols

@app.route('/', methods=['GET', 'POST'])
def index():
    stock_symbols = get_stock_symbols()
    graph_svg = None  # Initialize graph_svg to None

    if request.method == 'POST':
        chart_type = request.form.get('chart_type')
        if chart_type not in ['bar', 'line']:
            flash('Invalid chart type selected.')
            return render_template('index.html', stock_symbols=stock_symbols, graph_svg=graph_svg)
        
        time_series = request.form.get('time_series')
        if time_series not in ['intraday', 'daily', 'weekly', 'monthly']:
            flash('Invalid time series selected.')
            return render_template('index.html', stock_symbols=stock_symbols, graph_svg=graph_svg)
        
        try:
            start_date = datetime.strptime(request.form.get('start_date'), '%Y-%m-%d')
            end_date = datetime.strptime(request.form.get('end_date'), '%Y-%m-%d')
            if end_date < start_date:
                flash("Error: The end date must be after the start date.")
                return render_template('index.html', stock_symbols=stock_symbols, graph_svg=graph_svg)
        except ValueError:
            flash("Error: Invalid date format. Please use YYYY-MM-DD.")
            return render_template('index.html', stock_symbols=stock_symbols, graph_svg=graph_svg)
        
        symbol = request.form.get('symbol')
        api_function = {
            "intraday": "TIME_SERIES_INTRADAY",
            "daily": "TIME_SERIES_DAILY",
            "weekly": "TIME_SERIES_WEEKLY",
            "monthly": "TIME_SERIES_MONTHLY"
        }.get(time_series, "TIME_SERIES_DAILY")
        raw_data = Project3.get_JSON_data(symbol, time_series, start_date, end_date)

        if not raw_data:
            flash(f"Failed to fetch data for symbol: {symbol}")
        else:
            Project3.graph(raw_data, symbol, time_series, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'),  chart_type)
                
            absolute_file_path = os.path.join(os.path.dirname(__file__), "chart.svg")
                
            try:
                with open(absolute_file_path, 'r') as file:
                    graph_svg = Markup(file.read())
            except Exception as e:
                flash(f"An error occurred reading the graph file: {str(e)}")

    return render_template('index.html', stock_symbols=stock_symbols, graph_svg=graph_svg)

if __name__ == '__main__':
    app.run(host="0.0.0.0")

app.run(host="0.0.0.0")