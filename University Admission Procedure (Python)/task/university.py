
class Department:

    def __init__(self, university, dpt, places):
        self.university = university
        self.name = dpt[0]
        self.places = places
        self.students = []
        self.candidates = []
        self.subjects = [university.SUBJECTS[x] for x in dpt[1]]
    def rank_candidates(self):
        """
        Rank the candidates list according to the sorting method keeping the original format
        """
        self.candidates.sort(key=lambda x: (-x[2], x[0], x[1]))

    def admit_students(self):
        while self.places > 0 and len(self.candidates) > 0:
            student = self.candidates.pop(0)
            self.students.append(tuple(student[0:3]))
            self.places -= 1
            # remove the admitted student from the university waiting list
            self.university.candidates.pop(tuple(student[0:2]))
        # don't forget to sort again when the 2nd or 3rd choices are added
        # students have only 3 records as a tuple
        self.students.sort(key=lambda x: (-float(x[2]), x[0], x[1]))

    def add_candidate(self, candidate):
        candidate_record = candidate[0:2]
        candidate_grade = 0
        for subject in self.subjects:
            candidate_grade += int(candidate[subject])
        candidate_grade = candidate_grade / len(self.subjects)
        candidate_record.append(candidate_grade)
        self.candidates.append(tuple(candidate_record))

    def add_seats(self, seats):
        self.places += seats

    def clear_candidates(self):
        self.candidates.clear()

class University:
    DEPARTMENTS = (('Biotech', ['chem', 'physics']), ('Chemistry', ['chem']),
                   ('Engineering', ['computer', 'math']), ('Mathematics', ['math']),
                   ('Physics', ['physics', 'math'])
                   )
    SUBJECTS = {'physics': 2, 'chem': 3, 'math': 4, 'computer': 5}
    def __init__(self, candidates):
        self.departments = {}
        self.department_names= []
        for department in self.DEPARTMENTS:
            dep = Department(self, department, 0)
            self.departments[department[0]] = dep
            self.department_names.append(department[0])
        self.candidates = candidates

    def sort_candidates(self):
        """
        Distribute the candidates into the various departments according to their choice. Once
        placed into a department their choice is removed from the list
        """
        for c, v in self.candidates.items():
            if len(v) > BASIC_LENGTH:
                choice = v[BASIC_LENGTH]
                if choice in self.departments.keys():
                    candidate = list(c)
                    candidate.extend(v)
                    self.departments[choice].add_candidate(candidate)
                    v.remove(choice)
                    self.candidates[c] = v

    def open_class(self, classname, seats):
        if classname in self.departments.keys():
            self.departments[classname].add_seats(seats)

    def process_admission(self):
        rounds = 3
        while self.candidates and rounds > 0:
            self.sort_candidates()
            # Clear the candidates lists from the University as they are in their section now
            # self.candidates.clear()
            rounds -= 1
            for d_n in self.department_names:
                dpt = self.departments[d_n]
                dpt.rank_candidates()
                dpt.admit_students()
                # rebuild the candidates list - no need now
                # self.candidates.extend(dpt.candidates)
                dpt.clear_candidates()

# debug = False
# if __name__ == '__main__':
#     # filename = '/Users/rbutaud/InCirT/Dev/University Admission Procedure (Python)/University Admission Procedure (Python)/task/applicants.txt'
#     # filename = '/Users/rbutaud/InCirT/Dev/University Admission Procedure (Python)/University Admission Procedure (Python)/task/app1.txt'
# else:
# filename = 'applicants.txt'
# if debug:
# filename = '/Users/rbutaud/InCirT/Dev/University Admission Procedure (Python)/University Admission Procedure (Python)/task/applicant_list_5.txt'
filename = '/Users/rbutaud/InCirT/Dev/University Admission Procedure (Python)/University Admission Procedure (Python)/task/applicants_test5.txt'
debug = '/Users/rbutaud/InCirT/Dev/University Admission Procedure (Python)/University Admission Procedure (Python)/task/applicants_test_out.txt'

# basic length to be refined based on the minimum length for a record with at least one department choice
BASIC_LENGTH = 4
# if debug:
#     n = 4
# else:
n = int(input())

# applicants = []
# applicants format will be dictionary with:
# key = (first_name, last_name) as tuple
# content : [ physics chem math computer first_choice second_choice third_choice ]
applicants = {}
with open(filename, "r") as file:
    with open(debug, 'w') as output:
        for line in file:
            record = line.split()
            applicant_name = tuple(record[0:2])
            applicant_record = record[2:]
            # applicants.append(line.split())
            applicants[applicant_name] = applicant_record
            print(line.rstrip(), file=output)
uni = University(applicants)
for d in uni.department_names:
    uni.open_class(d, n)

uni.process_admission()
for d in uni.department_names:
    print(d)
    file_dept = f'{d.lower()}.txt'
    with open(file_dept, 'w') as output:
        for s in uni.departments[d].students:
            print( *s, file=output)
        # print('')

