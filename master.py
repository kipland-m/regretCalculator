"""
Takes one stock price and compares # of shares to current stock price
Example:

    Past value | 131.24
    Present/Future value | 89.21
    Different calculator for crypto price

Once enter in values enter in # / quanity of crypto of shares to be compared
"""

def stockCalc():
    while True:
        try:
            firstVal = float(input("first value: "))
            secondVal = float(input("second value: "))
            shareAmount = int(input("enter # of shares (whole number): "))
            break
        except ValueError:
            print("not a number, try again")
            continue

    print('\n{} {} {} {} {}'.format(shareAmount,"shares at",firstVal,"equal",round(shareAmount*firstVal,2)))
    print('\n{} {} {} {} {}'.format(shareAmount,"shares at",secondVal,"equal",round(shareAmount*secondVal,2)))

def cryptoCalc():
    while True:
        try:
            firstVal = float(input("first value: "))
            secondVal = float(input("second value: "))
            coinAmount = float(input("enter # of coins: "))
            break
        except ValueError:
            print("not a number, try again")
            continue

    print('\n{} {} {} {} {}'.format(coinAmount,"at",firstVal,"equal",round(coinAmount*firstVal,2)))
    print('\n{} {} {} {} {}'.format(coinAmount,"at",secondVal,"equal",round(coinAmount*secondVal,2)))

def main():

    print('\n{}\n{}'.format("1. Stock Comparator","2. Crypto Comparator"))
    StockOrCrypto = int(input("Choice: "))

    if StockOrCrypto == 1:
        print("\nStock Comparator Chosen")
        stockCalc()

    elif StockOrCrypto == 2:
        print("\nCrypto Comparator Chosen")
        cryptoCalc()




if __name__ == '__main__':
    main()