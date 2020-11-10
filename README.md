# Chess-Bot
This goal of this project was to create a competent chess AI using a neural network.

## Testing
This project makes use of Python's _unittest_ framework. Tests are used to check if algorithms work as intended.

From the root folder,
we can run the following command to run a unit test:
~~~shell
python3 -m unittest test/testname.py
~~~
There are useful decorators written in test/testlibrary.py to help with evaluating performance of algorithms.

To create a new test, create a new python file in the test/ folder. The following template creates a unit test that can be run with the above command:
~~~python
import unittest
from src.algorithms import function
from test.testlibrary import decorator

@decorator
def test_function():
  #Run code here
  function()

class testName(unittest.TestCase):
  test_function()
  #These tests are

~~~
