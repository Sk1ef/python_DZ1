# 2
with open('data.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# 3
with open('data.txt', 'a', encoding='utf-8') as file:
    file.write("\nУ лукоморья дуб зелёный")

# 4
with open('data.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())

# 5
with open('data.txt', 'rb') as file:
    content = file.read()
with open('data_copy.txt', 'wb') as file:
    file.write(content)