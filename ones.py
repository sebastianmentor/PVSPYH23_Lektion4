import random

# Parametrar
POPULATION_SIZE = 100
CHROMOSOME_LENGTH = 10000
GENERATIONS = 50
MUTATION_RATE = 0.01

# Funktion för att skapa en individ
def create_individual():
    return [random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]

# Fitness-funktion: Antalet 1:or i kromosomen
def fitness(individual):
    return sum(individual)

# Selektion: Turnering
def selection(population):
    tournament_size = 5
    selected = []
    for _ in range(len(population)):
        competitors = random.sample(population, tournament_size)
        winner = max(competitors, key=fitness)
        selected.append(winner)
    return selected

# Korsning: Enpunktskorsning
def crossover(parent1, parent2):
    crossover_point = random.randint(1, CHROMOSOME_LENGTH - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation: Bitflip-mutation
def mutate(individual):
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]
    return individual

# Skapa initial population
population = [create_individual() for _ in range(POPULATION_SIZE)]

# Huvudloop för genetiska algoritmen
for generation in range(GENERATIONS):
    # Utvärdera fitness
    population = sorted(population, key=fitness, reverse=True)

    # Utskrift av bästa individen
    best_individual = population[0]
    print(f"Generation {generation}: Bästa fitness = {fitness(best_individual)}")

    # Kontroll av terminering (om maximal fitness uppnås)
    if fitness(best_individual) == CHROMOSOME_LENGTH:
        print("Optimal lösning hittad!")
        break

    # Selektion
    selected = selection(population)

    # Skapa nästa generation
    next_generation = []

    # Elitism: Bevara de bästa individerna
    elite_size = 2
    next_generation.extend(population[:elite_size])

    # Generera nya avkommor genom korsning och mutation
    while len(next_generation) < POPULATION_SIZE:
        parent1, parent2 = random.sample(selected, 2)
        child1, child2 = crossover(parent1, parent2)
        child1 = mutate(child1)
        child2 = mutate(child2)
        next_generation.extend([child1, child2])

    population = next_generation[:POPULATION_SIZE]

# Visa den bästa lösningen
print("Bästa individen:", best_individual)
print("Kromosom:", best_individual)
print("Fitness:", fitness(best_individual))


# Förklaring av koden:

# Parametrar:

# POPULATION_SIZE: Antalet individer i populationen.
# CHROMOSOME_LENGTH: Längden på varje kromosom (antal gener).
# GENERATIONS: Maximalt antal generationer.
# MUTATION_RATE: Sannolikheten att en gen muteras.
# Funktioner:

# create_individual(): Skapar en ny individ med slumpmässiga 0:or och 1:or.
# fitness(individual): Beräknar fitnessvärdet genom att summera antalet 1:or.
# selection(population): Väljer individer för reproduktion via turneringsselektion.
# crossover(parent1, parent2): Utför enpunktskorsning mellan två föräldrar.
# mutate(individual): Muterar en individ genom att invertera bits med en viss sannolikhet.
# Huvudalgoritm:

# Initialiserar populationen med slumpmässiga individer.
# För varje generation:
# Utvärderar fitness för alla individer och sorterar populationen.
# Skriver ut bästa fitnessvärdet.
# Kontrollerar om den optimala lösningen har hittats.
# Väljer individer för reproduktion.
# Bevarar de bästa individerna (elitism).
# Genererar nya avkommor genom korsning och mutation.
# Ersätter den gamla populationen med den nya.
# Denna kod implementerar en enkel genetisk algoritm för att maximera antalet 1:or i en 
# binär sträng. Du kan justera parametrarna som POPULATION_SIZE, CHROMOSOME_LENGTH, 
# GENERATIONS och MUTATION_RATE för att se hur de påverkar algoritmens prestanda.