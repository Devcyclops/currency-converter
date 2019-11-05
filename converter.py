from bs4 import BeautifulSoup
import requests
def convert():
    print("Welcome to Currency converter v1.0\nEnter the shortform of the currencies eg dollars is usd, naira is ngn\nMake sure the shortform is correct else it won\'t  work")
    currency_from = input("Enter the currency you want to convert from >>: ").lower()
    currency_to = input("Enter the currency you want to convert to >>: ").lower()
    amount =  input("Enter the amount >>: ")
    print("Converting.............")
    url = f"https://transferwise.com/us/currency-converter/{currency_from}-to-{currency_to}-rate?amount={amount}"
    get = requests.get(url)
    soup = BeautifulSoup(get.text, 'html.parser')
    amount_to = soup.find(id='cc-amount-to')['value']
    print(f'{amount} {currency_from} is {amount_to} in {currency_to}')

convert()
