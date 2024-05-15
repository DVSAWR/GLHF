import random
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

preview('\\A')
# только с начало строки
print(re.search(r'\A.', text))

preview('\\b')
# пустая строка (начало или конец слова)
print(re.findall(r'\bqwe\b', 'qwe qwe. (qwe) asd qwe asd asdqwe qwe2'))

preview('\\B')
# пустая строка (НЕ начало или конец слова)
print(re.findall(r'qwe\B', 'qwe qwe. (qwe) asd qwe asd asdqwe qwe2'))

preview('\\d')
# любая десятичная цифра
print(re.search(r'\d+', text))

preview('\\D')
# НЕ десятичная цифра
print(re.findall(r'\D+', text))

preview('\\s')
# пробельный символ
print(re.findall(r'\s+', text))

preview('\\S')
# НЕ пробельный символ
print(re.findall(r'\S+', text))

preview('\\w')
# символы, которые могут быть частью слова
print(re.findall(r'\w+', text))

preview('\\W')
# символы, которые НЕ могут быть частью слова
print(re.findall(r'\W+', text))

preview('\\Z')
# только с конец строки
print(re.findall(r'\w+\Z', text))

preview('FUNCTIONS')

preview('compile()')
# Функция compile() модуля re компилирует шаблон регулярного выражения pattern в объект регулярного выражения, который может быть использован для поиска совпадений с использованием методов Match.match(), Match.search() и других способов.

prog = re.compile(r'(?i)[a-z]+')
print(prog)

print(text)
print(prog.match(text))

preview('re.compile() flags')
print('re.ASCII()')
print('re.DEBUG')
print('re.IGNORECASE()')
print('re.LOCALE()')
print('re.MULTILINE()')
print('re.DOTALL()')
print('re.VERBOSE()')

preview('search()')
# Функция search() модуля re сканирует строку string в поисках первого совпадения с шаблоном pattern регулярного выражения и возвращает соответствующий объект соответствия.

print(re.search('super', 'superstition').span())

match = re.search('super', 'superstition')
print(match)
print(match.span())
print(match.start())
print(match.end())

preview('match()')
# Функция match() модуля re возвращает соответствующий объект сопоставления, если ноль или более символов В НАЧАЛЕ СТРОКИ string соответствуют шаблону регулярного выражения pattern.

print(re.match('super', 'superstition'))
print(re.match('super', 'uperstition'))

preview('fullmatch()')
# Функция fullmatch() модуля re вернет объект сопоставления, если вся строка string соответствует шаблону регулярного выражения pattern.

print(re.fullmatch(r'[a-z]+\s\d+', 'super 205'))
print(re.fullmatch(r'[a-z]+\s\d+', 'puper 20'))
print(re.fullmatch(r'[a-z]+\s\d+', 'super 20   '))

preview('finditer()')
# Функция finditer() модуля re возвращает итератор объектов сопоставления по всем неперекрывающимся совпадениям для шаблона регулярного выражения в строке.

text = 'qwe 123 asd 456 zxc 789'
match = re.finditer(r'\d+', text)

print(match)
print(list(match))

preview('split()')
# Функция split() модуля re делит строку по появлению шаблона регулярного выражения pattern и возвращает список получившихся подстрок. Если в шаблоне используются захватывающие скобки, то текст всех групп в шаблоне также возвращается как часть результирующего списка. Если maxsplit отличен от нуля, происходит максимальное деление строки на maxsplit частей, а остаток строки возвращается как последний элемент списка.

text = """
qopefkqew f12 weofj 23
qvpfker 432 ok
0560k kg45k 
34kg0 k4-gk 0-k4
"""
ent = re.split('\n+', text)
print(ent)

for i in ent:
    print(i)

print('')

print(re.split(r'[a-z]+', '0d32tg59', flags=re.IGNORECASE))

preview('findall()')
# Функция findall() модуля re возвращает все неперекрывающиеся совпадения шаблона pattern в строке string в виде списка строк или список кортежей. Строка сканируется слева направо, и совпадения возвращаются в найденном порядке.

text = 'qwe 123 asd456 zxc 789'
print(text)

match = re.findall(r'\d+', text)
print(match)

match = re.findall(r'[a-z]+', text)
print(match)

match = re.findall(r'(\w+) (\d+)', text)
print(match)

preview('sub()')


# Функция sub() модуля re возвращает строку, полученную путем замены крайнего левого неперекрывающегося вхождения шаблона регулярного выражения pattern в строке string на строку замены repl. Если шаблон регулярного выражения не найден, строка возвращается без изменений.

def repl(text):
    inner_word = list(text.group(2))
    random.shuffle(inner_word)
    return text.group(1) + ''.join(inner_word) + text.group(3)


text = 'Quesadilla taco burrito avocadre'
print(re.sub(r'(\w)(\w+)(\w)', repl, text))
print(re.sub(r'(\w)(\w+)(\w)', repl, text))
print(re.sub(r'(\w)(\w+)(\w)', repl, text))

preview('subn()')
# Функция subn() модуля re выполняет ту же операцию, что и функция sub(), но возвращает кортеж (new_string, number_of_subs_made), где new_string - строка, полученная в результате замены, number_of_subs_made - количество совершенных замен.

text = 'Quesadilla taco burrito avocadre'
print(re.subn(r'(\w)(\w+)(\w)', repl, text))
print(re.subn(r'(\w)(\w+)(\w)', repl, text))
print(re.subn(r'(\w)(\w+)(\w)', repl, text))

preview('escape()')
# Функция escape() модуля re выполняет экранирование специальных символов в шаблоне. Это полезно, если требуется сопоставить произвольную строку литерала, которая может содержать метасимволы регулярных выражений.

print(re.escape('//w.qwe.asd+?|'))

import string

legal_chars = string.ascii_lowercase + string.digits + '!@#$%^&*()_+'

print('[%s] >>> END' % re.escape(legal_chars))

operators = ['+', '-', '*', '/', '**']
print(' | '.join(map(re.escape, sorted(operators, reverse=True))))

preview('purge()')
# Функция purge() модуля re очищает кэш от регулярных выражений.

preview('error()')
# Исключение error() модуля re возникает, когда строка, переданная одной из функций модуля, не является допустимым регулярным выражением, например шаблон может содержать несоответствующие скобки или когда возникает какая-либо другая ошибка во время компиляции шаблона или сопоставления со строкой.

# msg - Неформатированное сообщение об ошибке.
# pattern - Шаблон регулярного выражения.
# pos - Индекс в образце, где компиляция не удалась (может быть None).
# lineno - номер строки, соответствующая pos (может быть None).
# colno - Столбец, соответствующий pos (может быть None).