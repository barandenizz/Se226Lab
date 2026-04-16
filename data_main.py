from data_package import (
     remove_duplicates,
     strip_whitespaces,
     calculate_mean,
     find_maximum,
     find_maximum,
)
def main():
    user_input = input("Enter numbersseperated by commas: ")

    try:
        string_list = user_input.split(",")

        cleaned_strings = strip_whitespaces(string_list)

        numbers = [int(x) for x in cleaned_strings]

        numbers = remove_duplicates(numbers)

        mean = calculate_mean(numbers)
        maximum = find_maximum(numbers)
        minimum = find_minimum(numbers)

        print("Cleaned Numbers : ", numbers)
        print("Mean : ", mean)
        print("Max :", maximum)
        print("Min :", minimum)

    except Exception as e:
        print("Error:" , e)
