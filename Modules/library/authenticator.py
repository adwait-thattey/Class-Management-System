from Classes import *

data_file_paths = {"student":"../data/student_data.csv" , "professor":"../data/professor_data.csv"}


def authent_student_login (in_mail,in_pass):
	try:
        F = open(data_file_paths[student], mode='r')
    except:
        print('Error in opening File')
        exit()
    F.readline()

    for line in F:
    	if (in_mail == (line.split(','))[2] && in_pass == (line.split(','))[6]):
    		return True
	return False

def authent_professor_login (in_mail,in_pass):
	try:
        F = open(data_file_paths[professor], mode='r')
    except:
        print('Error in opening File')
        exit()
    F.readline()

    for line in F:
    	if (in_mail == (line.split(','))[2] && in_pass == (line.split(','))[4]):
    		return True
	return False


def new_student_info ():
	try:
        F = open("../data/present_student.csv", mode='r')
    except:
        print('Error in opening File')
        exit()

   	F.readline()

   	for line in F:
   		info = []
   		info = line.split(',')

   		new_stud = student.new_student(info[0],info[1],info[2],info[3],info[4])
   		new_stud.put_to_file()

   	F.close()


