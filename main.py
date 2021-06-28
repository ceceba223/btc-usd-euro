from usd_in_eur import usd_in_eur
from btc_in_usd import btc_in_usd
from btc_in_eur import btc_in_eur

def main():
    BTC_USD = round(btc_in_usd(), 2)
    USD_EUR = round(usd_in_eur(), 2)
    print(BTC_USD)
    print(USD_EUR)
    print(round(btc_in_eur(BTC_USD, USD_EUR), 3))
    
    
    #while True:
    #    # Sleep for 24 hours 
    #    # (For testing purposes you can set it to a lower number)
    #    time.sleep(24 * 60 * 60)

if __name__ == '__main__':
    main()
