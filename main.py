def convert_currency(amount, rate):
    return amount * rate

usd_to_eur = 0.85
amount_in_usd = 100
amount_in_eur = convert_currency(amount_in_usd, usd_to_eur)
print(amount_in_eur)
