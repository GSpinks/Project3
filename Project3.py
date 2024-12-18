from datetime import datetime
import sys
import requests
import pygal
import lxml

# Stock API: Y5BQFD53B87D4N0O

def getStock():
    stock_symbol = input("Enter the stock symbol you are looking for: ")
    return stock_symbol

def getChart():
    while True:
        types = input("\nChart Types\n-------------\n1. Bar\n2. Line\n\nEnter the chart type you want (1, 2): ")
        if types == "1" or types == "2":
            return types
        else:
            print("Enter a 1 or 2 for chart type")

def getTimeSeries():
    while True:
        dash = ("-"*56)
        time = input(f"\nSelect the Time Series of the chart you want to generate. Warning: Intraday only contains recent data.\n{dash}\n1. Intraday\n2. Daily\n3. Weekly\n4. Monthly\n\nEnter the time series option (1, 2, 3, 4): ")
        if time == "1" or time == "2" or time == "3" or time == "4":
            return time
        else:
            print("Enter a 1, 2, 3, or 4, for Time Series")

def getDate():
    while True:
        dateStart = input("Enter the start date (YYYY-MM-DD): ")
        dateEnd = input("Enter the end date (YYYY-MM-DD): ")
        dateFormat = "%Y-%m-%d"
        try:
            date1 = datetime.strptime(dateStart, dateFormat).date()
            date2 = datetime.strptime(dateEnd, dateFormat).date()
            if date1 < date2:
                return date1, date2
            else:
                print("\nError: Start date cannot be later than end date. Enter the dates again.\n")
        except:
            print("\nWrong date format. Please try again.\n")

def get_JSON_data(symbol, time_series, date1, date2):
    if time_series == "1":
        time_string = "TIME_SERIES_INTRADAY"
    elif time_series == "2":
        time_string = "TIME_SERIES_DAILY"
    elif time_series == "3":
        time_string = "TIME_SERIES_WEEKLY"
    else:
        time_string = "TIME_SERIES_MONTHLY"
    
    interval = (date2 - date1).days
    if (time_string == "TIME_SERIES_INTRADAY"):
        url = f'https://www.alphavantage.co/query?function={time_string}&symbol={symbol}&interval=5min&outputsize=full&apikey=Y5BQFD53B87D4N0O'
    else:
        url = f'https://www.alphavantage.co/query?function={time_string}&symbol={symbol}&outputsize=full&apikey=Y5BQFD53B87D4N0O'
    
    r = requests.get(url)
    data = r.json()

    
    return(data)

def filter_data_by_date(data, date1, date2, time_series_key): # DOESN'T WORK!!
    filtered_data = {}
    if (time_series_key == "Time Series (5min)"):
        for date, values in data[time_series_key].items():
            date_obj = datetime.strptime(date, "%Y-%m-%d %H:%M:%S").date()
            if date1 <= date_obj <= date2:
                filtered_data[date] = values
    else:
        for date, values in data[time_series_key].items():
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
            if date1 <= date_obj <= date2:
                filtered_data[date] = values
    
    return filtered_data

def graph(data, symbol, time_series, date1, date2, chart_type):
    time_series_keys = {
        "1": "Time Series (5min)",
        "2": "Time Series (Daily)",
        "3": "Weekly Time Series",
        "4": "Monthly Time Series"
    }

    time_series_key = time_series_keys.get(time_series)
    if time_series_key not in data:
        print("Error: No data available")
        return
    
    time_series_data = filter_data_by_date(data, date1, date2, time_series_key)
    #for date, values in data[time_series_key].items():
    #    time_series_data[date] = values

    if not time_series_data:
        print("No data available for the given date range.")
        return
    
    dates = []
    close = []
    opens = []
    high = []
    low = []
    
    # Extract dates and closing prices from the filtered data
    for date, values in sorted(time_series_data.items()):
        dates.append(date)
        close.append(float(values["4. close"]))  # Use the closing price for plotting
        opens.append(float(values["1. open"]))
        high.append(float(values["2. high"]))
        low.append(float(values["3. low"]))

    
    # Create the chart
    if chart_type == "2":  # Line chart
        line_chart = pygal.Line()
        line_chart.title = f"Stock data for {symbol}: {date1} to {date2}"
        line_chart.x_labels = dates
        line_chart.add("Close", close)
        line_chart.add("Open", opens)
        line_chart.add("High", high)
        line_chart.add("Low", low)
        line_chart.render_in_browser()  # Display in the browser
    else:
        bar_chart = pygal.Bar()
        bar_chart.title = f"Stock data for {symbol}: {date1} to {date2}"
        bar_chart.x_labels = dates
        bar_chart.add("Close", close)
        bar_chart.add("Open", opens)
        bar_chart.add("High", high)
        bar_chart.add("Low", low)
        bar_chart.render_in_browser()  # Display in the browser

def main():
    print("Stock Data Visualizer")
    print("-" * 10)

    while True:
        stock = getStock()
        chart = getChart()
        time = getTimeSeries()
        date1, date2 = getDate()
        
        data = get_JSON_data(stock, time, date1, date2)
        graph(data, stock, time, date1, date2, chart)

        repeat = input("Would you like to view more stock data? Press 'y' to continue: ").strip().lower()
        if repeat != 'y':
            print("Thank you and goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()
