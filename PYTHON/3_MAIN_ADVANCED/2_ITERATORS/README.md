## ITERATORS

[INFO w3schools.com](https://www.w3schools.com/python/python_iterators.asp)\
[INFO geeksforgeeks.org](https://www.geeksforgeeks.org/iterators-in-python/)

An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the
methods `__iter__()` and `__next__()`.

## Iterator vs Iterable

Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an
iterator from.

All these objects have a `iter()` method which is used to get an iterator

## Looping Through an Iterator

We can also use a for loop to iterate through an iterable object
The `for` loop actually creates an iterator object and executes the next() method for each loop.

## Create an Iterator

To create an object/class as an iterator you have to implement the methods `__iter__()` and `__next__()` to your object.

As you have learned in the Python Classes/Objects chapter, all classes have a function called `__init__()`, which allows
you to do some initializing when the object is being created.

The `__iter__()` method acts similar, you can do operations (initializing etc.), but must always return the iterator
object itself.

The `__next__()` method also allows you to do operations, and must return the next item in the sequence.

## StopIteration

The example above would continue forever if you had enough `next()` statements, or if it was used in a for loop.

To prevent the iteration from going on forever, we can use the `StopIteration` statement.

In the `__next__()` method, we can add a terminating condition to raise an error if the iteration is done a specified
number of times: