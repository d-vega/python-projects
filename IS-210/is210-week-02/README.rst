#####################
IS 210 Assignment #02
#####################
*************
Warm-Up Tasks
*************

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Lesson: 02

Overview
========

The warm-up tasks this week will focus on general python file structure.

Instructions
============

Add your interpreter directive, utf-8 encoding, and a short docstring.

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

As we discussed in the *Concepts and Terms* document, executable Python files
should have an interpreter directive. One such file in our repository happens
to be missing one!

Specifications
^^^^^^^^^^^^^^

1.  Edit ``task_01.py`` and add an interpreter directive in the proper
    location.


Task 02
-------

The encoding statement is as, if-not more, important to add to your Python
files than your interpreter directive. As it happens, one of our files
happens to be missing its coding statement. Correct it to receive credit
for this task.

Specifications
^^^^^^^^^^^^^^

1.  Edit ``task_02.py`` and add an coding statement in the appropriate
    location.



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

Your code should be submitted via Blackboard, as a python file(s).


.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
