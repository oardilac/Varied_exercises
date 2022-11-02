YELLOW = "\033[33m"
BLUE = "\033[36m"
RESET = "\033[39m"

menu = """
(☞ﾟヮﾟ)☞ Welcome to this currency converter. 💸💵

    1 - Colombian Pesos   --> DOLARES
    2 - Mexican Pesos     --> DOLARES
    3 - Argentinas Pesos  --> DOLARES
    4 - Peruvian Soles    --> DOLARES
    5 - Bolivians         --> DOLARES
    6 - Euros             --> DOLARES
    7 - Chilean Pesos     --> DOLARES
    8 - Brazilian reals   --> DOLARES

    0 - Exit

Select an option: \n"""

option: float = float(input(menu))

def conversion(currency_name: str, dollar_value: int):
    bagde = float(input("Which " + BLUE + currency_name +
                        RESET + " you have?: " + BLUE))
    dollars: int = bagde / dollar_value
    dollars = round(dollars, 2)
    bagde: str = str(bagde)
    dollars = str(dollars)
    print("")
    print(RESET + "You have " + YELLOW + dollars + " dolars" + RESET +
          ", i.e. " + BLUE + bagde + " " + currency_name + RESET + ".")


if option == 1:
    conversion("colombian pesos", 3500)

elif option == 2:
    conversion("mexican pesos", 19.92)

elif option == 3:
    conversion("argentina pesos", 83.28)

elif option == 4:
    conversion("peruvian Soles", 3.61)

elif option == 5:
    conversion("bolivians", 6.93)

elif option == 6:
    conversion("euros", 0.82)

elif option == 7:
    conversion("chilean pesos", 714.80)

elif option == 8:
    conversion("brazilian reals", 5.22)

elif option == 0:
    print("Bye.")

else:
    print(f"Please enter {BLUE} a correct opt" +
          RESET + " (Pon solo el número). ")
