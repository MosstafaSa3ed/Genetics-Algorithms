import random

def evaluate(pop,fitness):
    mx=max(fitness)
    ind=fitness.index(mx)
    return pop[ind],mx


def Fitness(population , inputt, mxWight):
    fitness=[]
    i=0
    j=0
    weight=0
    value=0
    for x in population:
        for y in x:
            if(population[i][j]==1):
                weight=weight+inputt[j][1]
                value=value+inputt[j][0]
            j=j+1
        # f1=[value,weight]
        #fitness.append(f1)
        if weight > mxWight:
            value=0
        fitness.append(value + 1)
        i=i+1
        j=0
        weight=0
        value=0
    return fitness

def mutation(population):
    i=0
    j=0
    pm=random.uniform(0.01,0.1)
    for x in population:
        for y in x:
           r=random.uniform(0,1)
           if (r<pm):
               if(population[i][j]==1):
                  population[i][j]=0
               else:
                   population[i][j]=1
           j=j+1
        j=0
        i=i+1
    return population

def GeneratePopulation(x, y = 0):
    if y == 0:
        y = int(x*x)
    # y=(int)(x*x)
    arr = []
    for _ in range(0,y):
        crom = []
        for _ in range(0,x,1):
            bit=random.uniform(0,1)
            if bit > 0.5:
                crom.append(1)
            else:
                crom.append(0)
        arr.append(crom)
    return arr

def select(generation, fitness, items,mxWight):
    new_generation = []
    com_fitness = []
    com_fitness.append(fitness[0])
    population_size = len(fitness)
    for i in range(1,len(fitness)):
        com_fitness.append(com_fitness[i-1] + fitness[i])
    new_fitness = []
    while len(new_generation) < population_size:
        r1 = random.randint(0, com_fitness[-1])
        first_parent_index = get_chromosome_index(r1, com_fitness)

        r2 = random.randint(0, com_fitness[-1])
        second_parent_index = get_chromosome_index(r2, com_fitness)
        
        while first_parent_index == second_parent_index:
            r2 = random.randint(0, com_fitness[-1])
            second_parent_index = get_chromosome_index(r2, com_fitness)
        temp_fit = [fitness[first_parent_index], fitness[second_parent_index]]
        first_parent = generation[first_parent_index]
        second_parent = generation[second_parent_index]
        temp_chromosomes = [first_parent, second_parent] + list(crossover(first_parent[:], second_parent[:]))

        chromosomes, fit = best_chromosomes(temp_chromosomes, temp_fit, items,mxWight)
        new_generation += chromosomes
        new_fitness += fit
    return new_generation, new_fitness

def get_chromosome_index(num, arr):
    for i in range(len(arr)):
        if arr[i] >= num:
            return i

def crossover(c1, c2):
    # Uniform Crossover
    for i in range(len(c1)):
        if random.random() < 0.5:
            c1[i], c2[i] = c2[i], c1[i]
    return c1, c2

def best_chromosomes(chromosomes, fit, items,mxWight):
    #choose best 2 of the children and parents
#    fitness = [fit(i) for i in chromosomes]
    fitness = fit + Fitness(chromosomes[2:], items,mxWight)
    min_index = fitness.index(min(fitness))
    del chromosomes[min_index], fitness[min_index]
    min_index = fitness.index(min(fitness))
    del chromosomes[min_index], fitness[min_index]
    return chromosomes, fitness


def get_int(file):
    temp = file.readline()
    while temp == "" or temp == '\n':
        temp = file.readline()
    return int(temp)

def get_item(file):
    temp = file.readline()
    while temp == '\n' or "":
        temp = file.readline()
    temp = [int(i) for i in temp.split()]
    return temp