import random

GREEN = '\033[32m'
YELLOW = '\033[33m'
RED = '\033[31m'
RESET = '\033[39m'


def is_number_valid(number: int, limit: int) -> bool:
    if limit < number:
        print(f"\n{number} is greater than {limit} -_-, enter a number please")
    elif number < 1:
        print(f"\n{number} is smaller than 1 -_-, enter a number please")
    else:
        return True


def game(number: int, limit: int, difficulty: str):
    random_number: int = random.randint(1, limit)
    while number != random_number:
        if number > random_number:
            number = int(input(f"Enter a number is smaller than {number}: "))
        elif number < random_number:
            number = int(input(f"Enter a number is greater than {number}: "))

    print(f"\nCongrats!!!, el número era {str(random_number)} ganaste en dificultad {difficulty}.")


def game_3(number: int, limit: int, difficulty: str):
    random_number: int = random.randint(1, limit)
    attempts: int = 2
    while number != random_number and attempts <= 8:
        if number > random_number:
            number = int(input(f"(Intento #{attempts})Ingresa un número menor que {number}: "))
            attempts += 1
        elif number < random_number:
            number = int(input(f"(Intento #{attempts})Ingresa un número mayor que {number}: "))
            attempts += 1
    if number == random_number:
        print(f"\nCongrats!!!, the number was {str(random_number)} ganaste en dificultad {difficulty}.")
    else:
        print(f"\nYou lost, you ran out of attempts ￣へ￣, the number was {str(random_number)}.")


def run():
    menu: str = f"\nWelcome to the battle, where BLOOD is spilled!!!, you will have to guess the number. {GREEN} \n\n1. noob {YELLOW} 2. Pro {RED} 3. ULTRA MEGA PRO {RESET} \n\nChoose the difficult of the game: "
    option: int = int(input(menu))

    if option == 1:
        limit: int = 100
        difficulty: str = GREEN + " noob" + RESET
        number: int = int(
            input(f"\nOk{difficulty}, you have infinitive attemps, give me a number{GREEN} from 1 to 100: {RESET}"))
        if is_number_valid(number, limit) == True:
            game(number, limit, difficulty)
    elif option == 2:
        limit: int = 1000
        difficulty: str = YELLOW + " pro" + RESET
        number: int = int(
            input(f"\nOk{difficulty}, you have infinitive attempts, give me a number{YELLOW} from 1 to 1000: {RESET}"))
        if is_number_valid(number, limit) == True:
            game(number, limit, difficulty)
    elif option == 3:
        limit: int = 1000
        difficulty: str = RED + " ULTRA MEGA PRO" + RESET
        number: int = int(
            input(f"\nOk{difficulty}, you have 8 attempts, give me a number{RED} from 1 to 1000{RESET} (attempt #1): "))
        if is_number_valid(number, limit) == True:
            game_3(number, limit, difficulty)
    else:
        print("Write a valid option, please.")


if __name__ == "__main__":
    run()
