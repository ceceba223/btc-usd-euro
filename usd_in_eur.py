from forex_python.converter import CurrencyRates 

def usd_in_eur():
    c = CurrencyRates()
    EUR = c.get_rate('USD', 'EUR')  #convert USD to EURO
    return(EUR)
