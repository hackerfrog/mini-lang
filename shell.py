from mini import mini

while True:
    command = input('>> ')

    if command in [':x', '::exit']:
        break

    if not command.strip():
        continue

    result, error = mini.run('<stdin>', command)

    if error:
        print(error.as_string())
    else:
        print(result)