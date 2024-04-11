import re


def preview(x):
    print(f'\n---- {x} ----')


text = 'abbbbc abbbbc12345 !*?@#$%ZXC'

preview('Специальные символы')

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

preview('(?:...)')
# группа без захвата

preview('(?P<name>...)')
# именованная группа

preview('(?P=name)')
# обратная ссылка на именованную группу

preview('(?#...)')
# комментарий
print(re.search('(?#si)BC', text))

preview('(?=...)')
# опережающая позитивная проверка;

preview('(?!...)')
# опережающая негативная проверка;

preview('(?<=...)')
# позитивная ретроспективная проверка;

preview('(?<!...)')
# негативная ретроспективная проверка;

preview('(?(id/name)yes-pattern|no-pattern)')
# стараться соответствовать yes-pattern;
