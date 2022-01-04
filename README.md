# Python Language
- **Statements and Data Types:**

  - ​	[Basics - Python 101](./Python_101.ipynb)

    Comments, Multi line comments, Multi line statements, Built in data types - List, Tuples, Set, Hash Tables. Functions, Lambda Functions and Classes.

  * [Python 201](./Python_201.ipynb)

    Variables and Memory References, Garbage Collection, Dynamic vs static Typing, Variable Reassignment, Object Mutability, Variable Equality, Everything is an Object and Python Interning

  * [Python 301](./Python_301.ipynb) - **Numeric Types in Detail**

    [Python 301 Extended](./Python_301_ext.ipynb) - **Numeric Types**

    [Project using Numerical types](./Projects/NumericalTypes)

    Integers, Constructors, Bases, Rational Numbers, Floats, rounding, Coercing to Integers and equality, Decimals, Decimal Operations, Decimal Performance, Complex Numbers, Booleans, Boolean Precedence and Comparison Operators

- **Data Structures:**

  - [Tuples, Namedtuples](./Tuples.ipynb)
  - [Project using Faker Library, namedtuples](./Projects/NamedTuples/README.md)
  - [Bytecode, Dis-assembly](./Disassembly.ipynb)

- **Functions as Objects:**

  - [Functions](./Python_401.ipynb)

  - [Project: Defining Higher Order Function - time_it](./Projects/HigherOrderFunction)

    Docstrings, and Annotations. Lambda Expressions, Lambdas and Sorting, Callables, Map, Filter, Zip, and List Comprehension, Reducing functions, Partial Functions, Operator Module

  * [Docs: Python Built-in Functions](https://docs.python.org/3/library/functions.html)
    * [Code Intropection](./CodeIntrospection.ipynb) - Inspecting the object at run time
    * [Scopes](./Scope.ipynb) - Global, Local & Nonlocal
  * [Closures](./ClosuresInPython.ipynb) - Nested function in which the inner function access the **nonlocal scope** variable, and remembers the state.
    * [Project using Closures](https://github.com/abalaji-blr/session-6/)
  * [Decorators](./Decorators_updated.ipynb) : Decorators Use **closures** and wrap around the object, that extend or decorate the object.
    * [Blog: Decorators in Python - Brief Introduction with examples.](https://betterprogramming.pub/decorators-in-python-72a1d578eac4)

- **Control Flow**

  - [**Iterables and Iterators**](./IterablesAndIterators.ipynb)
  - [Generators](./Generators.ipynb)
  - Context Managers

- Properties in Python







---

## Resources / Blogs



* [For memory profile - use library memory_profiler](https://pypi.org/project/memory-profiler/)

* PyDoc

  ```
  pydoc -b # b for browser
  ```

  

* PyTest

  ```
  pytest -v # verbose
  pytest -k one-specific_test
  
  ```

  

* Performance  - How to measure the time for a function?

  * timeit()

* [Python Optimization Techniques](./PythonOptimization.ipynb)

  * Python Interning
  * Peephole / Keyhole optimization
  * Lru_cache : Least Recently Used - eviction strategy to cache.
  * Constant folding - standard techinque of evaluating the expressions at compile time than the run time.

* Data generation using Faker Library

* Resources

  * [Blog: Python Code optimization Tips & Tricks](https://www.techbeamers.com/python-code-optimization-tips-tricks)
  * [Python 3 Language Reference](https://docs.python.org/3/reference/index.html)
  * [Python Documentation](https://www.python.org/doc/)
  * [Python Reference](https://python-reference.readthedocs.io/en/latest/intro.html)
  * [Python Grammar](https://docs.python.org/3/reference/grammar.html)
  * [Python Source code : GitHub](https://github.com/python/pythondotorg)
  * [Learn By Example : website](https://www.learnbyexample.org/python/)

---



