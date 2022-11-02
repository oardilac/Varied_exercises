def palindrome(word: str) -> bool:
    word = word.replace(" ", "")
    word = word.lower()
    inverted_word: str = word[::-1]
    if word == inverted_word:
        return True
    else:
        return False


def run():
    word: str = input("Enter a word, I will check if it is palindrome: ")
    is_palindrome: bool = palindrome(word)
    if is_palindrome == True:
        print("Yes, it is palindrome")
    else:
        print("No, it is not palindrome")


if __name__ == "__main__":
    run()
