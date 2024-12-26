import constants
import random
import math

# Write below this comment
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
def create_complexNumber(real_part : str , imaginary_part : str ) :
    return [real_part, imaginary_part]
def get_real_part(complexNumber : list) -> str :
    return complexNumber[constants.first_number]
def get_imaginary_part(complexNumber : list) -> str :
    if float(complexNumber[1]) >= constants.positive_number:
        return "+" + str(complexNumber[1])
    else:
        return str(complexNumber[1])
def to_string(complexNumber: list) -> str:
    real_part = get_real_part(complexNumber)
    imaginary_part = get_imaginary_part(complexNumber)
    return f"z={real_part}{imaginary_part}i"

#
# Write below this comment
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
"""def create_complexNumber(real_part : str , imaginary_part : str ) :
    return {"real_part": real_part, "imaginary_part": imaginary_part}
def get_real_part(complexNumber : dict) :
    return complexNumber["real_part"]
def get_imaginary_part(complexNumber : dict) :
    if int(complexNumber["imaginary_part"]) >= constants.positive_number:
        return "+" + str(complexNumber["imaginary_part"])
    else:
        return complexNumber["imaginary_part"]

def to_string(complexNumber)->str:
    return "z=" + str(get_real_part(complexNumber)) + str(get_imaginary_part(complexNumber)) + "i"""
#
# Write below this comment
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

def parse_and_add_complex_number(complex_number, complex_numbers_list):
    if '+' in complex_number:
        real_part, imaginary_part = complex_number.split('+')
        imaginary_part = imaginary_part.strip('i')
    else:
        if '-' in complex_number[constants.excluding_first_character:]:
            if complex_number[constants.first_number] == '-':
                real_part, imaginary_part = complex_number[constants.excluding_first_character:].split('-')
                real_part = '-' + real_part
            else:
                real_part, imaginary_part = complex_number[constants.excluding_first_character:].split('-')
            imaginary_part = '-' + imaginary_part.strip("i")
        else:
            if 'i' in complex_number:
                real_part = constants.positive_number
                imaginary_part = complex_number.strip('i')
            else:
                real_part = complex_number
                imaginary_part = constants.positive_number

    complex_numbers_list.append(create_complexNumber(real_part, imaginary_part))

def process_complex_numbers_strings(complex_numbers_strings, complex_numbers_list):
    for complex_number in complex_numbers_strings:
        parse_and_add_complex_number(complex_number, complex_numbers_list)

def generate_random_complex_numbers(list_length):
    complex_numbers_list = []
    while list_length > constants.positive_number:
        real_part = random.randint(constants.minimum_range, constants.maximum_range)
        imaginary_part = random.randint(constants.minimum_range, constants.maximum_range)
        complex_number = create_complexNumber(str(real_part), str(imaginary_part))
        complex_numbers_list.append(complex_number)
        list_length -= constants.increment
    return complex_numbers_list

def modulus(complex_number):
    real_part = float(get_real_part(complex_number))
    imaginary_part = float(get_imaginary_part(complex_number))
    return math.sqrt(real_part ** constants.power2 + imaginary_part ** constants.power2)

def is_prime(number):
    if number < constants.minimum_for_prime:
        return False
    for ala_la_care_imparti in range(constants.minimum_for_prime, int(math.sqrt(number)) + constants.increment):
        if number % ala_la_care_imparti == 0:
            return False
    return True

def longest_prime_difference_subarray(complex_numbers_list):
    list_length = len(complex_numbers_list)
    if list_length < constants.minimum_length_for_sequece:
        return []

    longest_subarray = []
    current_subarray = [complex_numbers_list[constants.first_number]]

    for complex_number in range(1, list_length):
        modulus_of_first_complex_number = modulus(complex_numbers_list[complex_number - 1])
        modulus_of_second_complex_number = modulus(complex_numbers_list[complex_number])
        diff = abs(modulus_of_second_complex_number - modulus_of_first_complex_number)

        if is_prime(int(diff)):
            current_subarray.append(complex_numbers_list[complex_number])
        else:
            if len(current_subarray) > len(longest_subarray):
                longest_subarray = current_subarray
            current_subarray = [complex_numbers_list[complex_number]]

    if len(current_subarray) > len(longest_subarray):
        longest_subarray = current_subarray

    return longest_subarray

