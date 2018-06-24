from data import *



# for i in num:
# 	print(i)

course_arr = []

course = get_course_data()
for line in course:
	course_arr.append(line.split()[0])

course_arr = [i.split(',') for i in course_arr]


for i in range(1,len(num)):
	for j in range(1,len(num[i])):
		for k in course_arr:
			if (str(k[0]) in str(num[i][j])):
				num[i][j] = k[1]

F = open("dummy.csv",mode='w')

for i in num:
	F.write(",".join(i) + "\n")

F.close()
