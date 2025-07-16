# pytest is the module that provides us with testing helper functions.
# Mostly not needed initially, but you'll call on it in some cases.
# See documentation on pytest.
import pytest
import os
from logger import logger, log_function

# Import the module whose procedures and functions you want to test here.
import pyls


# Note that the procedures below that are testing for things **must**
# have their names start with "test_" ... just as this file's name
# also starts with "test_". `pytest` will automatically pick up
# such functions and run them when you run `uvx pytest` from the
# command line.
def test_dummy():
    """
    A sample dummy test for illustration. This test will always succeed.
    """
    assert 2 == 2, "Two and two must be the same"


def test_dummy_fails():
    """
    A sample dummy test for illustration. This test will always fail.
    """
    assert 2 == 3, "Two and three must be the same. (Really?)"


def os_list_test(dirname, longform, formatted):
    """
    Test the os.listdir function.
    """
    dir_list = os.listdir(dirname)
    if longform:
        for entry in dir_list:
            path = os.path.join(".", entry)
            if os.path.isdir(path):
                print(f"{entry}/")
            else:
                print(f"{entry}*")
    elif formatted:
        pass


@log_function
def logger_testing():
    logger.info("This is an info message")
    logger.debug("This is a debug message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

    try:
        return logger.debug("Function exited")
    except:
        raise RuntimeError("Error returning in the function")


def main():
    logger.info("No script errors detected. Proceeding with execution ...")


main()
