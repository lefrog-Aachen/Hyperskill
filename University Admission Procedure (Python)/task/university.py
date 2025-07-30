# from typing import Any
from scipy.integrate import lebedev_rule


class Department:

    def __init__(self, name, places):
        self.name = name
        self.places = places
        self.students = []
        self.candidates = []

    def rank_candidates(self):
        self.candidates.sort(key=lambda x: (-float(x[2]), x[0], x[1]))

    def admit_students(self):
        while self.places > 0 and len(self.candidates) > 0:
            self.students.append(tuple(self.candidates.pop(0)[0:3]))
            self.places -= 1
        # don't forget to sort again when the 2nd or 3rd choices are added
        self.students.sort(key=lambda x: (-float(x[2]), x[0], x[1]))

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def add_seats(self, seats):
        self.places += seats

    def clear_candidates(self):
        self.candidates.clear()

class University:
    def __init__(self, departments, candidates):
        self.departments = {}
        self.department_names= []
        for department in departments:
            dep = Department(department, 0)
            self.departments[department] = dep
            self.department_names.append(department)
        self.candidates = candidates

    def sort_candidates(self):
        for c in self.candidates:
            if len(c) > 3:
                choice = c[3]
                if choice in self.departments.keys():
                    self.departments[choice].add_candidate(c)
                    c.remove(choice)

    def open_class(self, classname, seats):
        if classname in self.departments.keys():
            self.departments[classname].add_seats(seats)

    def process_admission(self):
        while self.candidates and len(self.candidates[0]) > 3:
            self.sort_candidates()
            self.candidates.clear()
            for d_n in self.department_names:
                dpt = self.departments[d_n]
                dpt.rank_candidates()
                dpt.admit_students()
                self.candidates.extend(dpt.candidates)
                dpt.clear_candidates()

 # DEBUG
if __name__ == '__main__':
    # filename = '/Users/rbutaud/InCirT/Dev/University Admission Procedure (Python)/University Admission Procedure (Python)/task/applicants.txt'
    # filename = '/Users/rbutaud/InCirT/Dev/University Admission Procedure (Python)/University Admission Procedure (Python)/task/app1.txt'
    filename = '/Users/rbutaud/InCirT/Dev/University Admission Procedure (Python)/University Admission Procedure (Python)/task/applicants_test2.txt'
else:
    filename = 'applicants.txt'
debug = '/Users/rbutaud/InCirT/Dev/University Admission Procedure (Python)/University Admission Procedure (Python)/task/applicants_test.txt'

DEPARTMENTS = ('Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics')
n = int(input())

applicants = []

with open(filename, "r") as file:
    with open(debug, 'w') as output:
        for line in file:
            applicants.append(line.split())
            print(line.rstrip(), file=output)
uni = University(DEPARTMENTS, applicants)
for d in DEPARTMENTS:
    uni.open_class(d, n)

uni.process_admission()
for d in uni.department_names:
    print(d)
    for s in uni.departments[d].students:
        print( *s)
    print('')
# for iteration in range(3):
#     if len(applicants) > 0:
#         for department in DEPARTMENTS:
#             dept_list = [app[:3] for app in applicants if app[3+iteration] == department]
#
#
#
#
#
# admission = Admission(applicants, n)
# admission.rank_candidates()
# for dpt in admission.DEPARTMENTS:
#     print(admission)
#
# # admissions is the file with the admitted candidates
# admission = { d: [n] for d in departments }
# with open(filename,"r") as file:
#     for line in file:
#         applicants.append(line.split())
#
# with open("debug.txt", "w") as file:
#     print(applicants, file=file)
#     applicants.sort(key=lambda applicant: (-float(applicant[2]), applicant[0], applicant[1]))
#     print(applicants, file=file)
#     while positions > 0 and applicants:
#         applicants, admission, positions = process_admissions(applicants, admission, positions)
#     for dpt in departments:
#         print(admission[dpt], file=file)
#     print(applicants, file=file)
#
# for dpt in departments:
#     print(dpt)
#     for admitted in admission[dpt][1:]:
#         print(*admitted)

