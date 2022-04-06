from pywubi import wubi
import re


def get_wubi(word):
    if re.match(r'[a-zA-Z]+', word):
        return word
    res = wubi(word, single=False)
    if not res:
        return 'error' + word
    return res[0]


def clean_data(line):
    word, bword = line.split('\t')
    emojis = bword.replace(word + " ", '').split(' ')
    wubi = get_wubi(word)
    lst = []
    for i, emoji in enumerate(emojis):
        idx = i + 2
        lst.append(f'{wubi},{idx}={emoji}')
    return lst


if __name__ == '__main__':
    f = open('es.txt', 'r', encoding='utf8')
    w = open('word.txt', 'w', encoding='utf8')
    res = []
    for line in f.read().splitlines():
        res.extend(clean_data(line))
    for word in res:
        w.write(word + '\n')
