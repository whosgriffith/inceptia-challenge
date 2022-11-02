_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1", "heladoFrozen"]


def validate_discount_code(discount_code):
    for available_code in _AVAILABLE_DISCOUNT_CODES:
        number_of_differences = 0
        char_pairs = zip(discount_code, available_code)

        for char1, char2 in char_pairs:
            if char1 != char2:
                number_of_differences += 1

        if number_of_differences < 3:
            return True

    return False


print(validate_discount_code("heladoFrozXN"))
