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
	#	pass:

	#def remove_past_courses(self,course_id):
	#	pass:

	def put_in_file(self):
		Student = [self.rollno,self.name,self.email,self.batch,"+".join(self.curr_courses),"+".join(self.past_courses)]
		file = open("class_data.csv",mode = "a")
		file.write(",".join(Student) + "\n")
		file.close()

