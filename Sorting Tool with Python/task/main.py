import argparse
from math import floor
from collections import Counter
class Element:
    TEXT_HEAD = {'long': 'numbers', 'word': 'words', 'line': 'lines'}
    def __init__(self, elements, nature, sorting):
        self.elements = elements
        self.nature = nature
        self.sorting = sorting
        self.sorted_elements = []
        self.n_elements = len(elements)
        self.counted_elements = {}

    def do_sort(self):
        self.sorted_elements = sorted(self.elements)
        self.counted_elements = Counter(self.elements).most_common()
        self.counted_elements.sort(key=lambda x: (x[1], x[0]))

    def print_elements(self, o_file):
        print(f'Total {self.TEXT_HEAD[self.nature]}: {self.n_elements}.', file=o_file)
        if self.sorting == 'natural':
            if self.nature == 'line':
                print('Sorted data:', file=o_file)
                for l in self.sorted_elements:
                    print(l, file=o_file)
            else:
                print('Sorted data:', *self.sorted_elements, file=o_file)
        elif self.sorting == 'byCount':
            for i in range(len(self.counted_elements)):
                e, c = self.counted_elements[i]
                print(f'{e}: {c} time(s), {floor(100 * c / self.n_elements)}%', file=o_file)

def process_data(in_str, entry_type):
    if entry_type == 'line':
        data_out = [in_str.rstrip()]
    else:
    # read as string elements
        data_out = in_str.split()
    # this is good for word type but not for long, in that case
    if entry_type == 'long':
        # need to check if they're all integers
        data_out_clean = []
        for num in range(len(data_out)):
            try:
                data_out_clean.append(int(data_out[num]))
            except ValueError:
                print(f'{data_out[num]} is not a long. It will be skipped.')
        data_out = data_out_clean
    if in_str == '':
        data_out = 'exit'
    return data_out

parser = argparse.ArgumentParser()
parser.add_argument('-dataType', type=str, nargs='?', const='void', default='word')
parser.add_argument('-sortingType', type=str, nargs='?', const='void', default='natural')
parser.add_argument('-inputFile', type=str)
parser.add_argument('-outputFile', type=str)
# parser.add_argument("arg_list", type=str, nargs='*')
args = parser.parse_known_args()
inputs = []
do_exit = False
out_file = None
in_file = None
out_f = None
sort_type = args[0].sortingType
if sort_type not in ['natural', 'byCount']:
    print('No sorting type defined!')
    do_exit = True
data_type = args[0].dataType
if data_type not in ['long', 'line', 'word']:
    print('No data type defined!')
    do_exit = True

in_file = args[0].inputFile
out_file = args[0].outputFile

for extra_arg in args[1]:
    # if extra_arg.startswith('-'):
    print(f'{extra_arg} is not a valid parameter. It will be skipped.')

# Build the lists, according to their type (as defined by -dataType)
# based on the user inputs
dbg = open('debug.txt', 'w')
read_file = False
if in_file is not None:
    read_file = True
    i_f = open(in_file, 'r')

if out_file is not None:
    out_f = open(out_file, 'w')

if not do_exit:
    while True:
        try:
            if in_file is not None:
                in_data = i_f.readline()
            else:
                in_data = input()
            data = process_data(in_data, data_type)
            print(data, file=dbg)
            if data == 'exit':
                break
            if data is not None:
                inputs.extend(data)
        except EOFError:
            break

    element = Element(inputs, data_type, sort_type)
    element.do_sort()
    element.print_elements(out_f)
if in_file is not None:
    i_f.close()
if out_file is not None:
    out_f.close()
dbg.close()