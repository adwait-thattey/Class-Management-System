from flask import Flask,render_template, flash, redirect, url_for, session, request, logging
from data import *
#from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

passwordI = '$5$rounds=535000$XQ9B0qEgtz//und.$hLC1UONM9fqAYHa2hlDoL4o0HreH/Tru1wxnFn5XTc2'

app = Flask(__name__)

num = get_TT_data1()
num = [i.split(',') for i in num]
course_arr = []

course = get_course_data()
for line in course:
	course_arr.append(line.split()[0])
course_arr = [i.split(',') for i in course_arr]


for i in range(1,len(num)):
	for j in range(1,len(num[i])):
		for k in course_arr:
			if (str(k[0]) in str(num[i][j])):
				num[i][j] = k[1]

F = open("final_ug1.csv",mode='w')

for i in num:
	F.write(",".join(i) + "\n")
F.close()



num2 = get_TT_data2()
num2 = [i.split(',') for i in num2]
course_arr = []

course = get_course_data()
for line in course:
	course_arr.append(line.split()[0])
course_arr = [i.split(',') for i in course_arr]


for i in range(1,len(num2)):
	for j in range(1,len(num2[i])):
		for k in course_arr:
			if (str(k[0]) in str(num2[i][j])):
				num2[i][j] = str(k[1])

F = open("final_ug2.csv",mode='w')

for i in num2:
	F.write(",".join(i) + "\n")
F.close()


num3 = get_TT_data3()
num3 = [i.split(',') for i in num3]
course_arr = []

course = get_course_data()
for line in course:
	course_arr.append(line.split()[0])
course_arr = [i.split(',') for i in course_arr]


for i in range(1,len(num3)):
	for j in range(1,len(num3[i])):
		for k in course_arr:
			if (str(k[0]) in str(num3[i][j])):
				num3[i][j] = k[1]

F = open("final_ug3.csv",mode='w')

for i in num3:
	F.write(",".join(i) + "\n")
F.close()


num4 = get_TT_data4()
num4 = [i.split(',') for i in num4]
course_arr = []

course = get_course_data()
for line in course:
	course_arr.append(line.split()[0])
course_arr = [i.split(',') for i in course_arr]


for i in range(1,len(num4)):
	for j in range(1,len(num4[i])):
		for k in course_arr:
			if (str(k[0]) in str(num4[i][j])):
				num4[i][j] = k[1]

F = open("final_ug4.csv",mode='w')

for i in num4:
	F.write(",".join(i) + "\n")
F.close()






F = open("final_ug1.csv", mode='r')
num = F.readlines()
num = [i.split(',') for i in num]

student_list = open("student_data.csv",mode='r')
student_list = [i.split(',') for i in student_list]

professor_list = open("professor_data.csv",mode='r')
professor_list = [i.split(',') for i in professor_list]


def get_studentI(student_id):
	try:
		file = open('student_data.csv', mode = "r")
	except:
		print("file is not present")
		exit()

	file.readline()

	for line in file:
		line = line.strip('\n').split(",")
		if(student_id == line[0] or student_id == int(line[0])):
			data = line
			return data

	else :
		print("student not found")
		return None

def get_profI(professor_id):
	try:
		file = open('professor_data.csv', mode = "r")
	except:
		print("file is not present")
		exit()

	file.readline()

	for line in file:
		line = line.strip('\n').split(",")
		if(professor_id == line[0] or professor_id == int(line[0])):
			data = line
			return data

	else :
		print("student not found")
		return None

	

# for i in range(0,len(num)):
# 	for j in range(0,len(i)):
# 		if str(num[i][j]) == str() 




'''login page'''

@app.route('/',methods=['GET','POST'])
def index():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']



		if (email == 'iiits-admin' and sha256_crypt.verify(password,passwordI)):

			return render_template('home.html')


	return render_template('form.html')

@app.route('/data')
def timetable():
	return render_template('data.html')

@app.route('/data1')
def batch_TT_1():
	return render_template('data_list.html', myDataUG1=num)

@app.route('/data2')
def batch_TT_2():
	return render_template('data_list2.html',myDataUG2=num2)

@app.route('/data3')
def batch_TT_3():
	return render_template('data_list3.html',myDataUG3=num3)

@app.route('/data4')
def batch_TT_4():
	return render_template('data_list4.html',myDataUG4=num4)

@app.route('/new_student')
def new_student():
	return render_template('new_login.html')



@app.route('/student_list')
def student_data():
	return render_template('student_list.html', student_data = student_list)

@app.route('/unique_student/<string:id>/')
def unique_student(id):
	stud_obj = get_studentI(id)
	return render_template('unique_student.html', id=stud_obj)



@app.route('/professor_list')
def professor_data():
	return render_template('professor_list.html', professor_data = professor_list)

@app.route('/unique_professor/<string:id>/')
def unique_professor(id):
	prof_obj = get_profI(id)
	return render_template('unique_professor.html', id2 = prof_obj)




if __name__ == '__main__':
	app.secret_key='secret'
	app.run(debug=True)