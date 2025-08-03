import argparse
from math import floor
parser = argparse.ArgumentParser()
parser.add_argument("-dataType", type=str, choices= ['long', 'line', 'word'], default='word')
parser.add_argument("-sortIntegers", action='store_true')
args = parser.parse_args()
# if args.dataType == 'word':
#     print('choice is word')
with open('debug.txt', 'a') as f:
    f.write(f'{args.dataType}, {args.sortIntegers}\n')
inputs = []
do_sort = args.sortIntegers
n_type = args.dataType
if  do_sort:
    n_type = 'long'
while True:
    try:
        if n_type == 'line':
            data = [input().rstrip()]
        else:
            data = input().split()
        inputs.extend(data)
        with open('debug.txt', 'a') as f:
            f.write(f'{data}')
    except EOFError:
        break

def do_count_size(elements, el_type):
    l_cnt = len(elements)
    max_val = 0
    longest = None
    if el_type == 'long':
        longest = max(elements)
    else:
        for l in elements:
            if len(l) > max_val:
                max_val = len(l)
                longest = l
    num = inputs.count(longest)
    return l_cnt, longest, num

# text = {'long': 'The greatest number:',
#     'word': 'The longest word:',
#     'line': 'The longest line:\n'}
text = {'long': ['greatest','number'],
        'word': ['longest','word'],
        'line': ['longest','line']}

cnt, longest, num = do_count_size(inputs, n_type)

new_case = True
debug = False
f = open('debug.txt', 'a')
if new_case:
    print(f'Total {text[n_type][1]}s: {cnt}.')
    if do_sort:
        s_inputs = sorted(inputs, key=lambda x: int(x))
        print('Sorted data:',*s_inputs)
    elif n_type == 'line':
        print('The longest line:')
        print(longest)
        print(f'({num} time(s), {floor( 100 * num / cnt)}%).')
    else:
        print(f'The {text[n_type][0]} {text[n_type][1]}: {longest} ({num} time(s), {floor( 100 * num / cnt)}%).')
else:
    if args.dataType == 'line':
        l_count = len(inputs)
        print(f'Total lines: {l_count}.')
        print(f'The longest line:')
        if debug:
            print(f'Total lines: {l_count}.', file=f)
            print(f'The longest line:', file=f)
        l_max = 0
        longest_line = None
        for l in inputs:
            if len(l) > l_max:
                l_max = len(l)
                longest_line = l
        print(longest_line)
        if debug:
            print(longest_line, file=f)
        n_l = inputs.count(longest_line)
        print(f'({n_l} time(s), {floor(100*n_l/l_count)}%).')
        if debug:
            print(f'({n_l} time(s), {floor(100 * n_l / l_count)}%).', file=f)
    if args.dataType == 'word':
        l_count = len(inputs)
        print(f'Total words: {l_count}.')
        if debug :
            print(f'Total words: {l_count}.', file=f)
        l_max = 0
        longest_word = None
        for l in inputs:
            if len(l) > l_max:
                l_max = len(l)
                longest_word = l
        n_l = inputs.count(longest_word)
        print(f'The longest word: {longest_word} ({n_l} time(s), {floor(100*n_l/l_count)}%).')
        if debug:
            print(f'The longest word: {longest_word} ({n_l} time(s), {floor(100 * n_l / l_count)}%).', file=f)
    if args.dataType == 'long':
        l_count = len(inputs)
        print(f'Total numbers: {l_count}.')
        l_max = max(inputs)
        n_l = inputs.count(l_max)
        print(f'The greatest number: {l_max} ({n_l} time(s)), {floor(100*n_l/l_count)}%.')
f.close()