from collections import Counter

text = input("Введите текст: ").lower().strip()
if not text:
    print("Ошибка: Пустая строка")
    exit()

punct = """!'()",.:;?{}"""
vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
text_no_punctuation = ""
vowels_counter = 0
words_counter = 0
longest_word = ""

# удаление знаков препинаний
for i in text:
    if i not in punct:
        text_no_punctuation += i
text_words = text_no_punctuation.split()

# самое длинное слово
longest_word = max(text_words, key=len)

# подсчет слов
for i in text_words:
    words_counter += 1

# подсчет гласных
for i in text:
    if i in vowels:
        vowels_counter += 1

print(f"самое длинное слово: {longest_word}")
print(f"кол-во слов: {words_counter}")
print(f"кол-во гласных: {vowels_counter}")
print(Counter(text_words))
