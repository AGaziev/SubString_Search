def main():
    text = input('Введите текст:\t')
    s = input('Введите образец:\t')
    print(BMSearch(s, text))


def BMSearch(s, text):
    shift = getShiftingTable(s)  # таблица сдвигов
    print(shift)
    text = len(s) - 1   # итератор в тексте
    ex = len(s) - 1     # итератор в образце
    lastText = text # последняя позиция итератора в тексте до сравнения
    while text < len(text):
        if text[text] == s[ex]: # если есть совпадения
            text -= 1
            ex -= 1
        elif text != lastText:  # если были совпадения
            text = lastText + shift.get(s[-1])
            lastText = text
            ex = len(s) - 1
        else: # если совпадений не было
            text = lastText + shift.get(text[text], len(s))  # получаем сдвиг или сдвигаем на длину строки
            lastText = text
            ex = len(s) - 1
        if ex < 0:  # дошли до начала образца
            return text + 1  # добавляем 1 так как перед выводом вычли 1 из text
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
