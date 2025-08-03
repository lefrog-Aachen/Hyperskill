import argparse
from math import floor
parser = argparse.ArgumentParser()
parser.add_argument("-dataType", type=str, choices= ['long', 'line', 'word'], default='word')
parser.add_argument("-sortIntegers", action='store_true')
args = parser.parse_args()
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

text = {'long': ['greatest','number'],
        'word': ['longest','word'],
        'line': ['longest','line']}

cnt, longest, num = do_count_size(inputs, n_type)

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