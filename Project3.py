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


def main():
    print("Stock Data Visualizer")
    print("-" * 10)
    
    stock = getStock()
    print(stock)
    chart = getChart()
    print(chart)
    time = getTimeSeries()
    print(time)

if __name__ == "__main__":
    main()



