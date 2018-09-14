#####################
IS 210 Assignment #03
#####################
*************
Warm-Up Tasks
*************

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Lesson: 03

Overview
========

The warm-up tasks this week will focus on general git repository tasks. You'll
be tasked to manipulate files with git's tools prior to submitting the work
through the git pull request workflow.

Instructions
============

The following tasks will either have you interacting with existing files in
the assignment repository or creating new ones on the fly. Don't forget to add
your interpreter directive, utf-8 encoding, and a short docstring with any new
files that you create!

.. important::

    In these exercises, you may, on occasion, come across a task that requres
    you to research or use a function or method not directly covered by the
    course text. Since Python is such a large language it would be impossible
    for the author to have included descriptions of each and every available
    function which would largely duplicate the offical Python documentation.

    A *vital* skill to successful programming is being comfortable searching
    for and using official language documentation sources like the
    `Python String Documentation`_ page. Throughout our coursework we will be
    practicing both the use of the language in practice and the search skills
    necessary to become functional programmers.

Warm-Up Tasks
=============

Task 01
-------

In the reading, we learned that python strings are immutable, meaning they
cannot be changed. Here we'll test for the same property to see if it holds
true for the variables that hold strings.

Specifications
^^^^^^^^^^^^^^

1.  Open ``task_01.py``

2.  After line 9, add a new line and assign a new value of ``Nevermore!`` to
    the ``RAVEN`` variable.

    .. note::

        Do not change the existing variable declaration. Add a new line
        instead.

Examples
^^^^^^^^

.. code:: pycon

    >>> print RAVEN
    Nevermore!

Task 02
-------

Python's order of operations respects parentheses. Create a mathematical
statement in a single-line.

Specifications
^^^^^^^^^^^^^^

1.  Create a new file ``task_02.py``

2.  Create a variable named ``WEEKS`` and, in a single statement:

    1.  Calculate the remainder of ``19`` divided by ``10``

    2.  Add the result to ``100``

    3.  Add that result to ``2^8`` (do exponentiation in Python!)

    4.  Divide all of the above by ``7`` 

Examples
^^^^^^^^

.. code:: pycon

    >>> print WEEKS
    52

Task 03
-------

In this task, we'll perform a basic slice operation with a string.

Specifications
^^^^^^^^^^^^^^

1.  Open ``task_03.py``

2.  Use the *slice* syntax to slice the first ``7`` characters from the
    ``WILL_ROBINSON`` variable and assign the result into a new variable
    named ``KLAXON``

Examples
^^^^^^^^

.. code:: pycon

    >>> print WILL_ROBINSON
    Danger Will Robinson!
    >>> print KLAXON
    Danger 


Task 04
-------

Next, we'll try repeating a string. This particular file uses an import to
take the KLAXON variable you created in `Task 03`_.

Specifications
^^^^^^^^^^^^^^

1.  Open ``task_04.py``

2.  On a new line, use the string repetition operator to repeat ``KLAXON`` five
    times and save the result back into ``KLAXON``

.. hint::

    While not required to achieve this objective, you could use an *arithmetic
    assignment* operator to achieve this objective.

Examples
^^^^^^^^

.. code:: pycon

    >>> print KLAXON
    Danger Danger Danger Danger Danger

Task 05
-------

The ``split()`` string function allows us to split a string according to a
specified delimiter and returns a list of the split statements.

Specifications
^^^^^^^^^^^^^^

1.  Open ``task_05.py``

2.  Use the string ``.split()`` program to split up the
    ``TEENAGE_MUTANT_NINJAS`` variable using a period + space ``'. '`` as the
    delimiter.

3.  Save the result into a new variable named ``TURTLE_POWER``

Examples
^^^^^^^^

.. code:: pycon

    >>> print TURTLE_POWER
    ['Michaelangelo', 'Leonardo', 'Rafael', 'Donatello',
     'Heroes in a half shell.']

Task 06
-------

In this task we're going to use the ``len()`` function to tell us how many
words are found in our copy of Tolstoy's *War and Peace*.

Specifications
^^^^^^^^^^^^^^

1.  Open ``task_06.py``

