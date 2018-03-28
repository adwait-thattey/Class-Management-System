#!/usr/bin/python3

from Classroom_class import Classroom

def get_Classroom(Classroom_id) :
    ''' Returns a course class object by filling it with details of the id of the course having same ID in the file '''
    data =[]
    try:
        F = open("Classroom_data.csv", mode='r')
    except:
        print("Error in opening file")
        exit()
    
    F.readline()  # To skip the first line as fire line is just information   
    
    for line in F :
        line = line.strip('\n').split(",")
        if(Classroom_id == line[0] or Classroom_id == int(line[0])) : # as ID can be both integer or string
            data = line
            break
    else : 
        print("Classroom not found")
        return None
    
    # calling class method of Classroom to build the object
    return_Classroom = Classroom.existing_Classroom(data[0],data[1],int(data[2]))
    
    return return_Classroom

def get_all_Classrooms() :
    ''' Returns all courses by calling get_course() repeatedly '''
    all_Classrooms = []
    all_ids = []
    try:
        F = open("Classroom_data.csv", mode='r')
    except:
        print("Error in opening file")
        exit()
    
    F.readline()  # To skip the first line as fire line is just information

    for line in F:  # get IDs of all courses present in file
        all_ids.append(line.split(',')[0])

    F.close()

    for i in all_ids : # call get_Classroom() repetedly with different ID
        all_Classrooms.append(get_Classroom(i))

    return all_Classrooms        

def clear_file() :
    ''' Truncates the file , then writes the first information line and closes the file '''
    F = open("Classroom_data.csv", 'w')
    F.write("000,Name,Max Capacity\n")
    F.close()


        
