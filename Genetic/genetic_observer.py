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

    def print_parents(self) :
        print()
        for i in self.parents :
            print(i.fitness , end=" ")

        print()            

    def perform_crossover(self) :
        children = list()
        children.extend(self.g_algo.crossover(self.parents[0] , self.parents[1]))
        children.extend(self.g_algo.crossover(self.parents[0] , self.parents[2]))
        children.extend(self.g_algo.crossover(self.parents[2] , self.parents[1]))
        # children.extend(self.g_algo.crossover(self.parents[i] , self.parents[self.number_of_parents//2 + i]))


    def select_best_chromosomes(self , chl1 , chl2 , number=None) :
        if number==None : number = self.number_of_parents

        i=j=0
        while number>0 :
            number-=1
            if chl1[i].fitness >= chl2.fitness[j] :
                yield chl1[i]
                i+=1

            else :
                yield chl2[j]
                j+=1    
