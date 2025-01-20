def get_mask_card_number(card_number: str) -> str:
    """Функция  принимает на вход номер карты и возвращает маску номера"""
    if len(card_number) == 16 and card_number.isdigit():
        mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        return mask_card_number
    else:
        return "Неверный формат ввода"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает маску номера"""

    if len(account_number) == 20 and account_number.isdigit():
        mask_account = "**" + account_number[-4:]
        return mask_account
    else:
        return "Неверный формат ввода"
