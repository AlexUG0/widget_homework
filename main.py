from src.masks import get_mask_account, get_mask_card_number

print("Введите номер карты (16 цифр без пробелов): ")
user_card_number = input()
print(get_mask_card_number(user_card_number))

print("Введите номер счета (20 цифр без пробела): ")
user_account = input()
print(get_mask_account(user_account))
