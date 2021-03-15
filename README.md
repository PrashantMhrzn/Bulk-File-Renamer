# Bulk-File-Renamer
A program that renames all files of a folder.

## Usage

```bash
$ python3 renamer.py <path_to_folder> -n<naming_convention>

$ python3 renamer.py -h
usage: renamer.py [-h] [-n] path

Renames every file inside the given folder

positional arguments:
  path                 Absolute path of the
                       folder.

optional arguments:
  -h, --help           show this help
                       message and exit
  -n , --naming_convention 
                       Not specifing will
                       default to the name
                       <file>
```

## Example
```bash
$ python3 renamer.py ./test_folder -n test
File Renaming Completed!

Before:
[!alt_text](./SS/1.png)

After:
[!alt_text](./SS/2.png)

```

## Installation
```bash
pip/pip3 installl argparse
```


## License
[MIT](https://github.com/PrashantMhrzn/Bulk-File-Renamer/blob/main/LICENSE)