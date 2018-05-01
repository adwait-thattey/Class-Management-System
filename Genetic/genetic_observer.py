import genetic_algo

class observer :

    def __init__(self , nps=10) :
        self.g_algo = genetic_algo.genetic_algorithm(4,5)
        self.number_of_parents = nps
        self.parents = list()
        for i in range(self.number_of_parents) :
            chrmo = genetic_algo.genetic_classes.chromosome()
            chrmo.make_course_times(self.g_algo.details)
            chrmo.make_timeline()
            chrmo.calc_fitness(self.g_algo.details)
            self.parents.append(chrmo)
        self.parents.sort(key = lambda x: x.fitness , reverse=True)

        print(" Parents Fitness :")
        self.print_fitness()

    def generate_timetable(self) :
            # import time
            # time.sleep(5)
            prev_chk=0
            count=0
            while self.parents[0].fitness<0 :
                self.perform_crossover()
                print("Iteration " + str(count+1))
                self.print_fitness()
                count+=1
                if self.parents[2].fitness - self.parents[self.number_of_parents-2].fitness < 2:
                    if prev_chk==1 :
                        print(1)
                        exit(1)
                        # print("Unable to Make Timetable")
                    # print("Mutation Required!")
                    print("....")
                    print(" Crossover Saturation Reached")
                    print("Attempting to perform Mutation")
                    print ("Attempt " + str(prev_chk+1))
                    print(".........")
                    self.perform_mutation()
                    prev_chk=1
                    print("Mutation Successful")
                    print("Finishing with final Crossovers...")                    

            else :
                self.parents[0].make_timetable(self.g_algo.details)
                print()
                print()
                print("Time-Table Generation Completed Successfully ")
                print("Exiting with code 0...")
                # print("Timeline Created \n Iterations Required :" + str(count))
                return

                    

    def perform_mutation(self) :
        import copy
        mutated_children = list()
        for k in range(self.number_of_parents):
            #for node in self.parents:
            temp_prof = copy.deepcopy(self.parents[k])
            # print("Mutating Batch of " + str(k))
            self.perform_batch_mutation(temp_prof)
            # print("Mutating Prof of" + str(k))
            self.perform_prof_mutation(temp_prof)

            temp_prof.calc_fitness(self.g_algo.details)
            if temp_prof.fitness == 0:
                check = temp_prof.validate_timeline()
                if(check == False):
                    print(1)
                    exit(1)

                temp_prof.display_timeline("mutate_timeline")
                # print("Achieved 0 in mutation")
                mutated_children.append(temp_prof)
                break
                
            else:
                mutated_children.append(temp_prof)

        mutated_children.sort(key = lambda x: x.fitness , reverse=True)
        self.parents.sort(key=lambda x: x.fitness, reverse=True)
        if mutated_children[0].fitness == 0 :
            self.parents[0] = mutated_children[0]
            return
        
        self.parents = list(self.select_best_chromosomes(self.parents, mutated_children))
    
    
    def perform_batch_mutation(self,req_parent) :
        # print("node" + str(k))
        problem_creators = req_parent.return_problem_creators(self.g_algo.details)
        # print(problem_creators[2])
        # print(req_parent.fitness_list)
        prev_list = problem_creators
        prev_count = 0
        while len(list(problem_creators[2].keys())) > 0 :
            taken_key = list(problem_creators[2].keys())[0]
            # print("Selected Key : " , taken_key)
            req_parent = self.g_algo.vacant_slot_mutate(req_parent , taken_key,problem_creators[2][taken_key])
            problem_creators = req_parent.return_problem_creators(self.g_algo.details)
            if prev_list == problem_creators:
                prev_count += 1
                if(prev_count > 5):
                    # print("MUTATION FAILED!")
                    break
            else:
                prev_list = problem_creators
                prev_count = 0
                # self.perform_mutation()
        # print(req_parent.fitness_list)
        problem_creators = req_parent.return_problem_creators(self.g_algo.details)
        # print(problem_creators[2])

    def perform_prof_mutation(self,req_parent) :
        # print("node" + str(k))
        problem_creators = req_parent.return_problem_creators(self.g_algo.details)
        # print(problem_creators[1])
        # print(req_parent.fitness_list)
        prev_list = problem_creators
        prev_count = 0
        while len(list(problem_creators[1].keys())) > 0 :
            taken_key = list(problem_creators[1].keys())[0]
            # print("Selected Key : " , taken_key)
            req_parent = self.g_algo.vacant_slot_mutate(req_parent , taken_key,problem_creators[1][taken_key])
            problem_creators = req_parent.return_problem_creators(self.g_algo.details)
            if prev_list == problem_creators :
                prev_count+=1
                if(prev_count > 5) :
                    # print("MUTATION FAILED!")
                    break
            else :
                prev_list=problem_creators
                prev_count = 0        
                # self.perform_mutation()
        # print(req_parent.fitness_list)
        problem_creators = req_parent.return_problem_creators(self.g_algo.details)
        # print(problem_creators[1])    
    
    def print_fitness(self , chrms = None) :
        if chrms==None : chrms = self.parents
        for i in chrms :
            print(i.fitness , end=" ")

        print()
        print()            

    def perform_crossover(self) :
        children = list()
        children.extend(self.g_algo.crossover(self.parents[0] , self.parents[1]))
        children.extend(self.g_algo.crossover(self.parents[0] , self.parents[2]))
        children.extend(self.g_algo.crossover(self.parents[2] , self.parents[1]))


        
        for i in range(self.number_of_parents//2) :
            children.extend(self.g_algo.crossover(self.parents[i] , self.parents[self.number_of_parents//2 + i]))

        if self.number_of_parents%2 : 
            children.extend(self.g_algo.crossover(self.parents[self.number_of_parents//2] , self.parents[self.number_of_parents - 1]))           

        try :
            for i in range(4) :
                children.extend(self.g_algo.crossover(self.parents[self.number_of_parents//2 + i] , self.parents[self.number_of_parents//2 - i]))
        except IndexError : pass

        # children.extend(self.g_algo.crossover(self.parents[self.number_of_parents-3] , self.parents[self.number_of_parents-2]))
        # children.extend(self.g_algo.crossover(self.parents[self.number_of_parents-3] , self.parents[self.number_of_parents-1]))
        # children.extend(self.g_algo.crossover(self.parents[self.number_of_parents-1] , self.parents[self.number_of_parents-2]))

        # self.print_fitness(children)
        
        children.sort(key = lambda x : x.fitness , reverse=True)

        # self.print_fitness(children)

        self.parents = list(self.select_best_chromosomes(self.parents , children , self.number_of_parents))

        del(children)

        # self.print_fitness()


    def select_best_chromosomes(self , chl1 , chl2 , number=None) :
        if number==None : number = self.number_of_parents
        elif number > len(chl1) + len(chl2) :
            # print("EXPECTED NUMBER OF BEST CHILDREN IS MORE THAN SUM OF BOTH PARENTS! \n TERMINATING...")
            print(1)
            exit(1) 
        i=j=0
        while number>0:
            number-=1
            try :
                if chl1[i].fitness >= chl2[j].fitness :
                    yield chl1[i]
                    i+=1

                else :
                    yield chl2[j]
                    j+=1
            except IndexError :
                # print("i or j exhausted!!")
                break

        if i > len(chl1) :
            while number>0 :
                yield chl2[j]
                j+=1
                number-=1 

        elif j > len(chl2) :
            while number>0 :
                yield chl1[i]
                i+=1
                number-=1

                              


if __name__=="__main__" :
    obs = observer()
    import multiprocessing
    import time
    # Start bar as a process
    p = multiprocessing.Process(target=obs.generate_timetable)
    p.start()

    # Wait for 10 seconds or until process finishes
    p.join(4)

    # If thread is still active
    if p.is_alive():
        # print("running... let's kill it...")
        # Terminate
        p.terminate()
        p.join()
        print(1)
        exit(1)


    print(0)
    exit(0)
