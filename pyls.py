# Imports make the mentioned "modules" accessible to the code within
# this file, which is itself a "module".
import argparse
import os
import datetime
from logger import logger, log_function


def main() -> None:
    parser = argparse.ArgumentParser(prog="pyls", description="A baby version of ls.")

    # We now add descriptions for the expected arguments for our program.
    parser.add_argument(
        "dirname",
        nargs="?",  # Indicates that either 0 or one directory name can be given.
        default=".",  # Gives the default value to use when this argument is not given.
        # '.' means "current directory".
        help="The name of the directory whose contents are to be listed.",
    )
    parser.add_argument(
        "-l",
        "--longform",
        action="store_true",  # Indicates that the value is a boolean and no further
        # values need to be supplied on the command line.
        default=False,  # This is not really needed as False is the default already
        # when -l is not given on the command line. Including it
        # for illustration.
        help="Prints details about each file in the format -\n"
        "<timestamp> <filesize> <filename>",
    )
    parser.add_argument(
        "-F",
        "--formatted",
        action="store_true",
        default=False,
        help="Adds a character to tell you whether its a file or a directory.",
    )

    # Now we ask argparse to use the above information to interpret the
    # arguments and give us an object which will have `.dirname`,
    # `.longform` and `/.formatted` attributes we can access instead of
    # having to check for all the combinations ourselves.
    # Furthermore, if you call your program with either the `-h` or `--help``
    # flag, it will print out all of the specification above in a nice format
    # as help. This is a convention employed by most command line programs.
    args = parser.parse_args()

@log_function
def pyls(dirname: str, longform: bool, formatted: bool) -> None:
    """
    DATA REPRESENTATION
    -------------------

    In this case, we're choosing a **representation** where we represent
    the directory name to list as a string and the choice of longform and
    formatted output as two boolean values.

    SIGNATURE
    ---------
    The "signature" of the procedure below can be written as
              str bool bool -> None

    PURPOSE
    -------

    TODO: Replace this content with a sentence or two describing what this
    function does.
    - :param dirname: Lists all the files and directories in the specified directory
    - :param longform: Prints additional details about the files and directories in the specified folder/directory
    - :param formatted: Prints additional characters to show if the listed names are files or directories

    EXAMPLES
    --------

    TODO: Below, give a few examples of what you expect the procedure to do when you
    give various inputs. This can help you think about what to implement.
    Consider various possible combinations.
    """
    # Replace the "pass" below with your implementation.
    dir_list = os.listdir(dirname)
    if formatted and longform:
        # If both Longform and formatted is toggled on
        for entry in dir_list:
            path = os.path.join(".", entry)
            if os.path.isdir(path):
                stat = os.stat(path)
                atime = datetime.datetime.fromtimestamp(stat.st_atime).strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                mtime = datetime.datetime.fromtimestamp(stat.st_mtime).strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                size_mb = stat.st_size / (1024)
                print(f"Last modified: {mtime} | Last Accessed: {atime} | {size_mb:.2f} KB | {entry}/ \n")
            else:
                stat = os.stat(path)
                atime = datetime.datetime.fromtimestamp(stat.st_atime).strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                mtime = datetime.datetime.fromtimestamp(stat.st_mtime).strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                size_mb = stat.st_size / (1024)
                print(f"Last modified: {mtime} | Last Accessed: {atime} | {size_mb:.2f} KB | {entry}* \n")
    elif formatted:
        # Only if formatted it toggled on
        for entry in dir_list:
            path = os.path.join(".", entry)
            if os.path.isdir(path):
                print(f"{entry}/")
            else:
                print(f"{entry}*")
    elif longform:
        # Only if Longform is toggled on
        for entry in dir_list:
            path = os.path.join(".", entry)
            stat = os.stat(path)
            atime = datetime.datetime.fromtimestamp(stat.st_atime).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            mtime = datetime.datetime.fromtimestamp(stat.st_mtime).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            size_mb = stat.st_size / (1024)
            print(f"Last modified: {mtime} | Last Accessed: {atime} | {size_mb:.2f} KB | {entry} \n")
    else:
        print(dir_list)


# A python module may be loaded in one of two ways --
# 1. `python myfile.py`: In this case, the python file/module is considered to be
#    a "main program" and is named "__main__" within. So if you want to run code
#    only in this mode, you check whether __name__ is "__main__" and run that code.
# 2. `import myfile`: (within some other python file). In this mode, it is a pure
#    "module" that exposes functions and values via `myfile.` notation within the
#    importing python file. In this case, __name__ will be "myfile" and not "__main__".
if __name__ == "__main__":
    # Function sig: dirname: str, longform: bool, formatted: bool
    pyls(".", True, True)
    logger.debug(f'End of script: {os.path.basename(os.path.abspath(__file__))}')
