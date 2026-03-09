import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def calculate_fitness(candidate_word, target_word):

    score = 0
    for i in range(len(target_word)):
        if candidate_word[i] == target_word[i]:
            score += 1

    return score


def generate_random_word(length):
    return ''.join(random.choice(alphabet) for _ in range(length))


def run_genetic_algorithm(target_word):

    population_size = 100
    generation_number = 0

    population = [generate_random_word(len(target_word)) for _ in range(population_size)]

    while True:

        population = sorted(population,
                            key=lambda individual: calculate_fitness(individual, target_word),
                            reverse=True)

        best_candidate = population[0]

        print(f"Generation {generation_number} | Best Candidate: {best_candidate}")

        if best_candidate == target_word:
            print("Target word successfully evolved!\n")
            break

        next_generation = population[:10]

        while len(next_generation) < population_size:

            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])

            crossover_point = len(target_word)//2
            child = parent1[:crossover_point] + parent2[crossover_point:]

            if random.random() < 0.1:
                mutation_index = random.randint(0, len(target_word)-1)
                child = child[:mutation_index] + random.choice(alphabet) + child[mutation_index+1:]

            next_generation.append(child)

        population = next_generation
        generation_number += 1


print("\n========== GENETIC ALGORITHM DEMONSTRATION ==========")

print("\nExample 1: Evolving the word 'HELLO'")
print("Explanation: Genetic algorithms simulate evolution by selecting the best candidates and combining them.")

run_genetic_algorithm("HELLO")

print("\n---------------------------------------------")

print("\nExample 2: Evolving the word 'WORLD'")
print("Explanation: The algorithm gradually improves random strings until they match the target word.")

run_genetic_algorithm("WORLD")