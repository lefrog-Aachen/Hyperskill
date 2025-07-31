import argparse
from math import floor
parser = argparse.ArgumentParser()
parser.add_argument("-dataType", type=str, choices= ['long', 'line', 'word'], default='word')
args = parser.parse_args()
# if args.dataType == 'word':
#     print('choice is word')
inputs = []
while True:
    try:
        if args.dataType == 'line':
            data = [input().rstrip()]
        else:
            data = input().split()
        inputs.extend(data)
    except EOFError:
        break

if args.dataType == 'line':
    l_count = len(inputs)
    print(f'Total lines: {l_count}.')
    print(f'The longest line:')
    l_max = 0
    longest_line = None
    for l in inputs:
        if len(l) > l_max:
            l_max = len(l)
            longest_line = l
    print(longest_line)
    n_l = inputs.count(longest_line)
    print(f'({n_l} time(s), {floor(100*n_l/l_count)}%).')

if args.dataType == 'word':
    l_count = len(inputs)
    print(f'Total words: {l_count}.')
    l_max = 0
    longest_word = None
    for l in inputs:
        if len(l) > l_max:
            l_max = len(l)
            longest_word = l
    n_l = inputs.count(longest_word)
    print(f'The longest word: {longest_word} ({n_l} time(s), {floor(100*n_l/l_count)}%).')

if args.dataType == 'long':
    l_count = len(inputs)
    print(f'Total numbers: {l_count}.')
    l_max = max(inputs)
    n_l = inputs.count(l_max)
    print(f'The greatest number: {l_max} ({n_l} time(s)), {floor(100*n_l/l_count)}%.')
