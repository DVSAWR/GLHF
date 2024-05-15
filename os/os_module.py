import stat


def preview(x):
    print(f'\n---- {x} ----')


preview('os')
import os

preview('os.name')
# имя операционной системы. Доступные варианты: posix, nt, mac, os2, ce, java.
print(os.name)

preview('os.environ')
# словарь переменных окружения. Изменяемый (можно добавлять и удалять переменные окружения).
print(os.environ)

preview('os.getlogin()')
# имя пользователя, вошедшего в терминал (Unix).
print(os.getlogin())

preview('os.getpid()')
# текущий id процесса.
print(os.getpid())

preview('os.uname()')
# os.uname()
# информация об ОС. возвращает объект с атрибутами: sysname - имя операционной системы, nodename - имя машины в сети (определяется реализацией), release - релиз, version - версия, machine - идентификатор машины.
import platform

print(platform.uname())

preview('os.access()')
# проверка доступа к объекту у текущего пользователя. Флаги: os.F_OK - объект существует, os.R_OK - доступен на чтение, os.W_OK - доступен на запись, os.X_OK - доступен на исполнение.
print(os.access('README.md', os.F_OK))

preview('os.chdir()')
# смена текущей директории.
os.chdir('test')

preview('os.chmod')
# смена прав доступа к объекту (mode - восьмеричное число).
os.chmod('test.py', stat.S_IRWXU)

preview('os.chown')
# меняет id владельца и группы (Unix).

preview('os.getcwd()')
# текущая рабочая директория.
print(os.getcwd())

preview('os.link()')
# создаёт жёсткую ссылку.

preview('os.listdir()')
# список файлов и директорий в папке.
print(os.listdir('../Python/MAIN/2_MODULES_STANDART_LIBRARY/'))

preview('os.mkdir()')
# создаёт директорию. OSError, если директория существует.
os.mkdir('test_dir')
os.rmdir('test_dir')

preview('os.makedirs()')
# создаёт директорию, создавая при этом промежуточные директории.
os.makedirs('test_dir')
os.rmdir('test_dir')

preview('os.remove()')
# удаляет путь к файлу.

preview('os.rename()')
# переименовывает файл или директорию из src в dst.
os.mkdir('test')
os.rename('test', 'QWE')
os.rmdir('QWE')

preview('os.renames()')
# переименовывает old в new, создавая промежуточные директории.
os.mkdir('test')
os.renames('test', 'QWE')
os.rmdir('QWE')

preview('os.replace()')
# переименовывает из src в dst с принудительной заменой.
os.replace('test.py', 'QWE.py')
os.replace('QWE.py', 'test.py')

preview('os.rmdir()')
# удаляет пустую директорию.
os.mkdir('test')
os.rmdir('test')

preview('os.removedirs()')
# удаляет директорию, затем пытается удалить родительские директории, и удаляет их рекурсивно, пока они пусты.
os.makedirs('test_1/test_2/test_3')
os.removedirs('test_1/test_2/test_3')

preview('os.symlink()')
# создаёт символическую ссылку на объект.

preview('os.sync()')
# записывает все данные на диск (Unix).

preview('os.truncate()')
# обрезает файл до длины length.
with open('test.py', 'r') as file:
    print(file.readline())
os.truncate('test.py', 2)
with open('test.py', 'r') as file:
    print(file.readline())
with open('test.py', 'w') as file:
    file.write('123456789')
with open('test.py', 'r') as file:
    print(file.readline())

preview('os.utime()')
# модификация времени последнего доступа и изменения файла. Либо times - кортеж (время доступа в секундах, время изменения в секундах), либо ns - кортеж (время доступа в наносекундах, время изменения в наносекундах).
import time

atime = os.stat('test.py').st_atime
mtime = os.stat('test.py').st_mtime
print(time.ctime(atime), time.ctime(mtime))

delta = 60 * 60 * 24 * 2
new_atime = atime - delta
new_mtime = mtime - delta

os.utime('test.py', times=(new_atime, new_mtime))
atime = os.stat('test.py').st_atime
mtime = os.stat('test.py').st_mtime
print(time.ctime(atime), time.ctime(mtime))

preview('os.walk()')
# генерация имён файлов в дереве каталогов, сверху вниз (если topdown равен True), либо снизу вверх (если False). Для каждого каталога функция walk возвращает кортеж (путь к каталогу, список каталогов, список файлов).
for (root, dirs, files) in os.walk('../Python/MAIN/2_MODULES_STANDART_LIBRARY', topdown=True):
    print(f'ROOT: {root}')
    print(f'DIRS: {dirs}')
    print(f'FILES: {files}')
    print('')

