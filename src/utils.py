import json

# import os
# from config import PATH_HOME


def get_data_transactions_list(path):
    """Функция возвращает список словарей с данными о транзакциях"""
    try:
        with open(path, encoding="utf-8") as f:
            try:
                data_transactions_list = json.load(f)
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
    return data_transactions_list


# path_to_json = os.path.join(PATH_HOME, "data", "operations.json")
# print(get_data_transactions_list(path_to_json))
