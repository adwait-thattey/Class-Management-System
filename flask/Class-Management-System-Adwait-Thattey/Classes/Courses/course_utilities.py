#!/usr/bin/python3

from course_class import course

def get_course(course_id) :
    ''' Returns a course class object by filling it with details of the id of the course having same ID in the file '''
    data =[]
    try:
        F = open("course_data.csv", mode='r')
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
    return_course = course.existing_course(data[0],data[1],int(data[2]),data[3],int(data[4]),data[5].split('+'),data[6].split('+'))
    
    return return_course

def get_all_courses() :
    ''' Returns all courses by calling get_course() repeatedly '''
    all_courses = []
    all_ids = []
    try:
        F = open("course_data.csv", mode='r')
    except:
        print("Error in opening file")
        exit()
    
    F.readline()  # To skip the first line as fire line is just information

    for line in F:  # get IDs of all courses present in file
        all_ids.append(line.split(',')[0])

    F.close()

    for i in all_ids : # call get_course() repetedly with different ID
        all_courses.append(get_course(i))

    return all_courses        

def clear_file() :
    ''' Truncates the file , then writes the first information line and closes the file '''
    F = open("course_data.csv", 'w')
    F.write("000,Name,Max Capacity,Professor,Classes Per Week,Dependent Courses,Dependent Classrooms\n")
    F.close()


        
