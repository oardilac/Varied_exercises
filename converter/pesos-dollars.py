pesos: str = input("Which dolars do you have? ")
pesos = float(pesos)
dollar_value: int = 3500
dollars = pesos / dollar_value
dollars = round(dollars, 2)
dollars = str(dollars)
print(f"Tienes $ {dollars} dólares")