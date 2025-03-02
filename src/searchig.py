import re
from collections import Counter
from typing import Dict, List


def filter_transactions(transactions: List[Dict], search_string: str) -> List[Dict]:
    """функция принимает список словарей с данными о банковских операциях и строку поиска, а возвращает список словарей,
       у которых в описании есть данная строка"""
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)  # Компилируем шаблон
    filtered_transactions = [
        transaction for transaction in transactions if pattern.search(transaction.get("description", ""))
    ]
    return filtered_transactions


def count_transactions_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """Принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    description_list = [
        transaction.get("description")
        for transaction in transactions
        if transaction.get("description") in categories
    ]
    grouped_transactions = Counter(description_list)

    return dict(grouped_transactions)
