def f(amount_to_pay):
    five = amount_to_pay // 5
    remainder = amount_to_pay % 5

    two = remainder // 2
    remainder = remainder % 2

    one = remainder // 1
    total_coins=(five+two+one)
    return total_coins
def main():
    print( f(23)) #returns 6
    print( f(8))# returns 3
    print( f(2))#returns 1
    print( f(0))#returns 0
if __name__ == "__main__":
    main()