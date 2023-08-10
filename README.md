# 0x00. AirBnB clone - The console

![Air_BnB_clone logo](logo/img.png)

---
# Console

A python command interpreter program built using the python module cmd. Contains to create, update, delete and print a class instance or all instaces created.

The console will perform the following tasks:

* create a new object
* retrive an object from a file
* do operations on objects
* destroy an object

---
## Environment

<!-- ubuntu -->
<a href="https://ubuntu.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A" alt="Suite CRM"></a> <!-- bash --> <a href="https://www.gnu.org/software/bash/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A" alt="terminal"></a> <!-- python--> <a href="https://www.python.org" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Python&color=FFD43B&logo=python&logoColor=3776AB&labelColor=2F333A" alt="python"></a> </a> <!-- vim --> <a href="https://www.vim.org/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A" alt="Suite CRM"></a> <!-- vs code --> <a href="https://code.visualstudio.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=5C2D91&logo=Visual%20Studio%20Code&logoColor=5C2D91&labelColor=2F333A" alt="Suite CRM"></a> </a><!-- git --> <a href="https://git-scm.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Git&color=F05032&logo=Git&logoColor=F05032&labelColor=2F333A" alt="git distributed version control system"></a> <!-- github --> <a href="https://github.com" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github"></a>
 <!-- Style guidelines -->
* Style guidelines:
  * [pycodestyle (version 2.7.*)](https://pypi.org/project/pycodestyle/)
  * [PEP8](https://pep8.org/)

All the development and testing was runned over an operating system Ubuntu 20.04 LTS using programming language Python 3.8.3. The editors used were VIM 8.1.2269, VSCode 1.6.1 and Atom 1.58.0 . Control version using Git 2.25.1.

---
## Getting Started
To start the command interpreter type in these commands in your terminal:

```bash
Cloning the repo and starting the console:
==========================================

git clone https://github.com/Jerry-kjk/AirBnB_clone.git
cd AirBnB_clone
./console.py
```

## Usage
Help for the console program can be obtained by running the program first and with the help command. This will show the available commands:

```bash
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

You can get help for specific command by specifing help <command>. For example

(htnb) help create

Usage: create BaseModel

        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
```

## Usage and Examples

```bash
./console.py

# Create a BaseModel instance and print its id
(htnb) create BaseModel
b61e46d6-9143-4d37-b271-ce76a759d6a6

# to print the instance
(htnb) show BaseModel b61e46d6-9143-4d37-b271-ce76a759d6a6
[BaseModel] (b61e46d6-9143-4d37-b271-ce76a759d6a6) {'id': 'b61e46d6-9143-4d37-b271-ce76a759d6a6', 'created_at': datetime.datetime(2021, 6, 30, 11, 34, 53, 117968), 'updated_at': datetime.datetime(2021, 6, 30, 14, 34, 53, 118060)}

# to print all object created previously
(htnb) all
["[BaseModel] (b61e46d6-9143-4d37-b271-ce76a759d6a6) {'id': 'b61e46d6-9143-4d37-b271-ce76a759d6a6', 'created_at': datetime.datetime(2021, 6, 30, 11, 34, 53, 117968), 'updated_at': datetime.datetime(2021, 6, 30, 14, 34, 53, 118060)}", "[BaseModel] (426aea0f-5012-4a52-9a3a-3c775ff98e07) {'id': '426aea0f-5012-4a52-9a3a-3c775ff98e07', 'created_at': datetime.datetime(2021, 6, 30, 13, 29, 6, 1369), 'updated_at': datetime.datetime(2021, 6, 30, 13, 29, 6, 1383)}"]
```

---
## Authors

* **IAN MHAMBE** - [ianmhambe@gmail.com] (https://github.com)
* **JERRY KAJIK** - [jerrykajik@gmail.com] (https://github.com/jerry-kjk)
