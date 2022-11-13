# Falcon
――――――――――――――――――――――――――――――――――――――――――――――――

To install:

`python3 setup.py develop --user`

This installs Falcon in development mode, meaning that it is not fully installed and any changes made do not require re-installation.

For a better experience, add this to the .bashrc file:

`alias="python3 <some-path>/falcon.py"

Then to use:

`falcon project-tests.fcn` to create a basic test file
`falcon project-tests.fcn -t -u` to create a basic test file and unit-test style file
`falcon project-tests.fcn -t -u --pytest` create files and run PyTest
`falcon project-tests.fcn -t -u --pytest --cov main.py` create files, run PyTest, use coverage.py on the specified file

――――――――――――――――――――――――――――――――――――――――――――――――

Falcon can be used on the command-line.

By default it must accept a Falcon <*>.fcn file.

* `-t --test`  [default] creates a Pytest-test file
* `-u --unit` [optional] creates a unit-test file
* `-d --debug` [optional] prints the generated tree
* `--pytest` [optional] runs PyTest after generation
* `--cov <filename.py>` [optional] measures coverage of the given file using coverage.py
