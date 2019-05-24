from __future__ import print_function


american_number_system = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 1000,
    'million': 1000000,
    'billion': 1000000000,
    'point': '.'
}

decimal_words = ['zero', 'one', 'two', 'three', 'four',
                 'five', 'six', 'seven', 'eight', 'nine']


def number_formation(number_words):
    numbers = []
    for number_word in number_words:
        if number_word == 'and':
            continue
        numbers.append(american_number_system[number_word])
    if len(numbers) == 4:
        return (numbers[0] * numbers[1]) + numbers[2] + numbers[3]
    elif len(numbers) == 3:
        return numbers[0] * numbers[1] + numbers[2]
    elif len(numbers) == 2:
        if 100 in numbers:
            return numbers[0] * numbers[1]
        else:
            return numbers[0] + numbers[1]
    else:
        return numbers[0]


"""
function to convert post decimal digit words to numerial digits
input: list of strings
output: double
"""


def get_decimal_sum(decimal_digit_words):
    decimal_number_str = []
    for dec_word in decimal_digit_words:
        if(dec_word not in decimal_words):
            return 0
        else:
            decimal_number_str.append(american_number_system[dec_word])
    final_decimal_string = '0.' + ''.join(map(str,decimal_number_str))
    return float(final_decimal_string)


"""
function to return integer for an input `number_sentence` string
input: string
output: int or double or None
"""


def string_to_nums(number_sentence):
    if type(number_sentence) is not str:
        raise ValueError("Type of input is not string! Please enter a valid "
                         "number word (eg. \'two million twenty three thousand and forty nine\')")

    number_sentence = number_sentence.replace('-', ' ')
    number_sentence = number_sentence.lower()  # converting input to lowercase

    split_words = number_sentence.strip().split()  # strip extra spaces and split sentence into words

    clean_numbers = []
    clean_number_sequence = []

    for i, word in enumerate(split_words):
        if word in american_number_system:
            if split_words[i - 1] in american_number_system or split_words[i - 1] == 'and':
                if split_words[i - 1] == 'and':
                    clean_number_sequence.append('and')
                clean_number_sequence.append(word)
            else:
                if len(clean_number_sequence) > 0:
                    clean_numbers.append(clean_number_sequence)
                    clean_number_sequence = []
                clean_number_sequence.append(word)
        elif word != 'and':
            if len(clean_number_sequence) > 0:
                clean_numbers.append(clean_number_sequence)
                clean_number_sequence = []
    if len(clean_number_sequence) > 0:
        clean_numbers.append(clean_number_sequence)

    # Error message if the user enters invalid input!
    if len(clean_numbers) == 0:
        raise ValueError("No valid number words found! Please enter a valid number word (eg. two million twenty three thousand and forty nine)") 

    total_sums = []

    for clean_number in clean_numbers:
        clean_decimal_number = []
        
        # Error if user enters million,billion, thousand or decimal point twice
        if clean_number.count('thousand') > 1 or clean_number.count('million') > 1 or clean_number.count('billion') > 1 or clean_number.count('point')> 1:
            raise ValueError("Redundant number word! Please enter a valid number word (eg. two million twenty three thousand and forty nine)")
        
        # separate decimal part of number (if exists)
        if clean_number.count('point') == 1:
            clean_decimal_number = clean_number[clean_number.index('point')+1:]
            clean_number = clean_number[:clean_number.index('point')]
        
        billion_index = clean_number.index('billion') if 'billion' in clean_number else -1
        million_index = clean_number.index('million') if 'million' in clean_number else -1
        thousand_index = clean_number.index('thousand') if 'thousand' in clean_number else -1
        
        if (thousand_index > -1 and (thousand_index < million_index or thousand_index < billion_index)) or (million_index>-1 and million_index < billion_index):
            raise ValueError("Malformed number! Please enter a valid number word (eg. two million twenty three thousand and forty nine)")
        
        total_sum = 0
        if len(clean_number) > 0:
            # hack for now, better way TODO
            if len(clean_number) == 1:
                if clean_number[0] == 'point':
                    continue
                total_sum += american_number_system[clean_number[0]]

            else:
                if billion_index > -1:
                    billion_multiplier = number_formation(clean_number[0:billion_index])
                    total_sum += billion_multiplier * 1000000000

                if million_index > -1:
                    if billion_index > -1:
                        million_multiplier = number_formation(clean_number[billion_index+1:million_index])
                    else:
                        million_multiplier = number_formation(clean_number[0:million_index])
                    total_sum += million_multiplier * 1000000

                if thousand_index > -1:
                    if million_index > -1:
                        thousand_multiplier = number_formation(clean_number[million_index+1:thousand_index])
                    elif billion_index > -1 and million_index == -1:
                        thousand_multiplier = number_formation(clean_number[billion_index+1:thousand_index])
                    else:
                        thousand_multiplier = number_formation(clean_number[0:thousand_index])
                    total_sum += thousand_multiplier * 1000

                if thousand_index > -1 and thousand_index != len(clean_number)-1:
                    hundreds = number_formation(clean_number[thousand_index+1:])
                elif million_index > -1 and million_index != len(clean_number)-1:
                    hundreds = number_formation(clean_number[million_index+1:])
                elif billion_index > -1 and billion_index != len(clean_numbers)-1:
                    hundreds = number_formation(clean_number[billion_index+1:])
                elif thousand_index == -1 and million_index == -1 and billion_index == -1:
                    hundreds = number_formation(clean_number)
                else:
                    hundreds = 0
                total_sum += hundreds
                
        if len(clean_decimal_number) > 0:
            decimal_sum = get_decimal_sum(clean_decimal_number)
            total_sum += decimal_sum

        total_sums.append(total_sum)

    clean_string = number_sentence

    for clean_number, total_sum in zip(clean_numbers, total_sums):
        clean_string = clean_string.replace(' '.join(clean_number), str(total_sum))
    
    return clean_string
