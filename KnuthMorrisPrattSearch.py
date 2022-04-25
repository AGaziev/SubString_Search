def main():
    text = input('Введите текст:\t')
    s = input('Введите образец:\t')
    prefixFunc = getPrefixFunction(s)
    print(prefixFunc)
    print(KMPSearch(prefixFunc, s, text))


def KMPSearch(prefixFunc, s, text):
    textIter, exIter = 0, 0
    while textIter < len(text):
        if text[textIter] == s[exIter]:
            textIter += 1
            exIter += 1
            if exIter == len(s): # дошли до конца образца
                return textIter - exIter
        elif exIter == 0: # если не совпадает и не проходили по образу, то просто идем дальше
            textIter += 1
            if textIter == len(text):
                return 'Не найдено'
        else: # если прошли по образу, но не до конца, то сдвигаем по префикс функции итератор
            exIter = prefixFunc[exIter - 1]
    return 'Не найдено'


def getPrefixFunction(s):
    func = [0 for i in range(len(s))]
    j = 0
    i = 1
    while i < len(s):
        if s[j] == s[i]:
            func[i] = j + 1
            j += 1
            i += 1
        elif j == 0:
            func[i] = 0
            i += 1
        else:
            j = func[j - 1]
    return func


main()
