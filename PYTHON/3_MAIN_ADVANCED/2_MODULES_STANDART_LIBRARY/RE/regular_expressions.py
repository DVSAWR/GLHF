import re


def preview(x):
    print(f'\n---- {x} ----')


text = 'abbbbc abbbbc12345 !*?@#$%ZXC'

preview('Специальные символы')
#

preview('.')
# любой символ

print(re.search(r'.', text))

preview('^')
# начало строки
print(re.search(r'^.', text))

preview('$')
# конец строки
print(re.search(r'.$', text))

preview('*')
# 0 или более повторений
print(re.search(r'ab*', text))

preview('+')
# 1 или более повторений
print(re.search(r'ab+', text))

preview('?')
# 0 или 1 повторений
print(re.search(r'ab?', text))

preview('*?, +?, ??')
# ограничение жадности
print(re.search(r'^.*?', text))
print(re.search(r'^.+?', text))
print(re.search(r'^.??', text))

preview('*+, ++, ?+')
# притяжательные квантификаторы
print(re.search(r'^.*+', text))
print(re.search(r'^.++', text))
print(re.search(r'^.?+', text))

preview('{m}')
# m повторений
print(re.search(r'b{4}', text))
print(re.search(r'b{6}', text))

preview('{m,n}')
# как можно больше повторений в промежутке от m до n
print(re.search(r'b{2,5}', text))

preview('{m,n}?')
# как можно меньше повторений в промежутке от m до n
print(re.search(r'b{2,5}?', text))

preview('{m,n}+')
# притяжательная версия квантификатора выше
print(re.search(r'b{2,5}+c', text))

preview('{\\}')
# экранирование специальных символов
print(re.search(r'^.*\*', text))

preview('[]')
# символьный класс
print(re.search(r'[b-z]+[1-5]', text))

preview('|')
# или
print(re.search(r'[#]|[1-5]', text))

preview('(...)')
# группа с захватом
print(re.search(r'(\w+3.)', text))

preview('Расширения регулярных выражений')
#

preview('(?aiLmsux)')
# установка флагов регулярного выражения
print(re.search(r'(?i)zx', text))
print(re.search(r'(?si)BC', text))

# re.a - сопоставление только в ASCII
# re.i - игнорирование регистра
# re.L - в зависимости от локали
# re.m - многострочный
# re.s - точка соответствует всем
# re.u - сопоставление в Юникоде
# re.x - режим отладки

preview('(?aiLmsux-imsx:...)')
# установка и удаление флагов;
print(re.search(r'(?a-i:ZX)', text))

preview('?>...')
# атомарная группа
print(re.search(r'(?>.)', text))

preview('(?:...)')
# группа без захвата
print(re.findall(r'(?:[ab]+)', text))

preview('(?P<name>...)')
# именованная группа
print(re.findall(r'(?P<group>[ab]+)', text))

preview('(?P=name)')
# обратная ссылка на именованную группу

preview('(?#...)')
# комментарий
print(re.search(r'(?si)BC', text))
print(re.search(r'(?#si)BC', text))

preview('(?=...)')
# опережающая позитивная проверка
print(re.search(r'c(?=[0-10])..', text))

preview('(?!...)')
# опережающая негативная проверка
print(re.search(r'c(?![0-10])..', text))

preview('(?<=...)')
# позитивная ретроспективная проверка
print(re.search(r'(?<=!).+', text))

preview('(?<!...)')
# негативная ретроспективная проверка

preview('(?(id/name)yes-pattern|no-pattern)')
# стараться соответствовать yes-pattern;

preview('Специальные последовательности')
#

preview('\\number')
# соответствие группы с тем же номером
p = re.compile(r'(\b\w+)\s+\1')
print(p.search('Pris in the the spring'))

preview('\A')
# только с начало строки
print(re.search(r'\A.', text))

preview('\\b')
# пустая строка (начало или конец слова)
print(re.findall(r'\bqwe\b', 'qwe qwe. (qwe) asd qwe asd asdqwe qwe2'))

preview('\B')
# пустая строка (НЕ начало или конец слова)
print(re.findall(r'qwe\B', 'qwe qwe. (qwe) asd qwe asd asdqwe qwe2'))

preview('\d')
# любая десятичная цифра
print(re.search(r'\d+', text))

preview('\D')
# НЕ десятичная цифра
print(re.findall(r'\D+', text))

preview('\s')
# пробельный символ
print(re.findall(r'\s+', text))

preview('\S')
# НЕ пробельный символ
print(re.findall(r'\S+', text))

preview('\w')
# символы, которые могут быть частью слова
print(re.findall(r'\w+', text))

preview('\W')
# символы, которые НЕ могут быть частью слова
print(re.findall(r'\W+', text))

preview('\Z')
# только с конец строки
print(re.findall(r'\w+\Z', text))

preview('FUNCTIONS')

