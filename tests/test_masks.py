import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "entered, masked",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("158300734726758", "Неверный формат ввода"),
        ("7896831982476737658", "Неверный формат ввода"),
        ("Visa Platinum", "Неверный формат ввода"),
        ("", "Неверный формат ввода"),
    ],
)
def test_get_mask_card_number(entered, masked):
    assert get_mask_card_number(entered) == masked


@pytest.mark.parametrize(
    "entered, masked",
    [
        ("64686473678894779589", "**9589"),
        ("353830334744478560", "Неверный формат ввода"),
        ("", "Неверный формат ввода"),
        ("Счет", "Неверный формат ввода"),
    ],
)
def test_get_mask_account(entered, masked):
    assert get_mask_account(entered) == masked
