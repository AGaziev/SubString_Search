def main():
    text = 'ABACBCBABCBABCABBAAABC'
    s = 'CBA'
    print(RabinKarpSearch(s, text))


def RabinKarpSearch(s, text):
    sizeSubstring = len(s)
    alphabet = getAlphabetSize(text)
    hs = getHashOfString(s, alphabet)
    for i in range(len(text) - sizeSubstring):
        if hs == getHashOfString(text[i:i + sizeSubstring], alphabet):
            return i
    return 'Не найдено'


def getHashOfString(s, size):
    hr = 0
    m = len(s)
    for i in range(len(s)):
        hr += ord(s[i]) * (size ** (m-i))
    return hr


def getAlphabetSize(text):
    alphabet = set(list(text))
    return len(alphabet)


main()
