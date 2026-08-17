# удаление знаков препинания
def remove_punctuation(text):
    punct = """!'()",.:;?{}"""
    result = ""

    for char in text:
        if char not in punct:
            result += char

    return result


# количество слов
def count_words(words):
    return len(words)


# самое длинное слово
def find_longest_word(words):
    return max(words, key=len)


# количество гласных
def count_vowels(text):
    vowels = "аеёиоуыэюя"
    counter = 0

    for char in text:
        if char in vowels:
            counter += 1

    return counter


# подсчитывает, сколько раз каждое слово встречается в тексте
def count_word_frequency(words):
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


# вызов функций и вывод
def main():
    text = input("Введите текст: ").lower().strip()

    if not text:
        print("Ошибка: Пустая строка")
        return

    text_without_punct = remove_punctuation(text)
    words = text_without_punct.split()

    print(f"Самое длинное слово: {find_longest_word(words)}")
    print(f"Количество слов: {count_words(words)}")
    print(f"Количество гласных: {count_vowels(text)}")
    print(count_word_frequency(words))


main()