def verify_card_number(card_number: str) -> str:

    cleaned = ''.join(filter(str.isdigit, card_number))
    
    if len(cleaned) < 2:
        return "INVALID!"
    
    digits = [int(d) for d in cleaned]
    

    for i in range(len(digits) - 2, -1, -2):
        doubled = digits[i] * 2
        digits[i] = doubled - 9 if doubled > 9 else doubled
    

    total = sum(digits)
    
    
    return "VALID!" if total % 10 == 0 else "INVALID!"
print(verify_card_number('4111-1111-1111-1111'))
print(verify_card_number('1234 5678 9012 3456'))