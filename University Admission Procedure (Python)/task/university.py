# m = int(input())
# applicants = []
# for i in range(n):
#     candidate = input().split()
#     applicants.append(candidate)
# applicants.sort(key = lambda x: (-float(x[2]), x[0], x[1]))
# print('Successful applicants:')
# for i in range(m):
#     print(f'{applicants[i][0]} {applicants[i][1]}')

filename = 'applicant_list.txt'

def process_admissions(candidates, admitted, positions):
    left_candidates = []
    for c in candidates:
        if len(c) > 3:
            choice = c[3]
            if admitted[choice][0] > 0:
                admitted[choice][0] -= 1
                positions -= 1
                admitted[choice].append(c[0:3])
                # print(f'{c[0:2]} admitted in {choice} with a GPA of {c[2]}')
            else:
                c.remove(choice)
                left_candidates.append(c)
        else:
            return None, admitted, positions
    return left_candidates, admitted, positions

departments = ('Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics')
n = int(input())
positions = n*5
applicants = []
admission = { d: [n] for d in departments }
with open(filename,"r") as file:
    for line in file:
        applicants.append(line.split())

with open("debug.txt", "w") as file:
    print(applicants, file=file)
    applicants.sort(key=lambda applicant: (-float(applicant[2]), applicant[0]))
    print(applicants, file=file)
    while positions > 0 and applicants:
        applicants, admission, positions = process_admissions(applicants, admission, positions)
    for dpt in departments:
        print(admission[dpt], file=file)
    print(applicants, file=file)

for dpt in departments:
    print(dpt)
    for admitted in admission[dpt][1:]:
        print(*admitted)
