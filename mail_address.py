#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on may 2022
# This program format the mailing adress


def format_address(
    full_name,
    house_number,
    street_name,
    city_name,
    province_name,
    postal_code,
    apartment_number=None,
):
    # format address

    # process
    if apartment_number == None:
        address = "\n{0}\n{1} {2}\n{3} {4}  {5}".format(
            full_name, house_number, street_name, city_name, province_name, postal_code
        )
    else:
        address = "\n{0}\n{1}-{2} {3}\n{4} {5}  {6}".format(
            full_name,
            apartment_number,
            house_number,
            street_name,
            city_name,
            province_name,
            postal_code,
        )
    address = address.upper()

    # output
    return address


def main():
    # this function gets the user input

    # input
    full_name_from_user = input("Enter your full name : ")
    apartment_answer_from_user = input("Do you live in an apartment? (y/n) : ")
    if apartment_answer_from_user == "y" or apartment_answer_from_user == "yes":
        apartment_number_as_string = input("Enter your apartment number : ")
    else:
        apartment_number_as_string = None
    house_number_as_string = input("Enter your house number : ")
    street_name_from_user = input(
        "Enter your street name and type (Main St, Country Dr... : "
    )
    city_name_from_user = input("Enter your city : ")
    province_name_from_user = input(
        "Enter your province (as an abbreviation, ex. ON, SK...) : "
    )
    postal_code_from_user = input("Enter your postal code (A1B 2C3) : ")

    # call function
    try:
        if (
            apartment_answer_from_user.upper() == "Y"
            or apartment_answer_from_user.upper() == "YES"
        ):
            apartment_number_from_user = int(apartment_number_as_string)
            house_number_from_user = int(house_number_as_string)
            formated_address = format_address(
                full_name_from_user,
                house_number_from_user,
                street_name_from_user,
                city_name_from_user,
                province_name_from_user,
                postal_code_from_user,
                apartment_number_from_user,
            )

        else:
            house_number_from_user = int(house_number_as_string)
            formated_address = format_address(
                full_name_from_user,
                house_number_from_user,
                street_name_from_user,
                city_name_from_user,
                province_name_from_user,
                postal_code_from_user,
            )

        print(formated_address)

    except Exception:
        print("\nInvalid input entered, please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
