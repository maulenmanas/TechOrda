import requests
class Account:
    def __init__(self, money = 0):
        self.__amount = money
    def addToBankAccount(self, add):
        self.__amount += add
    def substractFromBankAccount(self, minus):
        if self.__amount >= minus:
            self.__amount -= minus
        else:
            print("You don't have enough money in your bank account")
    def moneyConversion(self, amount, frm, to):

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={frm}&amount={amount}"

        payload = {}
        headers = {
            "apikey": "n81rYqGPEBhBHrE5wwFSkrTX2d2zF0dV"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        status_code = response.status_code
        result = response.json()
        if(status_code == 200):
            print(f'{amount} {frm} equals to {result["result"]} {to}')
        else:
            print("Error occurred")
    def __str__(self):
        return f"You have {self.__amount} KZT in your bank account"

if __name__ == '__main__':
    a = Account(100)
    print(a)
    a.addToBankAccount(50)
    print(a)
    a.substractFromBankAccount(13)
    print(a)
    a.moneyConversion(300, 'USD', 'KZT')