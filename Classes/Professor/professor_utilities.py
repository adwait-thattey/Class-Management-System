#!/usr/bin/python3

from professor_class import professor

def get_professor(professor_id) :
    ''' Returns a professor class object by filling it with details of the id of the professor having same ID in the file '''
    data =[]
    try:
        F = open("professor_data.csv", mode='r')
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
    all_professors = []
    all_ids = []
    try:
        F = open("professor_data.csv", mode='r')
    except:
        print("Error in opening file")
        exit()
    
    F.readline()  # To skip the first line as fire line is just information

    for line in F:  # get IDs of all professors present in file
        all_ids.append(int(line.split(',')[0]))

    F.close()

    for i in all_ids : # call get_professor() repetedly with different ID
        print(i)
        all_professors.append(get_professor(i))

    return all_professors        

def clear_file() :
    ''' Truncates the file , then writes the first information line and closes the file '''
    F = open("professor_data.csv", 'w')
    F.write("Id,professor's Name,professpor's email-id,course-list\n")
    F.close()


        
