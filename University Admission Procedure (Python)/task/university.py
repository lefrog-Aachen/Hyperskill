res = []
for i in range(3):
    response = int(input())
    res.append(response)
grade = sum(res) / 3
print(grade)
if grade >= 60:
    print('Congratulations, you are accepted!')
else:
    print('We regret to inform you that we will not be able to offer you admission.')
