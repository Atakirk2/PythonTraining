import requests
import sys

first_currency = input("Please enter the first currency:")

second_currency = input("Please enter the second currency that you want to convert:")

amount = float(input("Please enter the amount of the money:"))

url = "http://data.fixer.io/api/latest?access_key=2611783eddca7697e74a62ecb34b0931&base={}&symbols={}".format(
    first_currency, second_currency)

try:

    response = requests.get(url)

    data = response.json()

    print(amount, first_currency.upper(), "equals" ,float(data['rates']['TRY']) * amount, second_currency.upper())
except Exception:
    sys.stderr.write("Please enter a valid currency")