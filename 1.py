"""
"memoryUsed": "0.00",
"timeUsed": "0.012",
"passedTests": 6,
"score": 100,
"""

def letters_r_and_m(word: str) -> str:
    """
    Определяет правильность составленного слова
    :param word: string Слово, которое проверяется на правильность
    :return: Yes/No

    >>> letters_r_and_m("SMR")
    'No'
    >>> letters_r_and_m("RSM")
    'Yes'
    """
    if word.rfind("R") < word.rfind("M"):
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    created_word = input()
    print(letters_r_and_m(created_word))

