def main():
    text = input('Введите текст:\t')
    s = input('Введите образец:\t')
    print(FASearch(s, text))


def FASearch(s, text):
    alphabet = getAlphabet(s)
    FA = getFAForSubstring(s)
    state = 0
    for i, sym in enumerate(text):
        try:
            state = FA[state][alphabet.index(sym)]  # переходим в следующее состояние из автомата
        except ValueError:  # если в алфавите образца нет буквы которая есть в алфавите текста
            state = 0
        if state == len(s):  # если дошли до последнего состояния
            return i - state + 1
    return 'Не найдено'


def getFAForSubstring(s):
    alphabet = getAlphabet(s)
    FA = [[0 for i in range(len(alphabet))] for i in range(len(s))]
    FA[0][0] = 1
    length = 0
    for i in range(1, len(s)):
        FA[i] = FA[length].copy()                   #
        FA[i][alphabet.index(s[i])] = i + 1         # алгоритм построение конечного автомата
        length = FA[length][alphabet.index(s[i])]   #
    return FA


def getAlphabet(string):
    alphabet = []
    for i in string:
        if i not in alphabet:
            alphabet.append(i)
    return alphabet


main()
