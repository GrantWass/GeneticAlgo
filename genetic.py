import matplotlib.pyplot as plt
import numpy as np
import random 

# Target series of coordinates
target_sequence = [-2,0, -1,2, 0,1, 1,2, 2,0, 0,-3, -2,0]  

# Genetic algorithm parameters
population = []  # Population of solutions (2D list of 100 1D solutions)
parents = []  # Top 50 best solutions 
population_fits = []  # Fitness values of each solution
N = 100  # Number of solutions in the population
mutate_rate = 0.02  # Probability of mutation occurring
length = len(target_sequence)  # Length of a sequence of coordinates/solution


"""
Calculate the fitness of each solution in the population.
Fitness should measure how close each solution is to the target (problem).
Use the sum of squared differences between each coordinate in the solution and the target.
Store the fitness values in 'population_fits'.
"""
def fit_function():
    # TODO: Implement fitness function
    pass  


"""
Generate the initial population of N random solutions.
Each solution should be a list of 'length' numbers ranging from -10 to 10.
"""
def Gen0():
    # TODO: Implement initialization of generation 0
    pass 


"""
Remove the worst-performing 50% of solutions from the population.
Sort the population by fitness and keep the top 50%.
The best 50% should be selected as parents for reproduction.
The 'parents' list should be updated with the selected solutions and contain N/2 solutions.
Note, the 'parents' list should be cleared before adding new solutions.
"""
def prune():
    # TODO: Implement selection (pruning)
    pass  


"""
Generate new solutions by combining halves of two parent solutions.
Each new solution should take the first half from one parent and the second half from another.
The 'population' list should be updated with the new solutions.
Note, the 'population' list should be cleared before adding new solutions.
"""
def reproduce():
    # TODO: Implement reproduction (crossover)
    pass


"""
Introduce random mutations into the population.
Each coordinate in every solution has a 2% chance ('mutate_rate') of being mutated. 
For each mutated coordinate, a small random change is either -1, 0, or 1.
"""
def mutate():
    # TODO: Implement mutation
    pass


"""
Find and return the best solution (lowest fitness value).
"""
def find_best():
    best = []
    best_fit = float('inf')  
    for i in range(len(population_fits)):      
        if population_fits[i] < best_fit:
            best_fit = population_fits[i]
            best = population[i]
    print(best)
    return best

"""
Visualizes the best solution compared to the target coordinates.
"""
def visualization(best, generation):
    plt.clf()  
    # check if best solution is the target solution
    if best == target_sequence:  
        print("Target solution found!")
        plt.title("Target Solution Found!\nGeneration: " + str(generation))
        x1, y1 = best[::2], best[1::2]
        x2, y2 = target_sequence[::2], target_sequence[1::2]

        plt.scatter(x2, y2, label="Target Points", color="blue")
        plt.plot(x1, y1, color="red", label="Current Generation Path")
        plt.legend()
        plt.show() 
        return  

    x1, y1 = best[::2], best[1::2]
    x2, y2 = target_sequence[::2], target_sequence[1::2]

    plt.scatter(x2, y2, label="Target Points", color="blue")
    plt.plot(x1, y1, color="red", label="Best Solution Path")
    plt.title("Generation: " + str(generation))
    plt.legend()
    plt.draw()
    plt.pause(0.1)


# Main loop to run the genetic algorithm
Gen0()
for generation in range(200):
    print(f"Generation {generation}")
    fit_function()
    prune()
    reproduce()
    mutate()
    best = find_best()
    visualization(best, generation)

    if best == target_sequence:
        break