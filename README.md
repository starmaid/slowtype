# slowtype.py

This python module makes it possible to generate
output from programs that mimics human typing style.

This program is used to emulate the styles of
Jon Bois's hit webcomics, 17776 and 20020. 
This massively decreases video production time,
especially for content that is already written.

Color utilities can also be used for displaying 
homestuck pesterlog content in a terminal.

## Usage

There are two primary ways to use this software

### Reading a Script

This is the easiest way, just put your text in the
templates for `script.txt` and `chars.txt` and the
program, when run in the same directory, will read
the script with the apropriate formatting.

### Incorperating into other programs

import the module with

```Python
from slowtype.py import Slowtype
```

and then create a new object

```Python
S = Slowtype('chars.txt')
```

and then you can have it read any line in the script with

```Python
S.cute_print(line)
```