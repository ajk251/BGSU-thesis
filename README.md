# Falcon
――――――――――――――――――――――――――――――――――――――――――――――――

To install:

`python3 setup.py develop --user`

This installs Falcon in development mode, meaning that it is not fully installed and any changes made do not require re-installation.

For a better experience, add this to the .bashrc file:

`alias="python3 <some-path>/falcon.py"`

――――――――――――――――――――――――――――――――――――――――――――――――

Falcon is meant to be used the command-line. Falcon will create a Python test file (default), a unit test style file, or both. PyTest can be invoked right after creation. Also, `coverage.py` can be used to measure coverage, however the file must be specified.

By default it accepts a Falcon \*.fcn file.

* `-t --test`  [default] creates a Pytest-test file
* `-u --unit` [optional] creates a unit-test file
* `-d --debug` [optional] prints the generated tree
* `--pytest` [optional] runs PyTest after generation
* `--cov <filename.py>` [optional] measures coverage of the given file using coverage.py

Some examples of how it is used:

* `falcon project-tests.fcn` to create a basic test file
* `falcon project-tests.fcn -t -u` to create a basic test file and unit-test style file
* `falcon project-tests.fcn -t -u --pytest` create files and run PyTest
* `falcon project-tests.fcn -t -u --pytest --cov main.py` create files, run PyTest, use coverage.py on the specified file
