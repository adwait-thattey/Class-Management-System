from professor_class import *

if __name__ == "__main__" :
    F = open("professor_data.csv", 'w')
    F.write("000,name,email,Courses\n")
    F.close()

    P = professor.new_professor("Shehasis Mukharjee")
    P.display_details()
    P.put_to_file()
    P2 = professor.new_professor("Divya Raj")
    P2.display_details()
    P2.put_to_file()

    P3 = professor.existing_professor('013', "Raja Vara Prasad", 'raja.vara@iiits.in', ['013', '026', '011'])
    P3.put_to_file()
    P3.display_details()
