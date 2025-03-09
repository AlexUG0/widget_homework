import pandas as pd


def read_transactions_from_csv(file_path):
    """Функция считывает финансовые операции из CSV файла"""
    try:
        df = pd.read_csv(file_path, sep=';')
        transactions = df.fillna(value=0).to_dict(orient="records")
        return transactions
    except Exception:
        raise


def read_transactions_from_excel(path):
    """Функция считывает финансовые операции из Excel файла"""
    try:
        df = pd.read_excel(path)
        transactions = df.fillna(value=0).to_dict(orient="records")
        return transactions
    except Exception:
        raise
