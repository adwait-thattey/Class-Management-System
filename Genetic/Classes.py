from id_generators import *


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
        while len(obj.id) < 3:
            obj.id = "0" + obj.id
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
        F = open(data_file_paths["classroom"], mode='a')
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
        obj.email = name + obj.rollno + "@iiits.in"
        obj.batch = batch
        obj.curr_courses = obj.curr_courses.extend(curr_courses)
        obj.past_courses = obj.past_courses.extend(past_courses)
        return obj

    @classmethod
    def existing_student(cls,rollno,name,email,batch,curr_courses,past_courses):
        obj = student()
        obj.rollno = str(rollno)
        while len(obj.rollno) < 3:
            obj.id = "0" + obj.rollno
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
        file = open(data_file_paths["student"],mode = "a")
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
        self.time_duration = None


    @classmethod
    def new_course(cls,name,max_capacity,professor,no_of_classes_per_week,time_duration):
        ''' Creates a new course with minimum details. Calls generate_course_id() to generate a new id '''
        obj = course()
        obj.name = str(name)
        obj.max_capacity = int(max_capacity)
        obj.professor = str(professor)
        obj.no_of_classes_per_week = int(no_of_classes_per_week)
        obj.id = str(generate_course_id())
        obj.dependent_courses = []
        obj.dependent_classrooms = []
        obj.time_duration = time_duration
        return obj
    
    @classmethod
    def existing_course(cls,incoming_id,name,max_capacity,professor,no_of_classes_per_week,D_courses,D_classrooms,time_duration) :
        ''' Creates a course object with existing details passed as parameters. generate_course_id() IS NOT CALLED '''
        obj = course()
        obj.id = str(incoming_id)
        while len(obj.id) < 3 :
            obj.id = "0" + obj.id
        obj.name = str(name)
        obj.max_capacity = int(max_capacity)
        obj.professor = str(professor)
        obj.no_of_classes_per_week = int(no_of_classes_per_week)
        obj.dependent_courses = list(D_courses)
        obj.dependent_classrooms = list(D_classrooms)
        obj.time_duration = time_duration
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
        print("Duration of Classe : ",self.time_duration)
        print()

    
    def put_to_file(self) :
        ''' Appends this perticular course to the file 'course_data.csv'. '''
        String = [self.id, self.name, str(self.max_capacity), self.professor, str(self.no_of_classes_per_week),"+".join(self.dependent_courses),"+".join(self.dependent_classrooms),str(self.time_duration)]
        F = open(data_file_paths["course"], mode='a')
        F.write(",".join(String) + "\n")
        F.close()

class professor :
    ''' Class that contains details of a perticular professor '''

    def __init__(self):
        ''' Defaults all data elements to None '''
        self.id = None
        self.name = None
        self.email = None
        self.courses = None
        
    
    @classmethod
    def new_professor(cls,name) :
        obj = professor()
        obj.name = name
        obj.id = generate_professor_id()
        if(len(obj.id)!=3) :
            print("Number of characters in ID are not equal to 3. Will cause problems with email")
            exit()
        obj.email = name.split()[0].lower() + obj.id + "@iiits.in"
        obj.courses = []
        return obj
        
    @classmethod
    def existing_professor(cls,incoming_id,name,email,courses):
        obj = professor()
        obj.name = str(name)
        obj.id = str(incoming_id)
        while len(obj.id) < 3 :
            obj.id = "0" + obj.id
        obj.email = str(email)
        obj.courses = list(courses)
        return obj
        
    def display_details(self) :
        ''' Displays details of this perticular professor '''
        print("Details of Professor : ")
        print("%-13s : %s"%("Id",self.id))
        print("%-13s : %s"%("Name",self.name))
        print("%-13s : %s" % ("Email", self.email))
        print("List of Courses : ", self.courses)
        print()
        
    def put_to_file(self) :
        ''' Appends this perticular course to the file 'course_data.csv'. '''
        String = [self.id, self.name, str(self.email),"+".join(self.courses)]
        F = open(data_file_paths["professor"], mode='a')
        F.write(",".join(String) + "\n")
        F.close()


class batch :
    ''' Class that contains details of a perticular batch '''

    def __init__(self) :
        ''' Defaults all data elements to None '''   
        self.id = None
        self.name = None
        self.Mandatory_courses = None
        self.Optional_courses = None

    @classmethod
    def new_batch(cls,name,MC=[],OC=[]):
        ''' Creates a new Batch with minimum details. Calls generate_batch_id() to generate a new id '''
        obj = batch()
        obj.name = str(name)
        obj.id = str(generate_batch_id())
        obj.Mandatory_courses = MC
        obj.Optional_courses = OC
        return obj
    
    @classmethod
    def existing_batch(cls,incoming_id,name,MC=[],OC=[]) :
        ''' Creates a Batch object with existing details passed as parameters. generate_course_id() IS NOT CALLED '''
        obj = batch()
        obj.id = str(incoming_id)
        while len(obj.id) < 3:
            obj.id = "0" + obj.id
        obj.name = str(name)
        obj.Mandatory_courses = list(MC)
        obj.Optional_courses = list(OC)
        return obj

    def display_details(self) :
        ''' Displays details of this perticular batch '''
        print("\nDetails of Batch : ")
        print("%-13s : %s"%("Id",self.id))
        print("%-13s : %s"%("Name",self.name))
        print("\nMandatory Courses : " , self.Mandatory_courses)
        print("Optional Courses : ", self.Optional_courses)
        print()

    
    def put_to_file(self) :
        ''' Appends this perticular Batch to the file 'course_data.csv'. '''
        String = [self.id, self.name,"+".join(self.Mandatory_courses),"+".join(self.Optional_courses)]
        F = open(data_file_paths["batch"], mode='a')
        F.write(",".join(String) + "\n")
        F.close()

		

