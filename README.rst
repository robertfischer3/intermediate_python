
*****************************
Intermediate Python Exercises
*****************************

Welcome to the intermediate Python Exercises.  This a set of Python Labs designed to help you with some the less commonly taught aspects of Python. The project is broken down by exercises the focus on related topics that are often treated separately, but complement each other.

====================================================================================
Exercise One: Variable Function Arguments, Decorators, and Context Managers...oh my!
====================================================================================

**Variable Functions Lab**

For the first exercise, we are going to explore ``*args`` and ``**kwargs``. First, you need to know that ``*args`` and ``**kwargs`` are **NOT** keywords. Rather it is the presence of the single or double asterisks that determine whether it is positional parameter or a keyword parameter. Experiment with creating and testing variable functional arguments.  Also, experiment with returning a tuple from the methods and testing for expected result values.

Automated Testing
^^^^^^^^^^^^^^^^^^^^^
Since all Python code should be tested, the **TestArgsLab** has been created for you. **TestArgsLab** is designed to familiarize yourself with unitest in Python as well experimenting with dynamic method parameters. To complete the lab, create five different test scenarios by creating different variable parameter functions.

Install Black
^^^^^^^^^^^^^

Properly formatted code is essential to the Pythonista.  Python code formatting has several subtle rules which are difficult to keep track of.  What to do?  Install and run Black.  Black is a python code format tool.  To recursively format your code install Black with **pip3 install black**.  Then run the command **black .**  The period is part of the command and invokes black to recursively format all .py files in the current directory and below.