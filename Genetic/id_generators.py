data_file_paths = {"course":"../Modules/data/course_data.csv" , "student":"../Modules/data/student_data.csv" , "professor":"../Modules/data/professor_data.csv" , "classroom" : "../Modules/data/classroom_data.csv" , "batch":"../Modules/data/batch_data.csv"}


def generate_course_id():
    ''' Generates a new unique course ID by observing all the existing course IDs from the file 'course_data.csv' '''
    try:
        F = open(data_file_paths["course"], mode='r')
    except:
        print('Error in opening File')
        exit()
    cur_id = 0
    ret_id = 0
    F.readline()
    for line in F:
        # print(line)
        if(len(line) <= 0):
            break
        try :   line = int(line.split(',')[0])
        except : continue
        if(line-cur_id != 1):
            ret_id = cur_id+1
            break
        cur_id += 1
    else:
        ret_id = cur_id + 1
    ret_id = str(ret_id)
    F.close()
    while(len(ret_id) < 3):
        ret_id = '0' + ret_id

    return ret_id

def get_new_roll():
    try :
        file = open(data_file_paths["student"],mode='r')
        #print("file is found")
    except:
        print("file not found \n creating new file")
        file = open(data_file_paths["student"],"w")
        file.write("Roll No , Name , Email , Batch , list of current courses , list of past courses ")
        file.close()
        return "001"
	
    curr_id = 0
    ret_id = 0
    file.readline()
    id=[]
    for line in file:
        #print(line)
        if(len(line)<=0):
            break;
        try: 
            roll = int (line.split(',')[0])
            #print(roll)
        except : continue
        if (roll - curr_id != 1):
            ret_id = curr_id + 1
            break
        curr_id+= 1
    else:
        ret_id = curr_id + 1
    ret_id = str(ret_id)
    file.close()
    while(len(ret_id)<3):
        ret_id = '0' + ret_id
    #print(ret_id)
    return ret_id

def generate_classroom_id():
    ''' Generates a new unique classroom ID by observing all the existing classroom IDs from the file 'classroom_data.csv' '''
    try:
        F = open(data_file_paths["classroom"], mode='r')
    except:
        print('Error in opening File')
        exit()
    cur_id = 0
    ret_id = 0
    F.readline()
    for line in F:
        # print(line)
        if(len(line) <= 0):
            break
        try :   line = int(line.split(',')[0])
        except : continue
        if(line-cur_id != 1):
            ret_id = cur_id+1
            break
        cur_id += 1
    else:
        ret_id = cur_id + 1
    ret_id = str(ret_id)
    F.close()
    while(len(ret_id) < 3):
        ret_id = '0' + ret_id

    return ret_id


def generate_professor_id():
    ''' Generates a new unique professor ID by observing all the existing professor IDs from the file 'professor_data.csv' '''
    try:
        F = open(data_file_paths["professor"], mode='r')
    except:
        print('Error in opening File')
        exit()
    cur_id = 0
    ret_id = 0
    F.readline()
    for line in F:
        # print(line)
        if(len(line) <= 0):
            break
        try :   line = int(line.split(',')[0])
        except : continue
        if(line-cur_id != 1):
            ret_id = cur_id+1
            break
        cur_id += 1
    else:
        ret_id = cur_id + 1
    ret_id = str(ret_id)
    F.close()
    while(len(ret_id) < 3):
        ret_id = '0' + ret_id

    return ret_id


def generate_batch_id():
    ''' Generates a new unique batch ID by observing all the existing course IDs from the file 'course_data.csv' '''
    try:
        F = open(data_file_paths["batch"], mode='r')
    except:
        print('Error in opening File')
        exit()
    cur_id = 0
    ret_id = 0
    F.readline()
    for line in F:
        # print(line)
        if(len(line) <= 0):
            break
        try :   line = int(line.split(',')[0])
        except : continue
        if(line-cur_id != 1):
            ret_id = cur_id+1
            break
        cur_id += 1
    else:
        ret_id = cur_id + 1
    ret_id = str(ret_id)
    F.close()
    while(len(ret_id) < 3):
        ret_id = '0' + ret_id

    return ret_id    
