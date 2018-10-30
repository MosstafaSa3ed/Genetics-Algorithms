from functions import *

#CONSTANTS
POPULATION_SIZE = 300
NUM_OF_GENERATIONS = 700

f=open("d:/FCI/Level 4/first term/Genetic Algorithms/Assignments/1/test/input_example.txt", "r")
# f=open("d:/FCI/Level 4/first term/Genetic Algorithms/Assignments/1/test/small_test.txt", "r")

num_of_test_cases = int(input())
# num_of_test_cases = get_int(f)

for T in range(num_of_test_cases):
    n = int(input())
    #n = get_int(f)

    mxWeight = int(input())
    #mxWeight = get_int(f)
    
    items = []
    for i in range(n):
        weight = int(input())
        benefit = int(input())
       # [weight, benefit] = get_item(f)

        items.append([benefit, weight])
    pop= GeneratePopulation(n, POPULATION_SIZE)
    fit= Fitness(pop,items,mxWeight)
    val=0
    for _ in range( NUM_OF_GENERATIONS):
        pop, fit = select(pop, fit, items, mxWeight)
        pop= mutation(pop)
        # fit= Fitness(pop,items,mxWeight)
        tem,temVal = evaluate(pop,fit)
        if val < temVal:
            val=temVal
            best=tem
    # print(best)
    print("Case: %d  %d " % (T+1, val-1))
    sol=[]
    cnt=0
    for i in best:
        if i == 1:
            sol.append(items[cnt])
        cnt+=1
    # print(len(sol),sol)


