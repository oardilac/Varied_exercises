def is_prime(number: int) -> bool:
  contador: int = 0

  if number <= 1:
    return False

  for i in range(1, number + 1):
    if i == 1 or i == number:
      continue
    if number % i == 0:
      contador += 1
      break
  if contador == 0:
    return True
  else:
    return False  


def run():
    number = int(input("Write a number:  "))
    if is_prime(number):
        print(str(number) + " Is prime")
    else:
        print(str(number) + " Isn't prime")
      

if  __name__  == "__main__":
    run()