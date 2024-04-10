import stat


def preview(x):
    print(f'\n---- {x} ----')


preview('os')
import os

preview('os.name')
print(os.name)

preview('os.environ')
print(os.environ)

preview('os.getlogin()')
print(os.getlogin())

preview('os.getpid()')
print(os.getpid())

preview('os.access()')
print(os.access('README.md', os.F_OK))

preview('os.chdir()')
print(os.chdir('test'))

preview('os.chmod')
print(os.chmod('test.py', stat.S_IRWXU))

preview('os.chown')
print('NONE')

preview('os.getcwd()')
print(os.getcwd())

preview('os.link()')
print('NONE')

preview('os.listdir()')
print(os.listdir('../'))

preview('os.mkdir()')
print(os.mkdir('test_dir'))
print(os.getcwd())
print(os.rmdir('test_dir'))

preview('os.makedirs()')
print(os.makedirs('test_dir'))
print(os.getcwd())
print(os.rmdir('test_dir'))

preview('os.remove()')
# print(os.remove('test_dir'))

preview('os.rename()')
print(os.mkdir('test'))
print(os.rename('test', 'QWE'))
print(os.rmdir('QWE'))

preview('os.uname()')
# os.uname()
import platform

print(platform.uname())
