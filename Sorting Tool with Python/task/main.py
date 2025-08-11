import argparse
from math import floor
from collections import Counter

parser = argparse.ArgumentParser()
# parser.add_argument("-dataType", type=str, choices= ['long', 'line', 'word'], default='word')
# parser.add_argument("-sortingType", type=str, choices= ['natural', 'byCount'], default='natural')
#parser.add_argument("input_str", type=str, nargs='*')
parser.add_argument("-dataType", type=str, nargs='?', const='void', default='word')
parser.add_argument("-sortingType", type=str, nargs='?', const='void', default='natural')
# parser.add_argument("arg_list", type=str, nargs='*')
args = parser.parse_known_args()
inputs = []
do_exit = False
sort_type = args[0].sortingType
if sort_type not in ['natural', 'byCount']:
    print('No sorting type defined!')
    do_exit = True
data_type = args[0].dataType
if data_type not in ['long', 'line', 'word']:
    print('No data type defined!')
    do_exit = True

for extra_arg in args[1]:
    # if extra_arg.startswith('-'):
    print(f'{extra_arg} is not a valid parameter. It will be skipped.')

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

    def print_elements(self):
        print(f'Total {self.TEXT_HEAD[self.nature]}: {self.n_elements}.')
        if self.sorting == 'natural':
            if self.nature == 'line':
                print('Sorted data:')
                for l in self.sorted_elements:
                    print(l)
            else:
                print('Sorted data:', *self.sorted_elements)
        elif self.sorting == 'byCount':
            for i in range(len(self.counted_elements)):
                e, c = self.counted_elements[i]
                print(f'{e}: {c} time(s), {floor(100 * c / self.n_elements)}%')

# Build the lists, according to their type (as defined by -dataType)
# based on the user inputs
if not do_exit:
    while True:
        try:
            if data_type == 'line':
                # read the lines as a single element each
                data = [input().rstrip()]
            # elif data_type == 'word':
            else:
                # read as string elements
                data = input().split()
                if data_type == 'long':
                    data_clean = []
                    for ix in range(len(data)):
                        try:
                            data_clean.append(int(data[ix]))
                        except ValueError:
                            print(f'{data[ix]} is not a long. It will be skipped.')
                    data = data_clean
            inputs.extend(data)
        except EOFError:
            break

    element = Element(inputs, data_type, sort_type)
    element.do_sort()
    element.print_elements()
