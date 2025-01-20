from datetime import datetime


def filter_by_state(transaction_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает на вход список транзакций и возвращает список, отфильтрованный по состоянию"""

    state_filter_list = []
    for transaction in transaction_list:
        if transaction.get("state") == state:
            state_filter_list.append(transaction)
    return state_filter_list


def sort_by_date(transaction_list: list[dict], reverse_order: bool = True) -> list[dict]:
    """Функция принимает на вход список транзакций и возвращает список, отсортированный по дате"""

    by_date_sort_list = sorted(
        transaction_list,
        key=lambda transaction: datetime.strptime(transaction.get("date"), "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=reverse_order,
    )
    return by_date_sort_list
