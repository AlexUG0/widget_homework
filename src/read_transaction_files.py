import pandas as pd


def read_transactions_from_csv(file_path):
    """Функция считывает финансовые операции из CSV файла"""
    try:
        df = pd.read_csv(file_path)
        transactions = df.to_dict(orient="records")
        return transactions
    except Exception:
        raise


def read_transactions_from_excel(file_path):
    """Функция считывает финансовые операции из Excel файла"""
    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient="records")
        return transactions
    except Exception:
        raise
