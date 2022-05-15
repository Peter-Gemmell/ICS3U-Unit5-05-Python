#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on may 2022
# This program format the mailing adress


def mail_adress(
    full_name,
    street_number,
    street_name,
    city_name,
    province,
    postal_code,
    apartment_number=None,
):

    # process
    if apartment_number is not None:
        full_adress = "{0} \n{1}-{2} {3} \n{4} {5}  {6}".format(
            full_name,
            apartment_number,
            street_number,
            street_name,
            city_name,
            province,
            postal_code,
        )
    else:
        full_adress = "{0} \n{1} {2} \n{3} {4} {5}".format(
            full_name, street_number, street_name, city_name, province, postal_code
        )

    return full_adress.upper()


def main():
    # user answers prompts and outputs mailing address
    apartment = None

    # input & output
    print("This program formats your address to a mailing address.")
    full_name = input("Enter your full name: ")
    question_for_user = input("Do you live in an apartment? (y/n): ")
    if question_for_user.upper() == "Y" or question_for_user.upper() == "YES":
        apartment_number = input("Enter your apartment number: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter your street name: ")
    city_name = input("Enter your city name: ")
    province = input("Enter your province (ON, BC): ")
    postal_code = input("Enter your postal code: ")

    try:
        street_number_int = int(street_number)

        if street_number_int < 0:
            print("")
            print("That is an invalid number.")
        elif apartment is not None:
            apartment_int = int(apartment_number)
            if apartment_int < 0:
                print("")
                print("That is an invalid number.")
            else:
                prompt_list = mail_adress(
                    full_name,
                    street_number,
                    street_name,
                    city_name,
                    province,
                    postal_code,
                    apartment_number,
                )
                print("")
                print(prompt_list)
        else:
            prompt_list = mail_adress(
                full_name, street_number, street_name, city_name, province, postal_code
            )
            print("")
            print(prompt_list)

    except Exception:
        print("")
        print("That is an invalid response, please try again.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
