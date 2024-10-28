## Versionbump    

Versionbump is a simple application for modifying version strings either by 
incrementing a "field" or by replacing whole strings.

There are many other projects that do similar things to versionbump, and this 
certainly is not the best of them.

Feel free to employ it in your build processes. More importantly, 
learn from it, improve it and share it.

### Installation

Thebest way to install versionbump is by cloning the repository locally and 
using `pip` to install it.

*Hint:* For an OS-agnostic guide to setting up your Python environment, see 
[Python Packaging User Guide - Installing Packages][python-setup].

To install versionbump:

```
$ cd <versionbump-path>

$ pip install .
```

### Usage

The best way to start using versionbump is to take a look at the help.

```
$  versionbump --help
usage: versionbump [-h] [-p [PATH]] -c [CURRENT_VERSION] [-r [REPLACE_VERSION]] [-i [INCREMENT_BY]] [-v]
                   [{major,minor,patch}]

positional arguments:
  {major,minor,patch}   Version field to increment. (Required)

options:
  -h, --help            show this help message and exit
  -p [PATH], --path [PATH]
                        Path to search. (Default='.')
  -c [CURRENT_VERSION], --current-version [CURRENT_VERSION]
                        Current version to bump. (Required)
  -r [REPLACE_VERSION], --replace-version [REPLACE_VERSION]
                        Replace current version with specified version. (Optional)
  -i [INCREMENT_BY], --increment-by [INCREMENT_BY]
                        Increment by value. (Default=1)
  -v, --version         show program's version number and exit
```

#### Options

`-p/--path`
Provide a valid path to search for files containing versions which needs to 
be incremented. This argument is optional, if no path is provided, versionbump 
defaults to the current working directory ('.').

`-c/--current-version`
Provide the current version to be matched in the files found by the `-p/--path` 
argument. This argument is **required**.

`-r/--replace-version`
Ignore the `field` and `increment` arguments and instead replace the current 
version with the value of the replace version argument.

`-i/--increment-by`
Provide an unsigned integer value to increment the current version field by. 
This argument is optional. If no value is supplied, it defaults to **1**.

`-v/--version`
Displays the version of the versionbump script and exits.

`field: {major, minor, patch}`
Provide the field name to be incremented. In this context, "field" refers to 
one of *major.minor.patch* (Ex: '1.1.0'). This argument is **required**.

### Configuration

Versionbump supports configuration via a user-editable file installed in the 
root install location called `_config.json`. Currently, user configuration is 
limited to modifying the list of file wildcards used by versionbump's search 
functionality.

By default, the list only contains the following:

```
{
    "search-patterns": 
    [
        "*.h",
        "*.txt"
    ]
}
```

However, you can choose to add anything to this list that might be in your 
source project and contains a version number.

For example, the `_config.json` I use looks like this:

```
{
    "search-patterns": 
    [
        "*.h",
        "*.txt",
        "*.ism",
        "*.properties",
        "*.groovy"
    ]
} 
```

### Examples

Bump the `minor` field of version `1.0.1` by an increment of 2:

`$ versionbump -c 1.0.1 minor -i 2`

Replace version `23.11.2` with version `24.1.0` in all source files under
the `my-project` path:

`$ versionbump -p .\my-project -c 23.11.2 -r 24.1.0`

### To-Do

* Add SCM support.
* Add support to pass mutiple version strings.
* Add support for Visual Studio headers (i.e. VersionInfo.h)
* Add alpha-numeric support for version strings (Ex: '1.2.3-dev0')
* Add support for pre-release tags (alpha, beta, rc, etc.)


[python-setup]: https://packaging.python.org/en/latest/tutorials/installing-packages/
[pypi]: https://pypi.org/
[semver]: https://semver.org/
[software-versioning]: https://en.wikipedia.org/wiki/Software_versioning#Semantic_versioning