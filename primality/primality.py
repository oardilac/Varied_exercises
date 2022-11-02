RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[39m'


def is_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        counter = 0
        for i in range(1, number + 1):
            if i == 1 or i == number:
                continue
            if number % i == 0:
                counter += 1
        if counter == 0:
            return True
        else:
            return False


def run():
    number = int(input("Enter a number: "))
    if is_prime(number):
        print(f"The number enter {GREEN} is primality {RESET}")
    else:
        print(f"The number enter {RED} isn't primality {RESET}")


if __name__ == "__main__":
    run()
