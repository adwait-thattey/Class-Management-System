from Classes import classroom
from Classes import student
from Classes import course
from Classes import professor
from Classes import batch
from Classes import data_file_paths

def get_classroom(classroom_id) :
    ''' Returns a course class object by filling it with details of the id of the course having same ID in the file '''
    data =[]
    try:
        F = open(data_file_paths["classroom"], mode='r')
    except:
        print("Error in opening file")
        exit()
    
    F.readline()  # To skip the first line as fire line is just information   
    
    for line in F :
        line = line.strip('\n').split(",")
        if(classroom_id == line[0] or classroom_id == int(line[0])) : # as ID can be both integer or string
            data = line
            break
    else : 
        print("classroom not found")
        return None
    
    # calling class method of classroom to build the object
    return_classroom = classroom.existing_classroom(data[0],data[1],int(data[2]))
    
    return return_classroom

def get_all_classrooms() :
    ''' Returns all courses by calling get_course() repeatedly '''

    all_ids = []
    try:
        F = open(data_file_paths["classroom"], mode='r')
    except:
        print("Error in opening file")
        exit()
    
    F.readline()  # To skip the first line as fire line is just information

    for line in F:  # get IDs of all courses present in file
        all_ids.append(line.split(',')[0])

    F.close()

    for i in all_ids : # call get_classroom() repetedly with different ID
        yield get_classroom(i)

  

def get_student(student_id):
	try:
		file = open(data_file_paths["student"], mode = "r")
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
	
	all_ids = []
	try:
		file = open(data_file_paths["student"], mode ="r")
	except:
		print("file not present")
		exit()

	file.readline()

	for line in file:
		all_ids.append(line.split(',')[0])

	file.close()

	for i in all_ids:
		yield get_student(i)

	


def get_course(course_id) :
    ''' Returns a course class object by filling it with details of the id of the course having same ID in the file '''
    data =[]
    try:
        F = open(data_file_paths["course"], mode='r')
    except:
        print("Error in opening file")
        exit()
    
    F.readline()  # To skip the first line as fire line is just information   
    
    for line in F :
        line = line.strip('\n').split(",")
        if(course_id==line[0] or course_id==int(line[0])) : # as ID can be both integer or string
            data = line
            break
    else : 
        print("Course not found")
        return None
    
    # calling class method of course to build the object
    return_course = course.existing_course(data[0],data[1],int(data[2]),data[3],int(data[4]),data[5].split('+'),data[6].split('+'),data[7])
    
    return return_course

def get_all_courses() :
    ''' Returns all courses by calling get_course() repeatedly '''
    
    all_ids = []
    try:
        F = open(data_file_paths["course"], mode='r')
    except:
        print("Error in opening file")
        exit()
    
    F.readline()  # To skip the first line as fire line is just information

    for line in F:  # get IDs of all courses present in file
        all_ids.append(line.split(',')[0])

    F.close()

    for i in all_ids : # call get_course() repetedly with different ID
        yield get_course(i)

    

def get_professor(professor_id) :
    ''' Returns a professor class object by filling it with details of the id of the professor having same ID in the file '''
    data =[]
    try:
        F = open(data_file_paths["professor"], mode='r')
    except:
        print("Error in opening file")
        exit()
    
    F.readline()  # To skip the first line as fire line is just information   
    
    for line in F :
        line = line.strip('\n').split(",")
        if(professor_id==line[0] or professor_id==int(line[0])) : # as ID can be both integer or string
            data = line
            break
    else : 
        print("professor not found")
        return None
    
    # calling class method of professor to build the object

    return_professor = professor.existing_professor(data[0],data[1],data[2],data[3].split('+'))
    
    return return_professor

def get_all_professors() :
    ''' Returns all professors by calling get_professor() repeatedly '''
    
    all_ids = []
    try:
        F = open(data_file_paths["professor"], mode='r')
    except:
        print("Error in opening file")
        exit()
    
    F.readline()  # To skip the first line as fire line is just information

    for line in F:  # get IDs of all professors present in file
        all_ids.append(int(line.split(',')[0]))

    F.close()

    for i in all_ids : # call get_professor() repetedly with different ID
        print(i)
        yield get_professor(i)

            

def clear_professor_file() :
    ''' Truncates the file , then writes the first information line and closes the file '''
    F = open(data_file_paths["professor"], 'w')
    F.write("Id,professor's Name,professpor's email-id,course-list\n")
    F.close()


def clear_course_file() :
    ''' Truncates the file , then writes the first information line and closes the file '''
    F = open(data_file_paths["course"], 'w')
    F.write("000,Name,Max Capacity,Professor,Classes Per Week,Dependent Courses,Dependent Classrooms,Time Duration\n")
    F.close()


def clear_student_file():
	file = open(data_file_paths["student"],"w")
	file.write("Roll No , Name , Email , Batch , list of current courses , list of past courses ")
	file.close()      

def clear_classroom_file() :
    ''' Truncates the file , then writes the first information line and closes the file '''
    F = open(data_file_paths["classroom"], 'w')
    F.write("000,Name,Max Capacity\n")
    F.close()
