import argparse
parser = argparse.ArgumentParser()
parser.parse_args()

int_list = []
# while True:
#     try:
#         data = input().split()
#         int_list.extend(data)
#     except EOFError:
#         break

print(f'Total numbers: {len(int_list)}.')
# z = max(int_list)
z = 1
print(f'The greatest number: {z} ({int_list.count(z)} time(s)).')
