def hide(card_number):
    return card_number[:2] + "*"*10 + card_number[12:]


def main(insert):
    if len(hide(insert)) != 16:
        return "The length of card numbers must be 16 digit"
    return hide(insert)


print(main("5290312400019022"))