from collections import Counter


# удаление знаков препинаний
def remove_punctuation(text):
    punct = """!'()",.:;?{}"""
    result = ""

    for char in text:
        if char not in punct:
            result += char

    return result


# кол-во слов
def count_words(words):
    counter = 0

    for i in words:
        counter += 1

    return counter


# самое длинное слово
def find_longest_word(words):
    return max(words, key=len)


# кол-во глассных
def count_vowels(text):
    vowels = "аеёиоуыэюя"
    counter = 0

    for char in text:
        if char in vowels:
            counter += 1

    return counter


# Подсчитывает, сколько раз каждое слово встречается в тексте
def count_word_frequency(words):
    return Counter(words)


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
