import utilities

class details :

    def __init__(self) :
        self.course_details = dict()
        #import constants.file_paths["data_utilities"] :
        
        course_iterator = utilities.get_all_courses()
        I = next(course_iterator)
        while 1:
            L = list()
            L.append(I.professor)
            L.append(I.no_of_classes_per_week)
            self.course_details[I.id] = list(L)
            try:
                I = next(course_iterator)
            except StopIteration :
                break

        print(self.course_details)            


class chromosome :
    ''' A class that contains 1 chromosome for genetic algorithms '''
    def __init__(self , main_data) :
        self.timeline = [None]*10*6
        self.break_points = [4, 14, 24, 34, 44, 54]
        self.fitness_list = [0]*2
        self.fitness = sum(self.fitness_list)
        self.course_times = dict()
        self.number_of_vacant_slots = 0


        for i in range(len(self.timeline)) :
            if i in self.break_points:
                self.timeline[i] = "Break"
       
        
        for i in main_data.course_details.keys() :
            self.course_times[i] = list()
            no_of_points_to_be_generated = main_data.course_details[i][1]
            print(no_of_points_to_be_generated)
            import random
            while(no_of_points_to_be_generated > 0) :
                N = random.randint(0,len(self.timeline) - 1)
                if(N in self.break_points) : continue #break time. generate again.
                if N in self.course_times[i] : continue # slot taken by same course. Generate again    
                else :
                    self.course_times[i].append(N)
                    no_of_points_to_be_generated-=1    

        print(self.course_times);

        for i in self.course_times.keys() :
            for j in self.course_times[i] :
                try : self.timeline[j].append(i) # Exception will occur if it is not a list
                except AttributeError: 
                    self.timeline[j] = list()
                    self.timeline[j].append(i)

        for i in self.timeline :
            if i==None : self.number_of_vacant_slots+=1 


    def display_course_times(self) :
        print("-----\n Course Times \n")
        for i in self.course_times.keys() :
            print(i , end=" ")
            print(self.course_times[i])
        print("----------")    
    def display_timeline(self) :
        for i in range(len(self.timeline)) :
            if(i%10==0) : print()
            print(self.timeline[i] , end="  ")

    def display_details(self) :
        print("------\n Details\n")
        print("break points : " , self.break_points)
        print("fitness : " , self.fitness)
        print("no of vacant slots :" , self.number_of_vacant_slots)
        print("------")


    

class fitness_functions :
    def __init__(self , det , chrmo) :
        self.chrmo = chrmo
        self.det = det

    def check_professor_clash(self) :
        for i in self.chrmo.timeline :
            if(i==None) : continue
            if(len(i)<=1) : continue
            cur_profs = list()
            for j in i :
                if(self.det.course_details[j][0] in cur_profs) : return False
                else : cur_profs.append(self.det.course_details[j][0])

        return True            




C = details()
Chr = chromosome(C)
Chr.display_details()
Chr.display_course_times()
Chr.display_timeline()
