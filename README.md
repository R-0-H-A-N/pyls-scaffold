# pyls-scaffold

A template to get you going with the pyls assignment.

## Setup (once only)

1. Install the `uv` tool from https://docs.astral.sh/uv/ (See "Installation").
2. Ensure `uv` is runnable from your terminal/shell.
3. Open a terminal and change the current working directory to this directory.
4. Run `uv tool install ruff@latest pyright@latest`. VSCode users should
   install `Pylance` extension additionally.
5. Run `uv sync` . This will install the necessary dependencies. In our case,
   it is just `pytest`.
6. From now on, instead of running `python` directly, use `uv run`. For
   example, to run `pytest` on your work, run `uv run pytest` (or `uvx pytest`)
   instead of `pytest`. Or if you want to run your `pyls.py` script, use `uv
run pyls.py ...arguments...` instead of `python pyls.py ...arguments...`.
   This ensures that all the dependencies setup by `uv sync` are available to
   your program when it runs.

## Your task

There are two files - `pyls.py` which contains the main code for your program,
and `test_pyls.py` which contains code to test that your functions meet your
expectations. You'll need to fill in both in the indicated places.

## Code formatting

It is important for your own sake to stick to conventional python code
formatting so that your eyes get used to it and you can read quickly. This is
easily accomplished by running `uvx ruff format` from within your directory.
It'll rewrite all your python files using standard conventions.

**NOTE**: I recommend you do not try to deviate from standard conventions ...
not even when you are programming professionally. Any minor disagreements are
far less important than the ability of your peers to look at your code and be
able to read it fluently.

## "Linting"

Checking for minor syntactic and logical correctness of your programs is
usually known as "linting". "Linters" check for some common patterns of errors
made by programmers even if they may not be technically errors according to the
programming language. By catching these early, you can often save yourself some
trouble.

`ruff` provides a linter that runs so fast there is really no reason to not run
it every time you save your file! You run it using `uvx ruff check`. If the
check comes clean, it doesn't mean your program is error free, but if it is
pointing out something, it is likely a good idea to address it.

For example, "unused import" messages indicate some intended functionality that
is not implemented yet in your code, or you can remove the import to improve
load speed. Similarly "unused variables" indicate something missing in your
code -- you computed a variable but never used it, so perhaps you intended to
do something with it that you haven't done yet.
