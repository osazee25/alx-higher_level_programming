#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    prev_val = 0

    for numeral in roman_string[::-1]:  # Iterate the string in reverse order
        current_val = roman_dict[numeral]

        if current_val < prev_val:
            result -= current_val
        else:
            result += current_val

        prev_val = current_val

    return result
