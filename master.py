"""
Takes one stock price and compares # of shares to current stock price
Example:

    Past value | 131.24
    Present/Future value | 89.21
    Different calculator for crypto price

Once enter in values enter in # of shares to be compared
"""

def main():

    print("""
    1. Stock Comparator
    2. Crypto Comparator
    """)

    print('{}\n{}'.format("1. Stock Comparator","2. Crypto Comparator"))

    StockOrCrpyto = int(input("Choice:"))

    if StockOrCrpyto == 1:
        print("Stock Comparator Chosen")
        pastVal = int(input("Please enter past stock value"))
    elif StockOrCrpyto == 2:
        print("Crypto Comparator Chosen")




if __name__ == '__main__':
    main()