preview('os.system()')
# исполняет системную команду, возвращает код её завершения (в случае успеха 0).
print(os.system('WHOAMI'))

preview('os.urandom()')
# n случайных байт. Возможно использование этой функции в криптографических целях.
print(os.urandom(2))

preview('os.path')
# является вложенным модулем в модуль os, и реализует некоторые полезные функции для работы с путями.

preview('os.path.abspath()')
# возвращает нормализованный абсолютный путь.
print(os.path.abspath('test.py'))

preview('os.path.basename()')
# базовое имя пути (эквивалентно os.path.split(path)[1]).
print(os.path.basename('../test/test.py'))

preview('os.path.commonprefix()')
# возвращает самый длинный префикс всех путей в списке.
print(os.path.commonpath(['/user/qwe', '/user/qwe/asd']))

preview('os.path.dirname()')
# возвращает имя директории пути path.
print(os.path.dirname('/user/qwe'))

preview('os.path.exists()')
# возвращает True, если path указывает на существующий путь или дескриптор открытого файла.
print(os.path.exists('q/w/e'))

preview('os.path.expanduser()')
# заменяет ~ или ~user на домашнюю директорию пользователя.

preview('os.path.expandvars()')
# возвращает аргумент с подставленными переменными окружения ($name или ${name} заменяются переменной окружения name). Несуществующие имена не заменяет. На Windows также заменяет %name%.

preview('os.path.getatime()')
# время последнего доступа к файлу, в секундах.
with open('test.py', 'w') as file:
    file.write('123456789')
print(os.path.getatime('test.py'))
print(time.ctime(os.path.getatime('test.py')))

preview('os.path.getmtime')
# время последнего изменения файла, в секундах.
print(os.path.getmtime('test.py'))
print(time.ctime(os.path.getmtime('test.py')))

preview('os.path.getctime')
# время создания файла (Windows), время последнего изменения файла (Unix).
print(os.path.getctime('test.py'))
print(time.ctime(os.path.getctime('test.py')))

preview('os.path.getsize()')
# размер файла в байтах.
print(os.path.getsize('test.py'))

preview('os.path.isabs()')
# является ли путь абсолютным.
print(os.path.isabs(os.path.abspath('test.py')))
print(os.path.isabs('test/test.py'))

preview('os.path.isfile()')
# является ли путь файлом.
print(os.path.isfile('test.py'))
print(os.path.isfile('../test'))

preview('os.path.isdir')
# является ли путь директорией.
print(os.path.isfile('../Python/MAIN/2_MODULES_STANDART_LIBRARY'))

preview('s.path.islink()')
# является ли путь символической ссылкой.

preview('os.path.ismount()')
# является ли путь точкой монтирования.

preview('os.path.join()')
# соединяет пути с учётом особенностей операционной системы.

preview('os.path.normcase()')
# нормализует регистр пути (на файловых системах, не учитывающих регистр, приводит путь к нижнему регистру).

preview('os.path.normpath()')
# нормализует путь, убирая избыточные разделители и ссылки на предыдущие директории. На Windows преобразует прямые слеши в обратные.

preview('os.path.realpath()')
# возвращает канонический путь, убирая все символические ссылки (если они поддерживаются).
print(os.path.relpath('../test'))

preview('os.path.relpath()')
# вычисляет путь относительно директории start (по умолчанию - относительно текущей директории).
print(os.path.relpath('../test'))

preview('os.path.samefile()')
# указывают ли path1 и path2 на один и тот же файл или директорию.
print(os.path.samefile('test.py', 'test.py'))

preview('os.path.sameopenfile()')
# указывают ли дескрипторы fp1 и fp2 на один и тот же открытый файл.
print(os.path.sameopenfile(1, 2))

preview('os.path.split()')
# разбивает путь на кортеж (голова, хвост), где хвост - последний компонент пути, а голова - всё остальное. Хвост никогда не начинается со слеша (если путь заканчивается слешем, то хвост пустой). Если слешей в пути нет, то пустой будет голова.
print(os.path.split(os.path.abspath('test.py')))

preview('os.path.splitdrive()')
# разбивает путь на кортеж (голова, хвост), где хвост - последний компонент пути, а голова - всё остальное. Хвост никогда не начинается со слеша (если путь заканчивается слешем, то хвост пустой). Если слешей в пути нет, то пустой будет голова.
print(os.path.splitdrive(os.path.abspath('test.py')))

preview('os.path.splitext()')
# разбивает путь на пару (root, ext), где ext начинается с точки и содержит не более одной точки.
print(os.path.splitext(os.path.abspath('test.py')))

preview('os.path.supports_unicode_filenames')
print(os.path.supports_unicode_filenames)
