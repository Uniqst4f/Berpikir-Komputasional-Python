## Python as A Language
Python is a usable first beautiful second programming language. It is quite strange coming from another language to use it. 

For example: len(string) vs string.len() 

This is implemented by using special methods that are always named with leading underscores. Ex :
`__getitem__`

Why do we need to use this? If we implement a special methods function the python interperter can call functions from the python standard library for example sort and iterations.

3 important Special Methods are important for a collection :
1. Iterable
2. Sized (for len)
3. Containers (for the in operator)

The predecessor for Pyhton is called ABC. ABC introduces many pythonic ideas such as built-in tuple, structure by indentations, and strong types.

## Understanding Sequences 
There are 2 main types of Sequences
1. _Container Sequences_
A container sequences holds references to the objects it contains (which can be any type) somewhat like a pointer.
2. _Flat Sequences_
A single object and one data type C style array

Why does Pyhton need these distinctions?

Concrete classes such as lists and tuples predate the ABCs collections. On the other hand we need ABCs to implement elegant dynamic typing. So how does Python solve this? Python introduces virtual subclasses where concrete classes are registered with new ABCs types. You might be wondering why do we need to use ABCs so much?

In a language like CPP you for a function you would need the same data type/strucure as an input and ouput. In Python because of the ABCs we can just generalize it. 

Ex :
```
```
```
```from collections.abc import Sequence 
  
  def average(numbers: Sequence[float] -> float:
      return sum(numbers)/ len(numbers)
```

With this the function can input any type (tuples, lists, etc) as long as it fulfills the requirements to be a sequence.