2.  Add a new line and, *in a single line*, split the text with ``split()`` and
    use ``len()`` to count the number of words.

3.  Save the resulting number in a new variable named ``WORDCT``

.. hint::

    Python allows you to have multiple functions in the same line

.. note::

    While we won't get to this much later, as you can see, opening files and
    reading their contents in Python can be very easy to accomplish!

Examples
^^^^^^^^

.. code:: python

    >>> print WORDCT
    566316

Task 07
-------

In this task, we'll use the ``in`` operator to test whether or not a particular
string is found within another string.

Specifications
^^^^^^^^^^^^^^

1.  Open ``task_07.py``

2.  Use the ``in`` operator to test whether or not the word ``granaries``
    exists within the ``WORDS`` variable

3.  Save the result into a variable named ``GRANARIES_EXIST``

Examples
^^^^^^^^

.. code:: python

    >>> print GRANARIES_EXIST

Task 08
-------

The ``strip()`` commands are of great help when dealing with poorly formatted
data.

Specifications
^^^^^^^^^^^^^^

1.  Open ``task_08.py``

2.  Use the ``strip()`` function to remove whitespace from ``NERVOUS_AS`` and
    save the result back into the ``NERVOUS_AS`` variable

3.  In a single-line statement, use ``rstrip()`` and ``lstrip()`` to remove the
    commas (``,``), and forward slashes (``/``) from ``NERVOUS_AS`` storing the
    result back into the ``NERVOUS_AS`` variable.

.. note::

    Depending upon what a function returns, it is possible to chain together
    multiple function calls as a form of shorthand. This is possible because
    these functions either return the original object or an object of the
    exact same time (eg, a string) so subsequenct ``.function()`` calls may
    be strung together one after another.

Examples
^^^^^^^^

.. code:: pycon

    >>> print NERVOUS_AS
    A long-tailed cat in a room full of rockin' chairs.

Task 09
-------

One way to achieve a multi-line string is to use triple double or single
quotes. This is most commonly docstrings which are a required part of every
module.

Specifications
^^^^^^^^^^^^^^

1.  Open ``task_09.py``

2.  Add a multi-line docstring to ``task_09.py``. The docstring should break
    across two paragraphs.

3.  If you want to test your docstring, try the following commands
    from the Python interactive command line by using ``help()``.

Examples
^^^^^^^^

.. code:: pycon

    >>> import task_09
    >>> help(task_09)

Press ``q`` to exit the help page for this module.

Task 10
-------

One of the simple, though useful, string functions available in Python are
the casing functions such as ``.lower()`` and ``.upper()``.

Specifications
^^^^^^^^^^^^^^

1.  Open ``task_10.py``

2.  Use a string function that will change ``MOVIE`` to titlecase and save its
    result into a new variable named ``ENTITLED``

Examples
^^^^^^^^

.. code:: pycon

    >>> print ENTITLED
    Dr. Strangelove Or: How I Learned To Stop Worrying And Love The Bomb

Task 11
-------

Learning how to escape special characters and strings is an absolute necessity
for any beginning programmer.

Specifications
^^^^^^^^^^^^^^

1.  Create a new file called ``task_11.py``

2.  Create a new variable called ``ESCAPE_STRING`` with the value ``\n'"``

.. note::

   In this case, we want the real characters backslash + n, not the escape
   sequence of a newline.

Examples
^^^^^^^^

.. code:: pycon

    >>> print ESCAPE_STRING
    \n'"

Task 12
-------

In this task, we'll assign some simple numeric types. You'll need to use the
import statement as shown in your course text or video to get access to the
decimal and fraction types.

Specifications
^^^^^^^^^^^^^^

1.  Create a new file called ``task_12.py``

2.  Create a new variable named ``INTVAL`` and assign it a value of ``1``

3.  Create a new variable named ``FLOATVAL`` and assign it a value of ``0.1``

4.  Create a new variable named ``DECVAL`` and assign it a value of one-tenth

5.  Create a new variable named ``FRACVAL`` and assign it a value of one-tenth

.. hint::

    You must import both the ``decimal`` and ``fractions`` modules to get
    access to the ``Decimal`` and ``Fraction`` data types.

