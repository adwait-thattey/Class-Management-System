import genetic_classes

class genetic_algorithm() :
    def __init__(self,no_of_crossover_points,no_of_mutation_points) :
        self.details = genetic_classes.details()
        self.no_of_crossover_points = no_of_crossover_points
        self.no_of_mutation_points = no_of_mutation_points

    def crossover(self,parent1,parent2) :
        child1 = genetic_classes.chromosome()
        child2 = genetic_classes.chromosome()
        limit_of_points = len(parent1.course_times.keys()) - 1
        points = list()
        import random
        while(len(points) < self.no_of_crossover_points) :
            N = random.randint(0,limit_of_points)
            if(N not in points) : points.append(N)

        if limit_of_points not in points : points.append(limit_of_points)        
        points.sort()
        # print(points)
        keys = list(parent1.course_times.keys())
        keys.sort()
        # print(keys)
        start = 0
        for i in range(len(points)) :
            if(i%2==0) :
                while(start<=points[i]) :
                    child1.course_times[keys[start]] = parent1.course_times[keys[start]]
                    child2.course_times[keys[start]] = parent2.course_times[keys[start]]
                    start+=1
            else :
                while(start<=points[i]) :
                    child1.course_times[keys[start]] = parent2.course_times[keys[start]]
                    child2.course_times[keys[start]] = parent1.course_times[keys[start]]
                    start+=1

        child1.make_timeline()
        child1.calc_fitness(self.details)

        child2.make_timeline()
        child2.calc_fitness(self.details)

        return (child1,child2)            
                        

            
        
        
        


if __name__=="__main__" :
    algo = genetic_algorithm(5,5)
    # det = genetic_classes.details()
    # P1 = genetic_classes.chromosome()
    # P2 = genetic_classes.chromosome()
    # P1.make_course_times(det)
    # P1.make_timeline()
    # P1.calc_fitness(det)
    # P1.display_details()

    # P2.make_course_times(det)
    # P2.make_timeline()
    # P2.calc_fitness(det)
    # P2.display_details()

    # P1.display_course_times()
    # P2.display_course_times()
    
    Parents = list()
    for i in range(10):
        Chr = genetic_classes.chromosome()
        Chr.make_course_times(algo.details)
        Chr.make_timeline()
        Chr.calc_fitness(algo.details)
        Parents.append(Chr)

    Parents.sort(key = lambda x: x.fitness , reverse=True)
    for i in range(len(Parents)):
        print(Parents[i].fitness, end=" ")
    print()
    
    children = list()
    
    for i in range(5) :
        ch = algo.crossover(Parents[i],Parents[5+i])
        children.append(ch[0])
        children.append(ch[1])

    for i in  range(2) :
        ch = algo.crossover(Parents[i], Parents[2+i])
        children.append(ch[0])
        children.append(ch[1])

    children.sort(key = lambda x: x.fitness , reverse=True)
    for i in range(len(children)) :
        print(children[i].fitness , end=" ")

    print()
    newParents = list()
    i=j=k=0
    while(k<10) :
        if(Parents[i].fitness >= children[j].fitness) :
            newParents.append(Parents[i])
            i+=1
            k+=1
        else :
            newParents.append(children[j])
            j+=1
            k+=1

    # for i in range(len(newParents)):
        # print(newParents[i].fitness, end=" ")

    Parents = newParents

    children = list()

    # Parents.sort(key=lambda x: x.fitness, reverse=True)
    for i in range(len(Parents)):
        print(Parents[i].fitness, end=" ")
    print()

    for i in range(5):
        ch = algo.crossover(Parents[i], Parents[5+i])
        children.append(ch[0])
        children.append(ch[1])

    for i in range(2):
        ch = algo.crossover(Parents[i], Parents[2+i])
        children.append(ch[0])
        children.append(ch[1])

    children.sort(key=lambda x: x.fitness, reverse=True)
    for i in range(len(children)):
        print(children[i].fitness, end=" ")

    if(children[0].fitness==0) : children[0].display_timeline("childTT")
    if Parents[0].fitness==0 : Parents[0].display_timeline("parentTT")
        

