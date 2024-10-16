def getStock():
    stock_symbol = input("Enter the stock symbol you are looking for: ")
    return stock_symbol
def getChart():
    while True:
        types = input("\nChart Types\n-------------\n1. Bar\n2. Line\n\nEnter the chart type you want (1, 2): ")
        if types == "1" or types == "2":
            return types
        else:
            print("Invalid input. Please enter 1 or 2.")


def main():
    print("Stock Data Visualizer")
    print("-" * 10)
    
    stock = getStock()
    print(stock)
    chart = getChart()
    print(chart)

if __name__ == "__main__":
    main()



