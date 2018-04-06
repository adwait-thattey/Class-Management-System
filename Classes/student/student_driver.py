from student_utilities import *

if __name__ == '__main__':
	clear_file()

	st1 = student.new_student("aaquib","ug1",["ds","cp"],["maths","bec"])
	st1.add_curr_courses("fasdasd")
	st1.add_past_courses("ITWS2")
	st1.remove_curr_courses("fasdfasdffafsdf")
	st1.remove_past_courses("bec")
	st1.put_in_file()
	a= student.new_student("rohit","ug1",["cpp","python"],["iws","its"] )#during this call exisiting student is working
	
	a.put_in_file()
	st1.display()
	get = get_all_students()
#	for i in get:
#		print(i.name)
