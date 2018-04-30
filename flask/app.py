from flask import Flask,render_template, flash, redirect, url_for, session, request, logging
from data import *
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

num = get_TT_data()
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

F = open("idiot.csv",mode='w')

for i in num:
	F.write(",".join(i) + "\n")
F.close()

F = open("idiot.csv", mode='r')
num = F.readlines()
num = [i.split(',') for i in num]


# for i in range(0,len(num)):
# 	for j in range(0,len(i)):
# 		if str(num[i][j]) == str() 


@app.route('/')
def index():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/data')
def get_data():
	return render_template('data.html',myData = num)

class RegisterForm(Form):
	name = StringField('Name', [validators.Length(min=3,max=20)])
	username = StringField('Username', [validators.Length(min=3,max=20)])
	email = StringField('Email', [validators.Length(min=3,max=20)])
	password = PasswordField('Password',[
			validators.DataRequired(),
			validators.EqualTo('confirm',message='passwords do not match')
		])
	confirm = PasswordField('Confirm Password')

@app.route('/new_login' , methods=['GET','POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		name = form.name.data
		email = form.email.data
		username = form.username.data
		password = sha256_crypt.encrypt(str(form.password.data))

		string = [name,email,username,password]

		F = open("input.csv",mode='a')
		F.write(",".join(string) + "\n")
		F.close()


		flash('You are now connected')
		return redirect(url_for('index'))
	return render_template('new_login.html', form = form)


if __name__ == '__main__':
	app.secret_key='secret'
	app.run(debug=True)