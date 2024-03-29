'''

С целью экономии чернил в картридже принтера было принято решение укоротить некоторые слова в тексте. Для этого был составлен словарь слов, до которых можно сокращать более длинные слова. Слово из текста можно сократить, если в словаре найдется слово, являющееся началом слова из текста. Например, если в списке есть слово "лом", то слова из текста "ломбард", "ломоносов" и другие слова, начинающиеся на "лом", можно сократить до "лом".

Если слово из текста можно сократить до нескольких слов из словаря, то следует сокращать его до самого короткого слова.

Формат ввода
В первой строке через пробел вводятся слова из словаря, слова состоят из маленьких латинских букв. Гарантируется, что словарь не пуст и количество слов в словаре не превышет 1000, а длина слов — 100 символов.

Во второй строке через пробел вводятся слова текста (они также состоят только из маленьких латинских букв). Количество слов в тексте не превосходит 105, а суммарное количество букв в них — 106.

Формат вывода
Выведите текст, в котором осуществлены замены.

Пример 1
Ввод
a b
abdafb basrt casds dsasa a
Вывод
a b casds dsasa a

Пример 2
Ввод
aa bc aaa
a aa aaa bcd abcd
Вывод
a aa aa bc abcd

'''
#
# print('-------monk-time(GitHub)---------')
# from collections import defaultdict
# from functools import reduce
# from typing import Iterable
#
# LEAF = object()
#
#
# def replace_words(words: list[str], prefixes: list[str]) -> Iterable[str]:
#     make_tree = lambda: defaultdict(make_tree)
#     prefix_tree = make_tree()
#     for prefix in prefixes:
#         leaf = reduce(lambda tree, ch: tree[ch], prefix, prefix_tree)
#         leaf[LEAF] = prefix  # type: ignore
#     for word in words:
#         subtree = prefix_tree
#         for char in word:
#             if char not in subtree:
#                 yield word
#                 break
#             subtree = subtree[char]
#             if LEAF in subtree:
#                 yield subtree[LEAF]
#                 break
#         else:  # no break
#             yield word
#
#
# if __name__ == '__main__':
#     prefixes = input().split()
#     words = input().split()
#     print(*replace_words(words, prefixes), sep=' ')


print('\n---------DONE---------\n')

# first = input().split()
# second = input().split()

# first = 'a b'.split()
# second = 'abdafb basrt casds dsasa a'.split()

first = 'aa bc aaa'.split()
second = 'a aa aaa bcd abcd'.split()

print(first)

print(second)

answer = []

for i in second:
    print(i)
    if i[0] in first:
        print('IN FIRST')
        q = first[first.index(i[0])]
        if len(i) > len(q):
            print('>', q)
            answer.append(q)
        else:
            answer.append(i)
            print('>', i)
    else:
        answer.append(i)

print(*answer)

# a b
# abdafb basrt casds dsasa a
#
# a b casds dsasa a
#
# aa bc aaa
# a aa aaa bcd abcd
#
# a aa aa bc abcd


from collections import defaultdict

# sup = '\0'
#
#
# def replace_words(words, prefixes):
#     def make_tree():
#         return defaultdict(make_tree)
#
#     prefix_tree = make_tree()
#
#     for prefix in prefixes:
#         subtree = prefix_tree
#         for ch in prefix:
#             subtree = subtree[ch]
#         subtree[sup] = prefix
#
#     result = []
#     for word in words:
#         subtree = prefix_tree
#         found = False
#
#         for ch in word:
#             if ch not in subtree:
#                 result.append(word)
#                 found = True
#                 break
#
#             subtree = subtree[ch]
#             if sup in subtree:
#                 result.append(subtree[sup])
#                 found = True
#                 break
#
#         if not found:
#             result.append(word)
#
#     return result
#
#
# def main():
#     input_prefixes = sys.stdin.readline().strip()
#     input_words = sys.stdin.readline().strip()
#
#     prefixes = input_prefixes.split()
#     words = input_words.split()
#
#     replaced_words = replace_words(words, prefixes)
#     for word in replaced_words:
#         print(word, end=' ')
#
#
# if __name__ == "__main__":
#     main()


print('-------DONE---------')

from collections import defaultdict

reduct_dict = input().split()
text = input().split()
answer = []


def def_dict():
    return defaultdict(def_dict)


reduct_def_dict = def_dict()
sub = ''

for reduction in reduct_dict:
    subd = reduct_def_dict
    for symbol in reduction:
        subd = subd[symbol]
    subd[sub] = reduction

for word in text:
    subd = reduct_def_dict
    found = False

    for symbol in word:
        if symbol not in subd:
            answer.append(word)
            found = True
            break

        subd = subd[symbol]

        if sub in subd:
            answer.append(subd[sub])
            found = True
            break

    if not found:
        answer.append(word)

print(*answer)

# a b
# abdafb basrt casds dsasa a
#
# a b casds dsasa a
#
# aa bc aaa
# a aa aaa bcd abcd
#
# a aa aa bc abcd

print('----------yandex----------')

dictset = set(input().split())
ans = []
for word in input().split():
    for i in range(1, min(101, len(word))):
        part = word[:i]
        if part in dictset:
            ans.append(part)
            break
    else:
        ans.append(word)

print(' '.join(ans))
