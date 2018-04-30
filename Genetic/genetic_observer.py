import genetic_algo

class observer :

    def __init__(self , nps=10) :
        self.g_algo = genetic_algo.genetic_algorithm(5,5)
        self.number_of_parents = nps
        self.parents = list()
        for i in range(self.number_of_parents) :
            chrmo = genetic_algo.genetic_classes.chromosome()
            chrmo.make_course_times(self.g_algo.details)
            chrmo.make_timeline()
            chrmo.calc_fitness(self.g_algo.details)
            self.parents.append(chrmo)
        self.parents.sort(key = lambda x: x.fitness , reverse=True)

        self.print_fitness()

    def generate_timetable(self) :
            count=0
            while self.parents[0].fitness<0 :
                self.perform_crossover()
                self.print_fitness()
                count+=1
                if self.parents[2].fitness - self.parents[self.number_of_parents-2].fitness < 2:
                    print("Mutation Required!")
                    k=0
                    for node in self.parents :
                        print("node" + str(k))
                        node.display_problem_creators(self.g_algo.details)
                    # self.perform_mutation()
                    break

            else :
                self.parents[0].display_timeline("timeline")
                print("Timeline Created \n Iterations Required :" + str(count))
    def print_fitness(self , chrms = None) :
        if chrms==None : chrms = self.parents
        print()
        for i in chrms :
            print(i.fitness , end=" ")

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
            print("EXPECTED NUMBER OF BEST CHILDREN IS MORE THAN SUM OF BOTH PARENTS! \n TERMINATING...")
            exit() 
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
                print("i or j exhausted!!")
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
    obs.generate_timetable()
