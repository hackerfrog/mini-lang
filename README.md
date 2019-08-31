# mini-lang
 
mini-lang is overlay programming language build on top of python, with aim to provide extra flavor to primary language.

## Requirements

python v3.0 or greater

## Download & Run
```
git clone https://github.com/hackerfrog/mini-lang.git
cd mini-lang
python shell.py
```
## Examples

```
>> 1 + 2 * 3
7

>> (1 + 2) * 3
9

```
## Error Handling Example

```
>> 4/0
Run Time Error: Division by zero
File: <stdin>, Line: 1, Column: 3

4/0
~~^
```
```
>> (1+2
Invalid Syntax: Expected ')'
File: <stdin>, Line: 1, Column: 5

(1+2
~~~~^
```
## Exit shell.py

To exit from infinite loop of shell, type `:x` or `::exit`.
