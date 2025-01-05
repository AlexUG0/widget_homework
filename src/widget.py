from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_number: str) -> str:
    """Функция принимает на вход номер карты или счета и возвращает их маску"""
    if "Счет" in account_card_number:
        account_number = account_card_number[-20:]
        mask_account_number = get_mask_account(account_number)
        return f'{account_card_number[:-20]}{mask_account_number}'

    else:
        card_number = account_card_number[-16:]
        mask_card_number = get_mask_card_number(card_number)
        return f'{account_card_number[:-16]}{mask_card_number}'


def get_date(date_str: str) -> str:
    """Функция принимает на вход строку с датой и возвращает строку с датой в формате 'ДД.ММ.ГГГГ' """
    year = date_str[:4]
    month = date_str[5:7]
    day = date_str[8:10]
    formatted_date = f"{day}.{month}.{year}"
    return formatted_date
