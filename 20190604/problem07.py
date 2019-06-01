def print_inputted_words():
    """
    get English words from user input until user input the word "exit"
    and return the dic of the English words
    unavailable to get inputted words included digits
    :return: dictionary: keys: initial alphabet, values: array of English words
    """
    words = []
    while True:
        word = input('input an English word: ')
        if word == 'exit':
            break
        if does_word_have_digit(word):
            print('there is a number in the English word')
            continue
        words.append(word)
    if not words:
        return words
    distinct_words = list(set(words))
    words_dic = make_words_dic_with_alphabet_key(distinct_words)

    print(words_dic)
    return words_dic


def does_word_have_digit(word):
    """
    check if the word include some digits
    :param word: string
    :return: bool: if word has digits, return True, else return False
    """
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for c in word:
        if c in digits:
            return True
    return False


def make_words_dic_with_alphabet_key(words):
    """
    make English words dictionary with initial alphabet key
    :param words: array of strings
    :return: sorted and organized dictionary
    """
    words_dic = {}
    capital_alphabets = [chr(i) for i in range(65, 65+26)]
    for c in capital_alphabets:
        words_dic[c] = []
    for word in words:
        initial_alphabet = word[0:1]
        capital_initial_alphabet = initial_alphabet.upper()
        words_dic[capital_initial_alphabet].append(word)
    return words_dic


def main():
    print_inputted_words()


main()
