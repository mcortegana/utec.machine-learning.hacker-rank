sentence = input()


def generate_palindrome_sentence(sentence: str) -> str:
    palindrome: str = sentence[::-1]
    return f'{sentence}{palindrome}'


print(generate_palindrome_sentence(sentence))
