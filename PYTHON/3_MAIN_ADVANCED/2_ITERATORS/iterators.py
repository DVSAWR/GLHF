def preview(x):
    print(f'\n---- {x} ----')


preview('EXAMPLE TUPLET')

mytuplet = ('qwe', 'asd', 'zxc')
myiter = iter(mytuplet)

print(mytuplet)
print(myiter)
print(next(myiter))
print(next(myiter))
print(next(myiter))



preview('EXAMPLE STRING')

mystr = 'qwe'
myiter = iter(mystr)

print(mystr)
print(myiter)
print(next(myiter))
print(next(myiter))
print(next(myiter))


preview('LOOPING THROUGH AN ITERATOR')
# USING FOR to iterate through
mytuplet = ('qwe', 'asd', 'zxc')

print(mytuplet)

for i in mytuplet:
    print(i)

print('')
mystr = 'qwe'
print(mystr)
for i in mystr:
    print(i)


# The for loop actually creates an iterator object and executes the next() method for each loop.


preview('CREATE AN ITERATOR')

class MyNumbers:
    def __iter__(self):
        self.x = 1
        return self
    
    def __next__(self):
        x = self.x
        self.x += 1
        return x
    
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print('...')


preview('STOPITERATION')

class MyNumbers:
    def __iter__(self):
        self.x = 1
        return self

    def __next__(self):
        if self.x <= 10:
            x = self.x
            self.x += 1
            return x
        else:
            print('> raise StopIteration')
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for i in myiter:
    print(i)



