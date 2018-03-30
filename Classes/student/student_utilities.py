from student_class import student

def get_student(student_id):
	try:
		file = open("class_data.csv", mode = "r")
	except:
		print("file is not present")
		exit()

	file.readline()

	for line in file:
		line = line.strip('\n').split(",")
		if(student_id == line[0] or student_id == int(line[0])):
			data = line
			break

	else :
		print("student not found")
		return None

	student_details = student.existing_student(data[0],data[1],data[2],data[3],data[4],data[5])
	return student_details 

def get_all_students():
	all_students = []
	all_ids = []
	try:
		file = open("course_data.csv", mode ="r")
	except:
		print("file not present")
		exit()

	file.readline()

	for line in file:
		all_ids.append(line.split(',')[0])

	file.close()

	for i in all_ids:
		all_students.append(get_student(i))

	return all_students

def clear_file():
	file = open("class_data.csv","w")
	file.write("Roll No , Name , Email , Batch , list of current courses , list of past courses ")
	file.close()
