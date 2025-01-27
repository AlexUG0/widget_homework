from typing import Any


def filter_by_currency(transactions_list: list[dict], currency: str) -> Any:
    """Функция фильтрует список словарей транзакций по валюте"""
    for transaction in transactions_list:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions_list: list[dict]) -> Any:
    """Функция возвращает описание транзакции"""
    for transaction in transactions_list:
        yield transaction.get("description", "Данные о транзакции отсутствуют")


def card_number_generator(start: int, stop: int) -> Any:
    """Функция генерирует номера карт в формате ХХХХ ХХХХ ХХХХ ХХХХ в заданном диапазоне"""

    for number in range(start, stop + 1):
        card_number = f"{'0' * (16 - len(str(number)))}{number}" if len(str(number)) <= 16 else "None"
        yield " ".join([card_number[i : i + 4] for i in range(0, len(card_number), 4)])
