import genetic_classes

class genetic_algorithm() :
    def __init__(self,det,no_of_crossover_points,no_of_mutation_points) :
        self.details = det
        self.no_of_crossover_points = no_of_crossover_points
        self.no_of_mutation_points = no_of_mutation_points

    def crossover(self,parent1,parent2) :
        child1 = genetic_classes.chromosome(self.details)
        child2 = genetic_classes.chromosome(self.details)
        limit_of_points = len(parent1.course_times.keys()) - 1
        points = list()
        import random
        while(len(points) < self.no_of_crossover_points) :
            N = random.randint(0,limit_of_points)
            if(N not in points) : points.append(N)

        if limit_of_points not in points : points.append(limit_of_points)        
