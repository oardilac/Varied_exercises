def table(number: int):
    print(f"\nThis is the table of {number}")
    for counter in range(1, 11):
        product = number * int(counter)
        print(f"{number} X {counter} = {product}")


def run():
    number: int = int(input("\nEnter a number to give the multiplication table: "))
    table(number)


if __name__ == "__main__":
    run()
