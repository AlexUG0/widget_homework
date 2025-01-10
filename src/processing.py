def filter_by_state(transaction_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает на вход список транзакций и возвращает список, отфильтрованный по состоянию"""

    state_filter_list = []
    for transaction in transaction_list:
        if transaction["state"] == state:
            state_filter_list.append(transaction)
    return state_filter_list


def sort_by_date(transaction_list: list[dict]) -> list[dict]:
    """Функция принимает на вход список транзакций и возвращает список, отсортированный по дате"""

    date_sort_list = sorted(transaction_list, key=lambda transaction: transaction["date"], reverse=True)
    return date_sort_list
