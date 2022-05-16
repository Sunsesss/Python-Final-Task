def write_into_file(str1: list, str2: list):
        with open('res', "w", encoding="utf8") as file:
            file.write(str(len(str1)))
            file.write('\n')
            file.write(str(len(str2)))


def script():
    mass = ['что', 'на', 'и', 'а', 'как',
             '.', ':', ';', '[', ']', '<', '>', '(', ')', '«', '»', '!', '?', '…', '`', '——', '%']
    dictionary = {}

    with open('test', encoding="utf-8") as file:
        words = file.read().strip().lower().replace(',', '').replace('.', '').split()

    for w in words:
        if w not in mass:
            dictionary[w] = dictionary.get(w, 0) + 1

    return max(dictionary, key=dictionary.get)

def main():
    print(script())
    str1 = ''
    str2 = list()
    print('Введите слова через запятую')
    str1 = str(input()).split(",")
    print('Введите слова, для завершения процесса напишите stop')
    while True:
        word = input()
        if word == 'stop':
            break
        else:
            str2.append(word)
    write_into_file(str1, str2)

print(main())
