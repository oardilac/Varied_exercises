dollar: str = input("Which dolars do you have? ")
dollar = float(dollar)
peso_value: int = 0.00029
pesos: int = dollar / peso_value
pesos = round(pesos, 2)
pesos = str(pesos)
print(f"Tienes $ {pesos} pesos colombianos")
