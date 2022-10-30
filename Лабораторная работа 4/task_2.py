def get_count_char(str_):
    spisok_ = {}
    str_ = ''.join(str_.split())
    str_ = str_.lower()
    for spisok_bukv in str_:
        if spisok_bukv.isalpha():
            if spisok_bukv in spisok_:
                spisok_[spisok_bukv] = spisok_[spisok_bukv] + 1
            else:
                spisok_[spisok_bukv] = 1
    return spisok_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
