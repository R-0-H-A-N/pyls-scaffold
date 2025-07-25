import argparse
import os
import datetime


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


def pyls(dirname: str = ".", longform: bool = False, formatted: bool = False) -> None:
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
    - :param dirname: Lists all the files and directories in the specified directory
    - :param longform: Prints additional details about the files and directories in the specified folder/directory
    - :param formatted: Prints additional characters to show if the listed names are files or directories

    EXAMPLES
    --------
    # List all files and directories in the current directory (default, no options)
    pyls(".")
    # Output: ['file1.txt', 'file2.py', 'subdir', ...]

    # List all files and directories in the specified directory
    pyls("/tmp")
    # Output: ['temp1.txt', 'temp2.log', 'folderA', ...]

    # List with longform details (timestamps, size, name)
    pyls(".", longform=True)
    # Output:
    # Last modified: 2024-06-01 12:00:00 | Last Accessed: 2024-06-01 12:00:00 | 1.23 KB | file1.txt
    # Last modified: ... | ... | ... | subdir
    # ...

    # List with formatted output (add '/' for directories)
    pyls(".", formatted=True)
    # Output:
    # file1.txt
    # file2.py
    # subdir/
    # ...

    # List with both longform and formatted output
    pyls(".", longform=True, formatted=True)
    # Output:
    # Last modified: 2024-06-01 12:00:00 | Last Accessed: 2024-06-01 12:00:00 | 1.23 KB | file1.txt
    # Last modified: ... | ... | ... | subdir/
    # ...

    """
    dir_list = os.listdir(dirname)
    if formatted and longform:
        # If both Longform and formatted is toggled on
        for entry in dir_list:
            path = os.path.join(dirname, entry)
            if os.path.isdir(path):
                longform_getinfo(path, entry, "/")
            else:
                longform_getinfo(path, entry)
    elif formatted:
        # Only if formatted it toggled on
        for entry in dir_list:
            path = os.path.join(dirname, entry)
            if os.path.isdir(path):
                print(f"{entry}/")
            else:
                print(f"{entry}")
    elif longform:
        # Only if Longform is toggled on
        for entry in dir_list:
            path = os.path.join(dirname, entry)
            longform_getinfo(path, entry)
    else:
        print(dir_list)


def longform_getinfo(path: str, entry: str, suffix: str = ""):
    """
    This is a helper function for the longform info code block

    SIGNATURE
    ---------
        str, str, str -> None

    PARAMETERS
    ----------
    - :param path: Path of the file/directory
    - :param dir_list: The list of strings of the files and directories in the specified location
    - :param suffix: The end character used to differentiate between a file and a directory when looking at the stdout (OPTIONAL)
    """

    stat = os.stat(path)
    atime = datetime.datetime.fromtimestamp(stat.st_atime).strftime("%Y-%m-%d %H:%M:%S")
    mtime = datetime.datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    size_kb = stat.st_size / (1024)
    print(
        f"Last modified: {mtime} | Last Accessed: {atime} | {size_kb:.2f} KB | {entry}{suffix} \n"
    )


# A python module may be loaded in one of two ways --
# 1. `python myfile.py`: In this case, the python file/module is considered to be
#    a "main program" and is named "__main__" within. So if you want to run code
#    only in this mode, you check whether __name__ is "__main__" and run that code.
# 2. `import myfile`: (within some other python file). In this mode, it is a pure
#    "module" that exposes functions and values via `myfile.` notation within the
#    importing python file. In this case, __name__ will be "myfile" and not "__main__".
if __name__ == "__main__":
    # Function signature: dirname: str, longform: bool, formatted: bool
    pyls(".", False, True)
