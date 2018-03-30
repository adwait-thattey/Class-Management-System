#!/usr/bin/python3


def generate_Classroom_id():
    ''' Generates a new unique Classroom ID by observing all the existing Classroom IDs from the file 'Classroom_data.csv' '''
    try:
        F = open("Classroom_data.csv", mode='r')
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

# def get_Classroom(id):
# 	try:
#         F = open("Classroom_data.csv", mode='r')
#     except:
#         print('Error in opening File')
#         exit()

#     for line in F:
#     	if line[0] == str(id):
#     		print(line)





class Classroom :
    ''' Class that contains details of a particular Classroom '''

    def __init__(self) :
        ''' Defaults all data elements to None '''   
        self.id = None
        self.name = None
        self.max_capacity = None

    @classmethod
    def new_Classroom(cls,name,max_capacity):
        ''' Creates a new Classroom with minimum details. Calls generate_Classroom_id() to generate a new id '''
        obj = Classroom()
        obj.name = str(name)
        obj.max_capacity = int(max_capacity)
        obj.id = str(generate_Classroom_id())
        return obj
    
    @classmethod
    def existing_Classroom(cls,incoming_id,name,max_capacity) :
        ''' Creates a Classroom object with existing details passed as parameters. generate_Classroom_id() IS NOT CALLED '''
        obj = Classroom()
        obj.id = str(incoming_id)
        obj.name = str(name)
        obj.max_capacity = int(max_capacity)
        return obj

    def display_details(self) :
        ''' Displays details of this perticular Classroom '''
        print("Details of Classroom : ")
        print("%-13s : %s"%("Id",self.id))
        print("%-13s : %s"%("Name",self.name))
        print("%-13s : %s" % ("Capacity", self.max_capacity))
        print("\n")

    
    def put_to_file(self) :
        ''' Appends this perticular Classroom to the file 'Classroom_data.csv'. '''
        String = [self.id, self.name, str(self.max_capacity)]
        F = open("Classroom_data.csv", mode='a')
        F.write(",".join(String) + "\n")
        F.close()



