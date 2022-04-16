def main():
    text = 'ABCBCBABBBABAAACBABCBA'
    s = 'CBCB'
    print(BMSearch(s, text))


def BMSearch(s, text):
    shift = getShiftingTable(s)  # таблица сдвигов
    print(shift)
    k = len(s) - 1  # итераторы на конец образца
    l = len(s) - 1
    lastk = k
    while k < len(text):
        if l < 0:  # дошли до начала образца
            return k + 2  # добавляем 1 так как перед выводом вычли 1 из k
        if text[k] == s[l]:
            k -= 1
            l -= 1
        elif k != lastk:  # если были совпадения
            k = lastk + shift.get(s[-1])
            lastk = k
            l = len(s) - 1
        else:
            k = lastk + shift.get(text[k], len(s))  # получаем сдвиг или сдвигаем на длину строки
            lastk = k
            l = len(s) - 1
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
