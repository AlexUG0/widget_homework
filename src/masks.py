import logging
import os

from config import PATH_HOME

# Основная конфигурация logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=os.path.join(PATH_HOME, "logs", "masks.log"),  # Запись логов в файл
    filemode="w",
)  # Перезапись файла при каждом запуске
logger = logging.getLogger("masks.py")


def get_mask_card_number(card_number: str) -> str:
    """Функция  принимает на вход номер карты и возвращает маску номера"""

    logger.info("Маскировка банковской карты")
    if len(card_number) == 16 and card_number.isdigit():
        mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        return mask_card_number
    else:
        logger.error("Введены некорректные данные")
        return "Неверный формат ввода"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает маску номера"""

    logger.info("Маскировка банковской счета")
    if len(account_number) == 20 and account_number.isdigit():
        mask_account = "**" + account_number[-4:]
        return mask_account
    else:
        logger.error("Введены некорректные данные")
        return "Неверный формат ввода"
