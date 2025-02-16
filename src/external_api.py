import os

import requests
from dotenv import load_dotenv

from config import PATH_HOME

# from utils import get_data_transactions_list


path_to_dotenv = os.path.join(PATH_HOME, ".env")
load_dotenv(path_to_dotenv)


def amount_transaction(transaction_by_id):
    """Функция возвращает сумму транзакции в рублях с конвертацией"""

    trans_amount = transaction_by_id["operationAmount"]["amount"]
    trans_code = transaction_by_id["operationAmount"]["currency"]["code"]
    api_key = os.getenv("API_KEY")
    headers = {"apikey": api_key}
    if trans_code == "RUB":
        return float(trans_amount)
    else:
        try:

            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={trans_code}&amount={trans_amount}"
            response = requests.get(url, headers=headers)
            my_result = response.json()
            return float(my_result["result"])
        except Exception as e:
            print(e)


# path_to_json = os.path.join(PATH_HOME, "data", "operations.json")
# transactions = get_data_transactions_list(path_to_json)
# for i in  range(3):
#     print(amount_transaction(transactions[i]))
