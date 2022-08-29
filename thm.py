from ssl import AlertDescription


investment_in_bitcoin = 1.2
bitcoin_to_usd = 40000

def bitcoinToUSD(bitcoin_amount, boitcoin_value_usd):
    usd_value = bitcoin_amount * boitcoin_value_usd
    return usd_value

answer = bitcoin_to_usd(1.2, 40000)

if answer <=30000:
    print("alert")