Examples
^^^^^^^^

.. code:: pycon

    >>> print INTVAL
    1
    >>> print FLOATVAL
    0.1
    >>> print DECVAL
    0.1
    >>> print FRACVAL
    1/10

Task 13
-------

Testing equality can be tricky with the various mathematical types as they all
store data in slightly different ways. Here's we'll take a look at a few cases
from what you did in a prior step.

Specifications
^^^^^^^^^^^^^^

1.  Open ``task_13.py``, this file imports all of the variables you set in
    ``task_12.py``

2.  Use the equality comparison operator (``==``) to test if ``DECVAL`` and
    ``FRACVAL`` are equal.

3.  Save the result into a new variable named, ``FRAC_DEC_EQUAL``

4.  Similarly, use the inequality comparison operator (``!=``) to test if
    ``DECVAL`` and ``FLOATVAL`` are inequal

5.  Save the result into a new variable named, ``DEC_FLOAT_INEQUAL``


.. hint::

    You can access ``task_12`` data through its namespace so, for example, to
    access the ``FLOATVAL`` variable from ``task_12``, you'd do so through
    something like ``task_12.FLOATVAL``. Use this way of addressing the
    variables directly; don't reassign them to new variable names.

Examples
^^^^^^^^

.. code:: pycon

    >>> FRAC_DEC_EQUAL
    False
    >>> DEC_FLOAT_INEQUAL
    True

Task 14
-------

There are just a few more basic types with which we ought to familiarize
ourselves at this point.

Specifications
^^^^^^^^^^^^^^

1.  Create a new file named ``task_14.py``

2.  Create a new variable named ``IS_TRUE`` and assign it a value of ``True``

3.  Create a new variable named ``IS_FALSE`` and assign it a value of ``False``

4.  Create a new variabled named ``IS_NONE`` and assign it a value of ``None``

5.  **In a single, one-line statement**, use the *logical AND* operator and the
    *equality* operator to test if ``IS_TRUE`` is equal to ``1`` and
    ``IS_FALSE`` is equal to ``0``

6.  Store the result into a new variable named ``INTEGER_EQUIV``

Examples
^^^^^^^^

.. code:: pycon

    >>> print IS_TRUE
    True
    >>> print IS_FALSE
    False
    >>> print IS_NONE
    None
    >>> INTEGER_EQUIV
    True

Task 15
-------

The course text mentions that some types of operations are illegal between
objects of different types. For example, a string cannot be concatenated with
an integer using the concatenation operator (``+``) without first converting
the integer to a string.

Specifications
^^^^^^^^^^^^^^

1.  Open ``task_15.py``

2.  Concatenate the variables ``NOT_THE_QUESTION`` and ``ANSWER`` by using the
    concatenation operator and the ``str()`` function.

3.  Store the result into a new variable named ``THANKS_FOR_THE_FISH``

Examples
^^^^^^^^

.. code:: pycon

    >>> print THANKS_FOR_THE_FISH
    The answer to life, the universe, and everything? It's 42

Executing Tests
===============

Code must be functional and pass tests before it will be eligible for credit.

Linting
-------

Lint tests check your code for syntactic or stylistic errors To execute lint
tests against a specific file, simply open a terminal in the same directory as
your code repository and type:

.. code:: console

    $ pylint filename.py

Where ``filename.py`` is the name of the file you wish to lint test.

Unit Tests
----------

Unit tests check that your code performs the tested objectives. Unit tests
may be executed individually by opening a terminal in the same directory as
your code repository and typing:

.. code:: console

    $ nosetests tests/name_of_test.py

Where ``name_of_test.py`` is the name of the testfile found in the ``tests``
directory of your source code.

Running All Tests
-----------------

All tests may be run simultaneously by executing the ``runtests.sh`` script
from the root of your assignment repository. To execute all tests, open a
terminal in the same directory as your code repository and type:

.. code:: console

    $ ./runtests.sh

Submission
==========

Code should be submitted via Blackboard as python files.

In order to receive full credit you must complete the assignment as-instructed
and without any violations (reported in the build status). 


.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
