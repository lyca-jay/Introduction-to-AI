import heapq

def A_star(graph, start_location, goal_location, heuristic_values):
    
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_location))

    cost_from_start = {node: float('inf') for node in graph}
    cost_from_start[start_location] = 0

    previous_node = {}

    while priority_queue:
        current_cost, current_location = heapq.heappop(priority_queue)

        if current_location == goal_location:
            path = []
            while current_location in previous_node:
                path.append(current_location)
                current_location = previous_node[current_location]
            path.append(start_location)
            path.reverse()
            return path

        for neighbor, distance in graph[current_location]:
            new_cost = cost_from_start[current_location] + distance

            if new_cost < cost_from_start[neighbor]:
                cost_from_start[neighbor] = new_cost
                priority = new_cost + heuristic_values[neighbor]
                heapq.heappush(priority_queue, (priority, neighbor))
                previous_node[neighbor] = current_location

    return None


print("\n========== A* ALGORITHM DEMONSTRATION ==========")

print("\nExample 1: Finding the shortest route between cities")

city_graph = {
    'Kabacan': [('Mlang', 10), ('Kidapawan', 25)],
    'Mlang': [('Tulunan', 15)],
    'Kidapawan': [('Tulunan', 10)],
    'Tulunan': [('Tacurong', 20)],
    'Tacurong': []
}

city_heuristic = {
    'Kabacan': 30,
    'Mlang': 20,
    'Kidapawan': 15,
    'Tulunan': 10,
    'Tacurong': 0
}

route = A_star(city_graph, 'Kabacan', 'Tacurong', city_heuristic)

print("Start Location: Kabacan")
print("Destination: Tacurong")
print()
print("Shortest Route Found:", " -> ".join(route))


print("\n---------------------------------------------")

print("\nExample 2: Robot navigating inside a warehouse")

warehouse_graph = {
    'Entrance': [('Shelf_A', 3), ('Shelf_B', 4)],
    'Shelf_A': [('Packing_Station', 5)],
    'Shelf_B': [('Charging_Station', 2)],
    'Charging_Station': [('Packing_Station', 3)],
    'Packing_Station': []
}

warehouse_heuristic = {
    'Entrance': 7,
    'Shelf_A': 4,
    'Shelf_B': 3,
    'Charging_Station': 2,
    'Packing_Station': 0
}

robot_path = A_star(warehouse_graph, 'Entrance', 'Packing_Station', warehouse_heuristic)

print("Robot Start Position: Entrance")
print("Robot Target: Packing Station")
print()
print("Optimal Robot Path:", " -> ".join(robot_path))
print("\n---------------------------------------------")

