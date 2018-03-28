#!/usr/bin/python3

def generate_professor_id():
    ''' Generates a new unique professor ID by observing all the existing professor IDs from the file 'professor_data.csv' '''
    try:
        F = open("professor_data.csv", mode='r')
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
			F = open("professor_data.csv", mode='a')
			F.write(",".join(String) + "\n")
			F.close()
		




