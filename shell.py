from mini import mini
import sys

args = sys.argv[1:]

verbose = False

if '-v' in args:
    print('''
,_ _    ,_      |  _  ,_   _
| | | | | | | - | |_| | | |
| | | | | | |   | | | | | |_;
               - verbose [ON]
''')

while True:
    command = input('>> ')

    if command in [':x', '::exit']:
        break

    if not command.strip():
        continue

    result, error = mini.run('<stdin>', command)

    if error:
        print(error.as_string())
    elif result:
        print(result)