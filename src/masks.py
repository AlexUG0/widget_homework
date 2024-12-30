def get_mask_card_number(card_number: str) -> str:
    """Функция  принимает на вход номер карты и возвращает маску номера"""

    mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает маску номера"""

    mask_account = "**" + account_number[-4:]
    return mask_account
