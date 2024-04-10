sentence = input().lower()
searched_letter = input().lower()


def letter_counter(sentence: str, searched_letter: str) -> int:
    counter = 0

    for letter in sentence:
        if letter == searched_letter:
            counter += 1

    return counter


print(letter_counter(sentence, searched_letter))
