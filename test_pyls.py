# pytest is the module that provides us with testing helper functions.
# Mostly not needed initially, but you'll call on it in some cases.
# See documentation on pytest.
import tempfile
import pytest
import os
import sys
import io
from pyls import pyls

# Import the module whose procedures and functions you want to test here.
import pyls


@pytest.fixture()
def capture_stdout():
    sio = io.StringIO()
    yield sio


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
    assert 2 == 2, "Two and three must be the same. (Really?)"


def test_capture_manual():
    oldstdout = sys.stdout
    sio = io.StringIO()
    sys.stdout = sio
    print("Hello")
    sys.stdout = oldstdout
    sio.seek(0)
    result = sio.read()
    assert result == "Hello\n"


def test_capture_pytest(capture_stdout):
    old = sys.stdout
    sys.stdout = capture_stdout
    print("meow")
    sys.stdout = old

    capture_stdout.seek(0)
    result = capture_stdout.read()
    assert result == "meow\n", (
        f"result {len(result)} = {result}, capture = {capture_stdout}"
    )


def test_pyls_sample_dir(capture_stdout):
    import sys
    import tempfile
    import os

    with tempfile.TemporaryDirectory() as tmpdirname:
        os.mkdir(os.path.join(tmpdirname, "subdir"))
        with open(os.path.join(tmpdirname, "file1.txt"), "w") as f:
            f.write("hello")
        with open(os.path.join(tmpdirname, "file2.txt"), "w") as f:
            f.write("world")
        with open(os.path.join(tmpdirname, "subdir", "file3.txt"), "w") as f:
            f.write("!")


        old_stdout = sys.stdout
        sys.stdout = capture_stdout
        try:
            pyls.pyls(tmpdirname ,formatted=True)
        finally:
            sys.stdout = old_stdout

        capture_stdout.seek(0)
        output = capture_stdout.read()
        assert "file1.txt" in output
        assert "file2.txt" in output
        assert "subdir/" in output
        assert "subdir" not in output.replace("subdir/", "") # Checking if the formatting has been properly applied to the output


def test_longform():
    """
    This function tests for when longform is True
    """
    pass


def test_formatted():
    """
    This function tests for when formatted is True
    """
    pass


def test_longform_formatted():
    """
    This function tests for when both formatted and longform are activated
    """
    pass


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

def main():
    pass
