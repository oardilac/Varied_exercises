def run(number: int, limit: int):
    potency: int = 0
    result: int = number ** potency
    while result <= limit:
        print(str(number) + "^" + str(potency) +
              " = " + str(result))
        potency = potency + 1
        result = number ** potency


if __name__ == "__main__":
    number: int = int(input("What number do you want to potency? "))
    limit: int = int(input("What limit do you want to have? "))
    run(number, limit)