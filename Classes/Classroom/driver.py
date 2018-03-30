''' Driver Code to test the Classroom class and Classroom utilities functions '''

#!/usr/bin/python3

from Classroom_utilities import *

if __name__ == '__main__':
    clear_file()

    C1 = Classroom.new_Classroom("BEC-Lab", 100)
    C1.put_to_file()
    C2 = Classroom.new_Classroom("Computer Lab 1", 130)
    C2.put_to_file()
    C3 = Classroom.new_Classroom("Classroom 1", 200)
    C3.put_to_file()

    AC = get_all_Classrooms()
    
    for i in AC:
        i.display_details()
