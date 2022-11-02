import random
import string


def generate_password() -> str:
    mayus: str = list(string.ascii_uppercase)
    minus: str = list(string.ascii_lowercase)
    symbols: str = list(string.punctuation)
    numbers: int = list(string.digits)

    characters_list = mayus + minus + symbols + numbers

    password = []

    for i in range(15):
        random_character = random.choice(characters_list)
        password.append(random_character)

    password: str = "".join(password)
    return password


def run():
    password: str = generate_password()
    print(f"Your new password is: {password}")


if __name__ == '__main__':
    run()