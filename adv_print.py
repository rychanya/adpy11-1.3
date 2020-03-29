def str_iter(in_str: str, max_line: int):
    while len(in_str) > max_line:
        yield in_str[:max_line]
        in_str = in_str[max_line:]
    yield in_str
    raise StopIteration


def adv_print(*args, **kwargs):
    start = kwargs.get('start') or ''
    max_line = kwargs.get('max_line')
    in_file = kwargs.get('in_file')
    if max_line:
        lines = [(start + line) for line in str_iter(args[0], max_line)]
    else:
        lines = [args[0], ]
    for line in lines:
        print(line)
    if in_file:
        with open(in_file, mode='w', encoding='utf-8') as file:
            for line in lines:
                file.write(line + '\n')


if __name__ == '__main__':
    adv_print('dfdfdffd', max_line=3, start='-', in_file='out.txt')
