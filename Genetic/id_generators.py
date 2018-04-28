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
	except:
		print("file not found")

	file.readline()
	id=[]
	for line in file:
		if(len(line)<= 0):
			break
		try:
			id.append(int(line.split(',')[0]))
		except:
			continue
	if(len(list)<=0):
		return "001"
	maxm = max(id)
	maxm +=1
	file.close()
	maxm = str(maxm)
	while(len(maxm)<3):
		maxm = '0' + maxm
	return maxm

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
