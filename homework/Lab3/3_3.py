import re

def validate_id_card(id_card):
    pattern = r'^\d{17}[\dXx]$'
    return bool(re.match(pattern, id_card))

# 测试
print(validate_id_card('11010119900307458X'))  # True
print(validate_id_card('11010119900307458Y'))  # False