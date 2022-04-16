def main():
    text = input('Введите текст:\t')
    s = input('Введите образец:\t')
    print(FASearch(s, text))


def FASearch(s, text):
    alphabet = getAlphabet(s)
    FA = getFAForSubstring(s)
    state = 0
    length = len(alphabet)
    for i in range(len(text)):
        isFind: bool = bool(FA[state][length])
        if FA[state][length]:
            return i - FA[state][length] + 1
        state = FA[state][alphabet.index(text[i])]
    return 'Не найдено'


def getFAForSubstring(s):
    alphabet = getAlphabet(s)
    FA = [[0 for i in range(len(alphabet) + 1)] for i in range(len(s))]
    FA[0][0] = 1
    length = 0
    for i in range(1, len(s)):
        FA[i] = FA[length].copy()
        FA[i][alphabet.index(s[i])] = i + 1
        length = FA[length][alphabet.index(s[i])]
    FA[-1][-1] = len(s)
    return FA


def getAlphabet(string):
    alphabet = []
    for i in string:
        if i not in alphabet:
            alphabet.append(i)
    return alphabet


main()
