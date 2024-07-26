#Luhn Algorithm 1111111111111111

def verify_card_number(card_number):
    card_translation = str.maketrans({"-": '', " ": ''})
    translated_card_number = card_number.translate(card_translation)
    if len(translated_card_number) != 16 or not translated_card_number.isdigit():
        #random return value to have for other options other than True and False
        return 'sad'
    else:
        sum_of_odd_digits = 0
        card_number_reversed = translated_card_number[::-1]
        odd_digits = card_number_reversed[::2]

        for digit in odd_digits:
            sum_of_odd_digits += int(digit)

        sum_of_even_digits = 0
        even_digits = card_number_reversed[1::2]
        for digit in even_digits:
            number = int(digit) * 2
            if number >= 10:
                number = (number // 10) + (number % 10)
            sum_of_even_digits += number
        total = sum_of_odd_digits + sum_of_even_digits
        return total % 10 == 0


def main():
    print('Type \'exit\' to close the program')
    while True:
        custom_input = input('Enter a card number: \n')
        if custom_input == 'exit':
            break
        result = verify_card_number(custom_input)
        if result == 'sad':
            print('Card numbers consist only of digits and only 16 of them!')
        elif result:
            print('Valid!')
            break
        else:
            print('Invalid!')
            break


main()