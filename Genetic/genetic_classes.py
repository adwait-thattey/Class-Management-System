import utilities

class details :

    def __init__(self) :
        self.course_details = dict()
        #import constants.file_paths["data_utilities"] :
        
        course_iterator = utilities.get_all_courses()
        I = next(course_iterator)
        while 1:
            D = dict()
            D["professor"] = I.professor
            D["no_of_classes_per_week"] = I.no_of_classes_per_week
            D["time_slots_required"] = int(float(I.time_duration)*2) # As time-duration is in hours but each slot is of 0.5 hour
            # time_slots is the time slots required for each class
            self.course_details[I.id] = D
            try:
                I = next(course_iterator)
            except StopIteration :
                break

    def disp_all_details(self) :
        print("Course Details :")
        for i in self.course_details.keys() :
            print(i , end = " : ")
            print(self.course_details[i])
        


class chromosome :
    ''' A class that contains 1 chromosome for genetic algorithms '''
    def __init__(self , main_data) :
        self.timeline = [None]*20*6 # Each time-slot is of half hour
        self.break_points = [8,9,28,29,48,49,68,69,88,89,108,109]
        self.fitness_list = [0]*2
        self.fitness = sum(self.fitness_list)
        self.course_times = dict()
        self.vacant_slots = list()


        for i in range(len(self.timeline)) :
            if i in self.break_points:
                self.timeline[i] = "Break"
       
        
        for i in main_data.course_details.keys() :
            self.course_times[i] = list()
            no_of_points_to_be_generated = main_data.course_details[i]["no_of_classes_per_week"]
            # print(no_of_points_to_be_generated)
            import random
            while(no_of_points_to_be_generated > 0) :
                N = random.randint(0,len(self.timeline) - 1)
                if(N in self.break_points) : continue #break time. generate again.
                elif N in self.course_times[i] : continue # slot taken by same course. Generate again    
                else :
                    templist = list()
                    for k in range(main_data.course_details[i]["time_slots_required"]) :
                        if N+k in self.break_points or N+k >= len(self.timeline) : #point must not be in breaks and should not be out of index
                            break
                        elif k>0 and (N+k)%(len(self.timeline)/6)==0 : break # New Day has started. Cant schedule.
                        templist.append(N+k)

                    else :
                        self.course_times[i].extend(templist)
                        no_of_points_to_be_generated-=1    

        print(self.course_times)

        for i in self.course_times.keys() :
            for j in self.course_times[i] :
                try : self.timeline[j].append(i) # Exception will occur if it is not a list
                except AttributeError: 
                    self.timeline[j] = list()
                    self.timeline[j].append(i)

        for i in range(len(self.timeline)) :
            if self.timeline[i]==None : self.vacant_slots.append(i) 


    def display_course_times(self) :
        print("-----\n Course Times \n")
        for i in self.course_times.keys() :
            print(i , end=" ")
            print(self.course_times[i])
        print("----------")    
    def display_timeline(self , name="timeline") :
        # TimeLine is always written to a CSV File for easier analysis
        F = open(name+".csv" , mode="w")
        S = ""
        for i in range(len(self.timeline)) :
            Stemp=""    
            if(self.timeline[i]=="Break") : Stemp = "Break"
            elif(self.timeline[i]!=None) :
                for j in self.timeline[i] :
                    Stemp+= j + "+"

            if(i != 0 and i % 19 == 0):
                F.write(S + "\n")
                S = ""
            
            S+= Stemp + ","

        F.close()        

    def display_details(self) :
        print("------\n Details\n")
        print("break points : " , self.break_points)
        print("fitness : " , self.fitness)
        print("no of vacant slots :" , self.vacant_slots)
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
C.disp_all_details()
Chr = chromosome(C)
Chr.display_details()
Chr.display_course_times()
Chr.display_timeline("timeline1")
