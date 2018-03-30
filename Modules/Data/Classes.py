def generate_course_id():
    ''' Generates a new unique course ID by observing all the existing course IDs from the file 'course_data.csv' '''
    try:
        F = open("course_data.csv", mode='r')
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
		file = open("class_data.csv",mode='r')
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
        F = open("classroom_data.csv", mode='r')
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

class classroom :
    ''' Class that contains details of a particular classroom '''

    def __init__(self) :
        ''' Defaults all data elements to None '''   
        self.id = None
        self.name = None
        self.max_capacity = None

    @classmethod
    def new_classroom(cls,name,max_capacity):
        ''' Creates a new classroom with minimum details. Calls generate_classroom_id() to generate a new id '''
        obj = classroom()
        obj.name = str(name)
        obj.max_capacity = int(max_capacity)
        obj.id = str(generate_classroom_id())
        return obj
    
    @classmethod
    def existing_classroom(cls,incoming_id,name,max_capacity) :
        ''' Creates a classroom object with existing details passed as parameters. generate_classroom_id() IS NOT CALLED '''
        obj = classroom()
        obj.id = str(incoming_id)
        obj.name = str(name)
        obj.max_capacity = int(max_capacity)
        return obj

    def display_details(self) :
        ''' Displays details of this perticular classroom '''
        print("Details of classroom : ")
        print("%-13s : %s"%("Id",self.id))
        print("%-13s : %s"%("Name",self.name))
        print("%-13s : %s" % ("Capacity", self.max_capacity))
        print("\n")

    
    def put_to_file(self) :
        ''' Appends this perticular classroom to the file 'classroom_data.csv'. '''
        String = [self.id, self.name, str(self.max_capacity)]
        F = open("classroom_data.csv", mode='a')
        F.write(",".join(String) + "\n")
        F.close()

class student:

    def __init__(self):
        self.rollno = None
        self.name = None
        self.email = None
        self.batch = None
        self.curr_courses = None
        self.past_courses = None

    def display(self):
        print("Details of the student : ")
        print("%-13s : %s"%("Roll no",self.rollno))
        print("%-13s : %s"%("Roll no",self.name))
        print("%-13s : %s"%("Roll no",self.email))
        print("%-13s : %s"%("Roll no",self.batch))
        print("\n Current courses : ", self.curr_courses)
        print("\n Past courses : ", self.past_courses)


    @classmethod
    def new_student(cls,name,batch,curr_courses,past_courses):
        obj = student()
        obj.name = name
        obj.rollno = str(get_new_roll())
        obj.email = name + rollno + "@iiits.in"
        obj.batch = batch
        obj.curr_courses = obj.curr_courses.extend(curr_courses)
        obj.past_courses = obj.past_courses.extend(past_courses)
        return obj

    @classmethod
    def existing_student(cls,rollno,name,email,batch,curr_courses,past_courses):
        obj = student()
        obj.rollno = str(rollno)
        obj.name = str(name)
        obj.email = email
        obj.batch = batch
        obj.curr_courses = curr_courses
        obj.past_courses = past_courses
        return obj


    def add_curr_courses(self,course_id):
        if course_id not in self.past_courses and course_id not in self.curr_courses:
            self.curr_courses.append(course_id)


    def add_past_courses(self,course_id):
        if course_id not in self.curr_courses and course_id not in self.past_courses:
            self.past_courses.append(course_id)

    #def remove_curr_courses(self,course_id):
    #   pass:

    #def remove_past_courses(self,course_id):
    #   pass:

    def put_in_file(self):
        Student = [self.rollno,self.name,self.email,self.batch,"+".join(self.curr_courses),"+".join(self.past_courses)]
        file = open("class_data.csv",mode = "a")
        file.write(",".join(Student) + "\n")
        file.close()

class course :
    ''' Class that contains details of a perticular course '''

    def __init__(self) :
        ''' Defaults all data elements to None '''   
        self.id = None
        self.name = None
        self.max_capacity = None
        self.professor = None
        self.no_of_classes_per_week = None
        self.dependent_courses = None
        self.dependent_classrooms = None


    @classmethod
    def new_course(cls,name,max_capacity,professor,no_of_classes_per_week):
        ''' Creates a new course with minimum details. Calls generate_course_id() to generate a new id '''
        obj = course()
        obj.name = str(name)
        obj.max_capacity = int(max_capacity)
        obj.professor = str(professor)
        obj.no_of_classes_per_week = int(no_of_classes_per_week)
        obj.id = str(generate_course_id())
        obj.dependent_courses = []
        obj.dependent_classrooms = []
        return obj
    
    @classmethod
    def existing_course(cls,incoming_id,name,max_capacity,professor,no_of_classes_per_week,D_courses,D_classrooms) :
        ''' Creates a course object with existing details passed as parameters. generate_course_id() IS NOT CALLED '''
        obj = course()
        obj.id = str(incoming_id)
        obj.name = str(name)
        obj.max_capacity = int(max_capacity)
        obj.professor = str(professor)
        obj.no_of_classes_per_week = int(no_of_classes_per_week)
        obj.dependent_courses = list(D_courses)
        obj.dependent_classrooms = list(D_classrooms)
        return obj

    def display_details(self) :
        ''' Displays details of this perticular course '''
        print("Details of Course : ")
        print("%-13s : %s"%("Id",self.id))
        print("%-13s : %s"%("Name",self.name))
        print("%-13s : %s" % ("Professor", self.professor))
        print("%-13s : %s" % ("Capacity", self.max_capacity))
        print("%-13s : %s" % ("Classes/Week", self.no_of_classes_per_week))
        print("\nDependent On Courses : " , self.dependent_courses)
        print("Dependent on classrooms : ", self.dependent_classrooms)
        print()

    
    def put_to_file(self) :
        ''' Appends this perticular course to the file 'course_data.csv'. '''
        String = [self.id, self.name, str(self.max_capacity), self.professor, str(self.no_of_classes_per_week),"+".join(self.dependent_courses),"+".join(self.dependent_classrooms)]
        F = open("course_data.csv", mode='a')
        F.write(",".join(String) + "\n")
        F.close()



