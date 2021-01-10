#!/usr/bin/env python3

# Created by Sean McLeod
# Created on January 2021
# This program rounds off a number


def rounding_calculator(rounding_elements):
    # this function returns the rounded off number

    rounding_elements[0] = (rounding_elements[0]*10**rounding_elements[1]+0.5)
    rounding_elements[1] = ((int(rounding_elements[0]))
                            * 10**-rounding_elements[1])


def main():
    # gets the number to round off and decimal places
    rounding_elements = []

    # input
    number_to_round = input("Enter the number you want to round: ")
    decimal_places = input("Enter how many decimal places you "
                           "want to round by: ")
    print("\n")

    try:
        int_number_to_round = float(number_to_round)
        int_decimal_places = int(decimal_places)

        if int_number_to_round > 0 and int_decimal_places >= 0:
            rounding_elements.append(int_number_to_round)
            rounding_elements.append(int_decimal_places)

            # call functions
            rounding_calculator(rounding_elements)
            # output
            print("The rounded number is {}".format(rounding_elements[1]))

        else:
            print("The values should be positive")

    except Exception:
        print("This is not a number")


if __name__ == "__main__":
    main()
