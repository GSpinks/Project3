from datetime import datetime
import sys

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
        time = input(f"\nSelect the Time Series of the chart you want to Generate\n{dash}\n1. Intraday\n2. Daily\n3. Weekly\n4. Monthly\n\nEnter the time series option (1, 2, 3, 4): ")
        if time == "1" or time == "2" or time == "3" or time == "4":
            return time
        else:
            print("Enter a 1, 2, 3, or 4, for Time Series")

def getDate():
    while True:
        dateStart = input("Enter the start Date (YYYY-MM-DD)")
        dateEnd = input("Enter the end Date (YYYY-MM-DD)")
        dateFormat = "%Y-%m-%d"
        try:
            date1 = datetime.strptime(dateStart, dateFormat).date()
            date2 = datetime.strptime(dateEnd, dateFormat).date()
            if date1 < date2:
                return date1, date2
            else:
                print("\nError: Start date cannot be later than End date. Enter the dates again.\n")
        except:
            print("\nWrong Date Format. Please try again.\n")







def main():
    while True:
        print("Stock Data Visualizer")
        print("-" * 10)
        
        stock = getStock()
        print(stock)
        chart = getChart()
        print(chart)
        time = getTimeSeries()
        print(time)
        date1, date2 = getDate()
        print(date1)
        print(date2)
        Repeat = input("Would you like to view more stock data? Press 'y' to continue: ").lower()
        if(Repeat != "y"):
            sys.exit()

if __name__ == "__main__":
    main()



