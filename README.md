# dropbox

## Overview

My new project

## Setting up the environment

This project depends on [Python 2.7+ or 3.4+](https://www.python.org/).

Once you have installed Python for your environment, you
should also setup a [virtual environment](https://virtualenv.pypa.io/en/stable/)
with [pip](https://pip.pypa.io/en/stable/installing/).

Then, you should install the dependencies required by
the library as follows:

```
$ pip install -r requirements.txt
```

## Develop on the project

### Run tests

You can execute the library's tests as follows:

```
$ pytest tests
```

### Check code-style

This library does its best to follow
[PEP 8](https://www.python.org/dev/peps/pep-0008/) code style conventions. They
can be checked by running the following command:

```
$ pycodestyle dropbox
```

### Build the documentation

The documentation is written using the
[Sphinx](http://www.sphinx-doc.org/en/stable/) framework and can be built
as follows:

```
$ cd docs
$ make html
```

The generated output will be located into the `build` subdirectory.

