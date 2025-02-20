import json
import logging
import os

from config import PATH_HOME

# Основная конфигурация logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=os.path.join(PATH_HOME, "logs", "utils.log"),  # Запись логов в файл
    filemode="w",
)  # Перезапись файла при каждом запуске
logger = logging.getLogger("utils.py")


def get_data_transactions_list(path):
    """Функция возвращает список словарей с данными о транзакциях"""

    try:
        logger.info("Открытие JSON файла")
        with open(path, encoding="utf-8") as f:
            try:
                logger.info("Получение списка транзакций")
                data_transactions_list = json.load(f)
            except json.JSONDecodeError:
                logger.error("Данные в файле не являются JSON")
                return []
    except FileNotFoundError:
        logger.error("Не найден путь к файлу operations.json")
        return []
    return data_transactions_list


path_to_json = os.path.join(PATH_HOME, "data", "operations.json")
print(get_data_transactions_list(path_to_json))
