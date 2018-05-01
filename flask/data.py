def get_TT_data1():
    F = open('001.csv',mode='r')
    return F.readlines()

def get_TT_data2():
    F = open('002.csv',mode='r')
    return F.readlines()

def get_TT_data3():
    F = open('003.csv',mode='r')
    return F.readlines()

def get_TT_data4():
    F = open('004.csv',mode='r')
    return F.readlines()


def make_TT_Readable():
    temp = get_csv_data()
    arr = [temp.split(',') for i in temp]
    return arr    

def get_course_data():
	F = open('course_data.csv', mode='r')
	return F.readlines()

def check_course():
	course = get_course_data()
	TT_data = make_TT_Readable()

			

# num = get_csv_data()

# print(num)


# print("\n\n")
# for i in num:
#     i.split(',')


# for itera in num:
#     print(itera)
