from unittest.mock import mock_open, patch

from src.utils import get_data_transactions_list


def test_successful_read():
    mock_data = (
        '[{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041", "operationAmount": '
        '{"amount": "31957.58", "currency": '
        '{"name": "руб.", "code": "RUB"}}}]'
    )
    with patch("builtins.open", mock_open(read_data=mock_data)):
        data = get_data_transactions_list("path_to_file.json")
        assert data == [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {"name": "руб.", "code": "RUB"},
                },
            }
        ]


def test_file_not_found():
    """проверяем ответ, при некорректном пути к файлу json"""
    with patch("builtins.open", side_effect=FileNotFoundError):
        data = get_data_transactions_list("non_path_file.json")
        assert data == []


def test_json_decode_error():
    """проверяем ответ, при неккоректном json файле"""
    mock_data = (
        '[{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041", "operationAmount": '
        '{"amount": "31957.58", "currency": '
    )
    with patch("builtins.open", mock_open(read_data=mock_data)):
        data = get_data_transactions_list("uncorrect_file.json")

        assert data == []
