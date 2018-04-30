''' Driver Code to test the course class and course utilities functions '''

#!/usr/bin/python3

from utilities import *

if __name__ == '__main__':
    clear_course_file()

#    C1 = course.new_course("BEC", 100, "Paul Braniard", 3)
#    C1.put_to_file()
#    C2 = course.new_course("ITWS", 200, "Gowhri Subramanian", 5)
#    C2.put_to_file()
#    C3 = course.new_course("BEC-LAB", 200, "Don't Care", 1)
#    C3.dependent_courses.append('001')
#    C3.dependent_classrooms.append('306')
#    C3.put_to_file()
#    C4 = course.existing_course('012', 'Comms-2', 25, "Divya Raj", 3, ['001', '003'], ['103'])
#    C4.put_to_file()
    #print(C1.id, C2.id, C3.id, C4.id)

#    AC = get_all_courses()
#    V = next(AC)    
#    while AC:
#        V.display_details()
#        V = next(AC)

    # I = get_all_batches()
    # while 1:
    #     next(I).display_details()

    S1 = student.new_student("Adwait" , "001" , ["001","002"] , [])
    S1.display()
    S1.put_in_file()
    S2 = student.new_student("Adwait", "001", ["001", "002"], [])
    S2.display()
    S2.put_in_file()