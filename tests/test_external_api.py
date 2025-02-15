from unittest.mock import patch

from src.external_api import amount_transaction


@patch("src.external_api.requests.request")
def test_amount_transaction_rub(mock_request):
    mock_request.return_value.json.return_value = {"result": 31957.58}
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"},
        },
    }
    result = amount_transaction(transaction)
    assert result == "31957.58"


@patch("src.external_api.requests.request")
def test_amount_transaction_other_currency(mock_request):
    mock_request.return_value.json.return_value = {"result": 748686.186978}
    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {"name": "USD", "code": "USD"},
        },
    }

    result = amount_transaction(transaction)
    assert result == 748686.186978
