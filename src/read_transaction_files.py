import pandas as pd
import csv


def read_transactions_from_csv(path):
    """функция возвращает список словарей с данными о транзакциях"""
    try:
        with open(path, encoding="utf-8") as file:
            try:
                reader = pd.read_csv(file, delimiter=";")
                dict_trans = reader.to_dict(orient="records")
            except csv.Error as e:
                return []
    except FileNotFoundError:
        return pd.DataFrame()


def read_transactions_from_exel(path):
    try:
        df = pd.read_excel(path)
        return df.to_dict(orient="records")
    except FileNotFoundError:
        return "{}"
    except ValueError as e:
        return "{}"