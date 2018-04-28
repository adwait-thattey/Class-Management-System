import utilities

class details :

    def __init__(self) :
        self.course_details = dict()
        self.batch_details = dict()
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

        # self.disp_all_details()
        batch_iterator = utilities.get_all_batches()
        I = next(batch_iterator)

        while 1:
            self.batch_details[I.id] = list()
            self.batch_details[I.id].extend(I.Mandatory_courses)
            # self.batch_details[I.id].extend(I.Optional_courses)

            for j in I.Mandatory_courses :
                self.course_details[j]["batch"] = I.id

            try:
                I = next(batch_iterator)
            except StopIteration :
                break    



    def disp_all_details(self) :
        print("Course Details :")
        for i in self.course_details.keys() :
            print(i , end = " : ")
            print(self.course_details[i])

        print("Batch Details :")
        for i in self.batch_details.keys():
            print(i, end=" : ")
            print(self.batch_details[i])
        


class chromosome :
    ''' A class that contains 1 chromosome for genetic algorithms '''
    def __init__(self) :
        self.timeline = [None]*20*6 # Each time-slot is of half hour
        self.break_points = [8,9,28,29,48,49,68,69,88,89,108,109]
        self.fitness_list = [0]*3
        self.fitness = sum(self.fitness_list)
        self.course_times = dict()
        self.vacant_slots = list()


        for i in range(len(self.timeline)) :
            if i in self.break_points:
                self.timeline[i] = "Break"


    def make_course_times(self,main_data) :
        for i in main_data.course_details.keys() :
            self.course_times[i] = list()
            no_of_points_to_be_generated = main_data.course_details[i]["no_of_classes_per_week"]
            # print(no_of_points_to_be_generated)
            import random
            #######
# The working logic of the following loop is explained here. Read carefully
#The outermost loop (loop 1) will run until required number of start points for the corrosponding course have been generated
# Then 'N'  , a random point is being generated. Now we will check whether 'N' is a valid point
# main_data.course_details[i]["time_slots_required"] stores the CONSECUTIVE TIME-SLOTS that need to be reserved starting from N , as the class runs for the given duration
#Thus in Loop2 k takes the values from  N till N+(number of slots)
# For Ex : if no of slots = 4 and N = 52 , the k will take the values 52,53,54,55
#Now in loop2 we will check whether any of these values already exist in the course to ensure that the same course is not scheduled twice at the same position
# Loop 2 will break if the above condition doesn't get satisfied. Then the else part with contains the rest the loops will not get executed and we will go into next iteration of the loop1
#If the condition satisfies , then we reserve all the time-slots for the course by inserting in  course_times[i] 
            #Loop1
            while(no_of_points_to_be_generated > 0) :
                N = random.randint(0,len(self.timeline) - 1)
                #loop 2
                for k in range(N, N+main_data.course_details[i]["time_slots_required"]) :
                    if k in self.course_times[i] : break
                    if k in self.break_points : break
                    elif k >= len(self.timeline) : break
                    elif k > N and (k % (len(self.timeline)/6)) == 0 : break
                else :
                    self.course_times[i].extend(list(range(N,N+main_data.course_details[i]["time_slots_required"])))
                    no_of_points_to_be_generated -= 1


    def make_timeline(self) :
        # Now make the timeline based on course times
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
        Days=["Mon","Tue","Wed","Thurs","Fri","Sat"]
        dayi=0
        F = open(name+".csv" , mode="w")
        F.write(
            "Days ,8.00-8.30,8.30-9.00,9.00-9.30,9.30-10.00,10.00-10.30,10.30-11.00,11.00-11.30,11.30-12.00,12.00-12.30,12.30-1.00,1.00-1.30,1.30-2.00,2.00-2.30,2.30-3.00,3.00-3.30,3.30-4.00,4.00-4.30,4.30-5.00,5.00-5.30,5.30-6.00,\n")
        S = ""
        for i in range(len(self.timeline)) :
            if(i!=0 and i%20==0) : 
                F.write(Days[dayi] + "," + S + "\n")
                dayi+=1
                S = ""
            Stemp=""    
            if(self.timeline[i]=="Break") : Stemp = "Break"
            elif(self.timeline[i]!=None) :
                for j in self.timeline[i] :
                    Stemp+= j + "+"
            
            S+= Stemp + ","

        F.write(Days[dayi] + "," + S + "\n")
                
        F.close()        

    def display_details(self) :
        print("------\n Details\n")
        print("break points : " , self.break_points)
        print("fitness : " , self.fitness , self.fitness_list)
        print("no of vacant slots :" , self.vacant_slots)
        print("------")

    def calc_fitness(self,det) :
        F = fitness_functions(det,self)
        # self.fitness_list[0] = F.check_same_course()
        # self.fitness_list[1] = F.check_professor_clash()
        # self.fitness_list[2] = F.check_batch_clash()
        
        self.fitness_list = F.check_total_fitness()
        # print(self.fitness_list)
        self.fitness = sum(self.fitness_list)




    

class fitness_functions :
    def __init__(self , det , chrmo) :
        self.chrmo = chrmo
        self.det = det

    def check_total_fitness(self) :
        fit = [0]*len(self.chrmo.fitness_list)
        fit[0] = self.check_same_course()
        fit[1] = self.check_professor_clash()
        fit[2] = self.check_batch_clash()

        # print(fit)
        return fit
        

    def check_same_course(self) :
        fitness = 0
        for i in self.chrmo.timeline :
            if(i==None) : continue
            elif(i=="Break") : continue    
            elif(len(i)<=1) : continue
            for j in i :
                if(i.count(j) > 1) : 
                    fitness-=1
                    break

        return fitness                

    def check_professor_clash(self) :
        fitness = 0
        for i in self.chrmo.timeline :
            if(i==None) : continue
            elif(i=="Break") : continue    
            elif(len(i)<=1) : continue
            cur_profs = list()
            for j in i :
                if(self.det.course_details[j]["professor"] in cur_profs) : 
                    # print("clash at " + str(self.chrmo.timeline.index(i)))
                    fitness-=1
                    break
                else : cur_profs.append(self.det.course_details[j]["professor"])

        return fitness  

    def check_batch_clash(self) :
        fitness = 0
        for i in self.chrmo.timeline :
            if(i==None) : continue
            elif(i=="Break") : continue    
            elif(len(i)<=1) : continue
            for j in i :
                B = self.det.course_details[j]["batch"]
                for k in i :
                    if(k!=j and k in self.det.batch_details[B]) : 
                        # print("clash at " + str(self.chrmo.timeline.index(i)))
                        fitness-=1
                        break

        return fitness


if __name__=="__main__" :
    Dt = details()
    #Dt.disp_all_details()
    Chr = chromosome()
    Chr.make_course_times(Dt)
    Chr.make_timeline()
    Chr.calc_fitness(Dt)
    Chr.display_timeline("timeline1")
    # Fittness = fitness_functions(Dt,Chr)
    # print(Fittness.check_same_course())
    # print(Fittness.check_professor_clash())
    # print(Fittness.check_batch_clash())
    
    Chr.display_details()