import csv
data_file = '/Users/rbutaud/PycharmProjects/To-Do List (Python)/To-Do List (Python)/task/todolist/alcohol-available-for-consumption-year-ended-december-2019-csv.csv'
count = 0
with open(data_file, 'r') as d_f:
    file_reader = csv.DictReader(d_f, delimiter=',')
    for line in file_reader:
        if(line['MAGNITUDE'] == '0'):
            count += 1
            print(line)

    print(count)



