# Kipland Melton
# 04/12/2021
# Simple Stock price and Crypto price comparator

def productPrint(typeAmount,firstVal,secondVal):
    print('\n{} shares at {} equal {}'.format(typeAmount,firstVal,round(typeAmount*firstVal,2)))
    print('\n{} shares at {} equal {}'.format(typeAmount,secondVal,round(typeAmount*secondVal,2)))

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

    productPrint(shareAmount,firstVal,secondVal)

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

    productPrint(coinAmount,firstVal,secondVal)

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