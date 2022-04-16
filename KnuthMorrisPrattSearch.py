def main():
    text = input('Введите текст:\t')
    s = input('Введите образец:\t')
    prefixFunc = getPrefixFunction(s)
    print(KMPSearch(prefixFunc, s, text))


def KMPSearch(prefixFunc, s, text):
    k, l = 0
    while k < len(text):
        if text[k] == s[l]:
            k += 1
            l += 1
            if l == len(s):
                return k - l
        elif l == 0:
            k += 1
            if k == len(text):
                return 'Не найдено'
        else:
            l = prefixFunc[l - 1]
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
