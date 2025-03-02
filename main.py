import os

from config import DATA_DIR
from src.processing import filter_by_state
from src.read_transaction_files import read_transactions_from_csv, read_transactions_from_excel
from src.searchig import filter_transactions
from src.utils import get_data_transactions_list
from src.widget import get_date, mask_account_card


def print_transaction(transaction_dict):
    """Функция форматирования вывода данных"""
    amount = transaction_dict.get('amount') or transaction_dict.get('operationAmount')['amount']
    currency_out = transaction_dict.get('currency_name') or transaction_dict.get('operationAmount')['currency']['name']
    if transaction_dict.get('from') and transaction_dict.get('from') != "nan":
        print("\n"
              f"{get_date(transaction_dict.get('date'))} {transaction_dict.get('description')}\n"
              f"{mask_account_card(transaction_dict.get('from'))} -> {mask_account_card(transaction_dict.get('to'))}\n"
              f"Сумма: {amount} {currency_out}"
              )
    else:
        print("\n"
              f"{get_date(transaction_dict.get('date'))} {transaction_dict.get('description')}\n"
              f"{mask_account_card(transaction_dict.get('to'))}\n"
              f"Сумма: {amount} {currency_out}"
              )


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
          "Выберите необходимый пункт меню:\n"
          "1. Получить информацию о транзакциях из JSON-файла\n"
          "2. Получить информацию о транзакциях из CSV-файла\n"
          "3. Получить информацию о транзакциях из XLSX-файла\n"
          )

    choice = input()

    if choice == "1":
        file_path = os.path.join(DATA_DIR, "operations.json")
        transactions = get_data_transactions_list(file_path)
        print("Для обработки выбран JSON-файл.")
    elif choice == "2":
        file_path = os.path.join(DATA_DIR, "transactions.csv")
        transactions = read_transactions_from_csv(file_path)
        print("Для обработки выбран CSV-файл.")
    elif choice == "3":
        file_path = os.path.join(DATA_DIR, "transactions_excel.xlsx")
        transactions = read_transactions_from_excel(file_path)
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор.")
        return

    # Фильтрация по статусу
    states = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        state = (
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            )
            .strip()
            .upper()
        )
        if state in states:
            print(f'Операции отфильтрованы по статусу "{state}"')
            filtered_transactions = filter_by_state(transactions, state)
            break
        else:
            print(f'Статус операции "{state}" недоступен.')

    # Дополнительные фильтры
    sort_choice = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
    if sort_choice == "да":
        order_choice = input("Сортировать по возрастанию или по убыванию?\n").strip().lower()
        if order_choice == "по возрастанию":
            filtered_transactions.sort(key=lambda x: x["date"])
        elif order_choice == "по убыванию":
            filtered_transactions.sort(key=lambda x: x["date"], reverse=True)

    currency_choice = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
    if currency_choice == "да":
        # currency = filtered_transactions['currency_code'] or filtered_transactions.get('operationAmount')['currency']['code']
        filtered_transactions = [
            t for t in filtered_transactions
            if 'currency_code' in t and t['currency_code'] == "RUB"
               or "operationAmount" in t and t["operationAmount"]["currency"]["code"] == "RUB"
        ]

    description_filter = (
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
        .strip()
        .lower()
    )
    if description_filter == "да":
        search_string = input("Введите строку для поиска в описании: ")
        filtered_transactions = filter_transactions(filtered_transactions, search_string)

    # Вывод результатов
    print("Распечатываю итоговый список транзакций...")
    if filtered_transactions:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            print_transaction(transaction)
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