def longest_alternating_subsequence_real_parts(complex_numbers_list):
    list_length = len(complex_numbers_list)
    if list_length == constants.empty_list:
        return []

    real_parts = [float(get_real_part(number)) for number in complex_numbers_list]

    longest_subsequence_ending_at_that_position = [[1, 1] for _ in range(list_length)]
    previos_number = [[constants.no_previous_number, constants.no_previous_number] for _ in range(list_length)]

    for number in range(constants.first_number_with_succesor, list_length):
        for before_number in range(number):
            if real_parts[number] > real_parts[before_number]:
                if longest_subsequence_ending_at_that_position[number][1] < longest_subsequence_ending_at_that_position[before_number][constants.first_number] + 1:
                    longest_subsequence_ending_at_that_position[number][1] = longest_subsequence_ending_at_that_position[before_number][constants.first_number] + 1
                    previos_number[number][1] = before_number
            elif real_parts[number] < real_parts[before_number]:
                if longest_subsequence_ending_at_that_position[number][constants.first_number] < longest_subsequence_ending_at_that_position[before_number][1] + 1:
                    longest_subsequence_ending_at_that_position[number][constants.first_number] = longest_subsequence_ending_at_that_position[before_number][1] + 1
                    previos_number[number][constants.first_number] = before_number

    maximum_length, last_index, direction = constants.default_length, constants.null_index, constants.decrement
    for number in range(list_length):
        for direction_at_index in range(constants.minimum_length_for_sequece):
            if longest_subsequence_ending_at_that_position[number][direction_at_index] > maximum_length:
                maximum_length = longest_subsequence_ending_at_that_position[number][direction_at_index]
                last_index = number
                direction = direction_at_index

    result = []
    while last_index != constants.no_previous_number:
        result.append(complex_numbers_list[last_index])
        last_index = previos_number[last_index][direction]
        direction = 1 - direction

    result.reverse()
    return result



#
# Write below this comment
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#

def print_menu():
    print("___________________________________")
    print("0. Exit program")
    print("1.Read a list of complex numbers")
    print("2. Display the entire list of numbers")
    print("3. Longest subarray of numbers where the difference between the modulus of consecutive numbers is a prime number")
    print("4. Longest alternating subsequence, when considering each number's real part")
    print("___________________________________")


def get_input(user_input="->"):
    return input(user_input)


def read_list_complex_numbers(complex_numbers_list):
    user_input = input("Complex numbers: ").strip()
    complex_numbers_strings = [number.strip() for number in user_input.split(',')]
    process_complex_numbers_strings(complex_numbers_strings, complex_numbers_list)

def display_all_complex_numbers(complex_numbers_list):
    for number in complex_numbers_list:
        print(to_string(number))

def choose_option(user_option, complex_numbers_list):
    if user_option == constants.read_complex_number_list:
        read_list_complex_numbers(complex_numbers_list)
    elif user_option == constants.display_complex_number_list:
            display_all_complex_numbers(complex_numbers_list)
    elif user_option == constants.longest_number_subarray_with_consecutive_numbers_difference_prime:
        longgest_prime_difference_subbaray = longest_prime_difference_subarray(complex_numbers_list)
        display_all_complex_numbers(longgest_prime_difference_subbaray)
    elif user_option == constants.longest_alternating_subsequence_considering_real_part:
        longest_alternating_subsequence_considering_real_part = longest_alternating_subsequence_real_parts(complex_numbers_list)
        display_all_complex_numbers(longest_alternating_subsequence_considering_real_part)

def start_program():
    print("The program started")
    complex_number_list = generate_random_complex_numbers(constants.default_numbers)
    print("Random numbers generated")
    while True:
        print_menu()
        user_option = get_input()
        if user_option == constants.exit_program:
            print("Bye!")
            break
        else:
            choose_option(user_option, complex_number_list)


if __name__ == "__main__":
    print("Make magic happen")
    start_program()



