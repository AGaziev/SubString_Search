def main():
    text = input('Введите текст:\t')
    s = input('Введите образец:\t')
    print(BMSearch(s, text))


def BMSearch(s, TEXT):
    shift = getShiftingTable(s)  # таблица сдвигов
    print(shift)
    textIt = len(s) - 1  # итератор в тексте
    ex = len(s) - 1  # итератор в образце
    lastText = textIt  # последняя позиция итератора в тексте до сравнения
    while textIt < len(TEXT):
        if TEXT[textIt] == s[ex]:  # если есть совпадения
            textIt -= 1
            ex -= 1
        elif textIt != lastText:  # если были совпадения
            textIt = lastText + shift.get(s[-1])
            lastText = textIt
            ex = len(s) - 1
        else:  # если совпадений не было
            textIt = lastText + shift.get(TEXT[textIt], len(s))  # получаем сдвиг или сдвигаем на длину строки
            lastText = textIt
            ex = len(s) - 1
        if ex < 0:  # дошли до начала образца
            return textIt + 1  # добавляем 1 так как перед выводом вычли 1 из textIt
    return 'Не найдено'


def getShiftingTable(s):
    shift = {}
    for i in range(len(s) - 2, -1, -1):
        if s[i] not in shift.keys():
            shift[s[i]] = len(s) - 1 - i  # сдвиг равен отдаленности от конца образца
    if s[-1] not in shift.keys():  # если последний символ не был указан в таблице сдвигов
        shift[s[-1]] = len(s)
    return shift


main()
