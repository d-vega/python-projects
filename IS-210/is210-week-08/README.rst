####################
IS 210 Assignment 08
####################
************
Warmup Tasks
************

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210

Overview
========

In this assignment, we'll look at some basic uses of conditionals to enforce
control-flow of some simple programs.

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

Warmup Tasks
============

Task 01
-------

Use ``raw_input`` to collect user input on the command line.

Specifications
^^^^^^^^^^^^^^

1.  Create a file named ``task_01.py``

2.  Use ``raw_input()`` to ask the user a question (any question!) and save
    the result to a variable named ``MY_ANSWER``

Examples
^^^^^^^^

.. code:: pycon

    What is your name? Arthur
    >>> print MY_ANSWER
    Arthur

.. note::

    Examples given here are just examples. They are *not* guaranteed to be the
    exact values encountered in your code.

Task 02
-------

Extend our ``raw_input()`` usage and convert the data type of collected user
input.

Specifications
^^^^^^^^^^^^^^

1.  Create a new file named ``task_02.py``

2.  In ``task_02.py`` use ``raw_input()`` and a type conversion function
    to ask the user a question and store the result *as an integer* into a
    new variable named ``MY_INTEGER``

Examples
^^^^^^^^

.. code:: pycon

    What is the answer to the life the universe and everything? 42
    >>> print MY_INTEGER
    42
    >>> type(MY_INTEGER)
    <type 'int'>

Task 03
-------

Create a complex test using logical operators.

Specifications
^^^^^^^^^^^^^^

1.  Open ``task_03.py``

2.  Create a multi-part statement that uses *logical operators* to combine
    several comparisons:

    1.  That ``LOOKS_NICE`` is ``True`` and that ``EXPENSE`` is less than or
        equal to ``MAX_EXPENSE``

    2.  OR, if **both** of the above conditions are not met, that
        ``GET_OUT_ALIVE`` is ``False``

3.  Save the result into a variable named ``SACRIFICE``, eg

    .. code:: python

        SACRIFICE =  # your logical test goes here

.. hint::

    Review how to properly group statements with logical operators and how
    boolean values should be tested or negated before attempting this task. The
    style video will be of particular help.

.. note::

    Automated testing for this task will not be able to tell you whether you
    accomplished the overall objective of proper style or grouping as it only
    tests the resulting value of ``SACRIFICE``. Don't assume that at PASSed
    test means you're guaranteed credit.

Examples
^^^^^^^^

.. code:: pycon

    >>> print SACRIFICE
    True

Task 04
-------

Use a single, simple branching statement to alter behavior based on user
input.

Specifications
^^^^^^^^^^^^^^

1.  Open ``task_04.py`` which contains some existing code.

2.  Use ``len()`` to measure the length of the input string and save the
    value to a variable at the spot marked in the comments.

3.  Create a conditional expression that changes the value of ``LONGSTR`` to
    ``'long'`` if the length measured in step #2 is greater than ``MAX_LENGTH``

Examples
^^^^^^^^

.. code:: pycon
    
    Tell me a story! A story.
    That certainly was a short story!
    >>> print LONGSTR
    'short'

Task 05
-------

Imagine that you were taking an incredibly difficult programming course. The
stress of the course is starting to get to you so your doctor tells you to
start regularly checking your systolic blood pressure. Unfortunately, the
numbers are fairly hard to remember, you'd much rather know your pressure in
common language terms.

Create a simple branching statement to achieve this objective.

Specifications
^^^^^^^^^^^^^^

1.  Create a new file called ``task_05.py``

2.  Using a combination of ``raw_input()``, ``if``, ``elif``, and ``else``,
    write a program that asks the user their blood pressure. Compare the blood
    pressure against the following chart and save the Status to a variable
    named ``BP_STATUS``. At the end of the program, print a nice sentence with
    a formatting string to tell you your status and use ``.format()`` to
    replace the formatting string with your ``BP_STATUS``.
    
    .. table:: Blood Pressure Readings
        
        ====== ===== ================
        Start  End   Status
        ====== ===== ================
        --     89    Low
        90     119   Ideal
        120    139   Warning
        140    159   High
        160    --    Emergency
        ====== ===== ================

.. hint::

    Don't forget that the input of ``raw_input`` is a string!

Examples
^^^^^^^^

.. code:: console

    $ python -i task_05.py
    What is your blood pressure? 120
    Your status is currently: Warning!

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

Code should be submitted via Blackboard as a compressed folder with python files.

.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
