#!/usr/bin/python3


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
        print("Dependent on Classrooms : ", self.dependent_classrooms)
        print()

    
    def put_to_file(self) :
        ''' Appends this perticular course to the file 'course_data.csv'. '''
        String = [self.id, self.name, str(self.max_capacity), self.professor, str(self.no_of_classes_per_week),"+".join(self.dependent_courses),"+".join(self.dependent_classrooms)]
        F = open("course_data.csv", mode='a')
        F.write(",".join(String) + "\n")
        F.close()



