from itertools import combinations

def apriori_algorithm(transactions, minimum_support):

    unique_items = set(item for transaction in transactions for item in transaction)
    frequent_itemsets = {}

    for size in range(1, len(unique_items) + 1):
        for itemset in combinations(unique_items, size):

            occurrence_count = 0

            for transaction in transactions:
                if set(itemset).issubset(transaction):
                    occurrence_count += 1

            support_value = occurrence_count / len(transactions)

            if support_value >= minimum_support:
                frequent_itemsets[itemset] = support_value

    return frequent_itemsets


print("\n========== APRIORI ALGORITHM DEMONSTRATION ==========")

print("\nExample 1: Supermarket purchase pattern analysis")

supermarket_transactions = [
    ['Bread', 'Milk'],
    ['Bread', 'Diaper', 'Beer', 'Eggs'],
    ['Milk', 'Diaper', 'Beer', 'Cola'],
    ['Bread', 'Milk', 'Diaper', 'Beer'],
    ['Bread', 'Milk', 'Diaper', 'Cola']
]

results = apriori_algorithm(supermarket_transactions, 0.4)
for itemset, support in results.items():
    print(f"Items: {itemset} | Support: {support:.2f}")


print("\n---------------------------------------------")

print("\nExample 2: Fast food restaurant order patterns")

restaurant_orders = [
    ['Burger', 'Fries', 'Soda'],
    ['Burger', 'Fries'],
    ['Fries', 'Soda'],
    ['Burger', 'Soda'],
    ['Burger', 'Fries', 'Soda']
]

results2 = apriori_algorithm(restaurant_orders, 0.4)
for itemset, support in results2.items():
    print(f"Items: {itemset} | Support: {support:.2f}")
print()