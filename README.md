# as115
The as31 assembler used for MIT's 6.115 course (Microcontrollers Lab) loaded with extra preprocessing directives that makes it nicer to use.

## Features

It allows you to place `.inc` directive anywhere in an assembly file that tells the preprocessor to insert the contents of a given file in your assembly file. I made it so that I could distribute large projects over multiple files. Check out the files in the `Test` directory for usage.

It also has the additional feature that it will automatically end your files with a newline character so as31 won't complain.

## Known Issues

* Error messages won't give the right line numbers.
* This has been tested only on a Windows machine. However, it has been designed also with Unix machines in mind, and it is python, so it should be easily portable to other platforms. Please email me at trehans@mit.edu if you can confirm this works on Mac or Linux or are able to modify the script so that it works.

## Documentation

Do `python as115.py -h` for usage. It should be identical to the usage of `as31`.
