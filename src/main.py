#https://github.com/AliRaeisian/Practice-three-Functions-
def calculate_price(price, tax_rate):
    final_price = price * (1 + tax_rate)
    return final_price


def main():
    p = int(input())
    tax = input()
    if tax == '':
        tax = 0.1
    else:
        tax = float(tax)
    f_price = calculate_price(p, tax)
    print(f"{f_price}")


main()