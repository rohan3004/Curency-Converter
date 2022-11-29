from forex_python.converter import CurrencyRates #we are importing forex_python module and importing a class CurrencyRates
cr = CurrencyRates() #we are creating an instance of the class CurrencyRates
amount = int(input("Enter the amount you want to convert: "))
from_currency = input("Enter the currency code that has to be converted: ").upper()
to_currency = input("Enter the currency code to convert: ").upper()
print("You are converting", amount, from_currency, "to", to_currency,".")
output = cr.convert(from_currency, to_currency, amount) #we are calling covert function
print(f"The converted rate is: {output:.2f}")