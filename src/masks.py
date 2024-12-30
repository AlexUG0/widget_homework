def get_mask_card_number(card_number: str) -> str:
    """Функция  принимает на вход номер карты и возвращает маску номера"""

    if card_number.isdigit() and len(card_number) == 16:
        mask_card_number = card_number[:4] + " " + card_number[4:6] + "** " + 4 * "*" + " " + card_number[-4:]
        return mask_card_number
    else:
        return "Введен некорректный номер карты"


def get_mask_account(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает маску номера"""
    if account.isdigit() and len(account) == 20:
        mask_account = "**" + account[-4:]
        return mask_account
    else:
        return "Введен некорректный номер счета"
