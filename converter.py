from bs4 import BeautifulSoup as bs
import requests
import sys
def err(a):
    print("\33[91m\33[1m",a.capitalize(),"\033[m")
def succ(a):
    print("\33[32m\33[1m",a.capitalize(),"\033[m")
def convert():
    currency_from = input("Enter the currency you want to convert from >>: ").lower()
    if(currency_from=="exit"):
        err("Program Exited")
        sys.exit();
    currency_to = input("Enter the currency you want to convert to >>: ").lower()
    if(currency_to=="exit"):
        err("Program Exited")
        sys.exit();
    amount =  input("Enter the amount >>: "
            )
    if(amount=="exit"):
        err("Program Exited")
        sys.exit();
    print("Converting.............")
    url = f"https://transferwise.com/us/currency-converter/{currency_from}-to-{currency_to}-rate?amount={amount}"
    get = requests.get(url)
    soup = bs(get.text, 'html.parser')
    if(soup.find(id='cc-amount-to')):
        amount_to=soup.find(id='cc-amount-to')['value']
        succ(f'{amount} {currency_from} is {amount_to} in {currency_to}')
    else:
        err("Could not convert currency. Check your inputs and try again.");
def welcome():
    succ("Welcome to Currency converter v1.0")
    print("Enter the short form of the currencies e.g dollars is usd, naira is ngn\nMake sure the shortform is correct else it won\'t  work.","\nEnter \33[91mexit\033[m at any time to exit\n")

if __name__=='__main__':
    welcome();
    while True:
        convert()
