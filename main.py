from usd_in_eur import usd_in_eur
from btc_in_usd import btc_in_usd
from btc_in_eur import btc_in_eur

from save import save, setup
import os.path

import time

def main():
    if os.path.isfile('data.xlsx'):
        pass
    else:
        setup()

    while True:
        BTC_USD = round(btc_in_usd(), 2)
        USD_EUR = round(usd_in_eur(), 2)
        BTC_EUR = round(btc_in_eur(BTC_USD, USD_EUR), 2)

        save(BTC_USD, BTC_EUR, USD_EUR)

        # Sleep for 24 hours 
        # (For testing purposes you can set it to a lower number)
        time.sleep(24 * 60 * 60)

if __name__ == '__main__':
    main()
