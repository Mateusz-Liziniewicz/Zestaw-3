def roman2int(roman_number):
    roman_to_arabic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    arabic_number = 0
    prev_value = 0

    for letter in reversed(roman_number):
        value = roman_to_arabic[letter]
        if value < prev_value:
            arabic_number -= value
        else:
            arabic_number += value
        prev_value = value

    return arabic_number

print(roman2int("III"))
print(roman2int("IV"))
print(roman2int("IX"))
print(roman2int("LVIII"))
print(roman2int("MCMXCIV"))
print(roman2int("MMXXIV"))
