sentence = input().lower()


def consonant_counter(word: str) -> int:
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    counter = 0

    for letter in word.replace(" ", "").strip():
        if letter not in vowels:
            # if letter not in consonants:
            counter += 1

    return counter


print(consonant_counter(sentence))
