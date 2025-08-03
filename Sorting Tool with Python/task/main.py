import argparse
from math import floor
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument("-dataType", type=str, choices= ['long', 'line', 'word'], default='word')
parser.add_argument("-sortingType", type=str, choices= ['natural', 'byCount'], default='natural')
args = parser.parse_args()
inputs = []

sort_type = args.sortingType
data_type = args.dataType

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
        # if self.sorting == 'natural':
        self.sorted_elements = sorted(self.elements)
        # elif self.sorting == 'byCount':
        self.counted_elements = Counter(self.elements).most_common()
        self.counted_elements.sort(key=lambda x: (x[1], x[0]))
        # print(self.counted_elements)

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
            # for item in sorted(self.counted_elements):
            # for e in self.counted_elements.keys():
            #     print(self.counted_elements)
                e, c = self.counted_elements[i]
                # print(e, c)
                # c = self.counted_elements[e]
                print(f'{e}: {c} time(s), {floor(100 * c / self.n_elements)}%')
            # for e, c in self.sorted_elements:
            #     print(f'{e}: {c} time(s), {floor(100 * c / self.n_elements)}%')

# Build the lists, according to their type (as defined by -dataType)
# based on the user inputs
while True:
    try:
        if data_type == 'line':
            # read the lines as a single element each
            data = [input().rstrip()]
        elif data_type == 'word':
            # read as string elements
            data = input().split()
        else:
            # read as integer
            data = [int(n) for n in input().split()]
        inputs.extend(data)
    except EOFError:
        break

element = Element(inputs, data_type, sort_type)
element.do_sort()
element.print_elements()

# 
# def do_count_size(elements, el_type):
#     l_cnt = len(elements)
#     max_val = 0
#     longest = None
#     if el_type == 'long':
#         longest = max(elements)
#     else:
#         for l in elements:
#             if len(l) > max_val:
#                 max_val = len(l)
#                 longest = l
#     num = inputs.count(longest)
#     return l_cnt, longest, num
# 
# text = {'long': ['greatest','number'],
#         'word': ['longest','word'],
#         'line': ['longest','line']}
# 
# cnt, longest, num = do_count_size(inputs, n_type)
# 
# print(f'Total {text[n_type][1]}s: {cnt}.')
# if do_sort:
#     s_inputs = sorted(inputs, key=lambda x: int(x))
#     print('Sorted data:',*s_inputs)
# elif n_type == 'line':
#     print('The longest line:')
#     print(longest)
#     print(f'({num} time(s), {floor( 100 * num / cnt)}%).')
# else:
#     print(f'The {text[n_type][0]} {text[n_type][1]}: {longest} ({num} time(s), {floor( 100 * num / cnt)}%).')