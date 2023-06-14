# Python Template Repository

![python_logo](https://github.com/I506dk/Python-Template/assets/33561466/cabea7fe-cfc8-48fb-a155-801b177725ad)

#### A python template for use with all python projects and repositories

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![CodeQL](https://github.com/I506dk/Python-Template/workflows/CodeQL/badge.svg)
![Latest version](https://github.com/i506dk/Python-Template/actions/workflows/versioning.yml/badge.svg)

## Features
- Automatically configure semantic versioning and releases
- Leverage CodeQL for code scanning
- Simple foundation to build automation scripts or projects on

## Dependencies
- [Python](https://www.python.org/downloads/) - Programming language that lets you work quickly
and integrate systems more effectively.

## Installation
**Download the latest release of python below:**

[![Python Latest](https://img.shields.io/badge/python-latest-blue.svg)](https://www.python.org/downloads/windows/)

**Download and install Pip using the following commands:**
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
**Dependencies can be installed using requirements.txt:**
```
pip install -r requirements.txt
```
**Or individually installed via Pip:**
```
pip install example_package
```

## Usage
To run example_script.py for the first time:
```
python example_script.py
```
This will run the script, and require user interaction

Arguments can be passed to the script or executable if automation is wanted.

(***-h or --help***) - will display the help screen.

- Examples: ```python example_script.py -h``` or ```python example_script.py --help```

(***-a1 or --argument_1***)  - the first argument in the example script.

- Examples: ```python example_script.py -a1``` or ```python example_script.py --argument_1```

(***-a2 or --argument_2***)  - the second argument in the example script.

- Examples: ```python example_script.py -a2``` or ```python example_script.py --argument_2```

(***-a3 or --argument_3***)  - the third argument in the example script.

- Examples: ```python example_script.py -a3``` or ```python example_script.py --argument_3```

REMINDER - You can use multiple arguments as long as they aren't -h or --help (Those will default to showing the help screen then exiting)

Example run using arguments:
```
python example_script.py -a1 my_first_string -a2 my_second_string -a3 my_third_string
```

## Troubleshooting
If python isn't found or won't start, make sure that it is added to PATH when installed.

## To Do
- [x] Add to this repository as needed
- [x] Configure code scanning with CodeQL
- [x] Configure Semantic versioning
- [x] Configure releases
- [ ] Use as a template for future repositories
