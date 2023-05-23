import itertools
import sys

def calculate_distance(points, order):
    distance = 0
    for i in range(len(order) - 1):
        distance += distance_between(points[order[i]], points[order[i+1]])
    return distance

def distance_between(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def tsp(points):
    num_points = len(points)
    best_order = None
    best_distance = sys.maxsize

    all_orders = list(itertools.permutations(range(num_points)))

    for order in all_orders:
        distance = calculate_distance(points, order)
        if distance < best_distance:
            best_distance = distance
            best_order = order

    return best_order, best_distance

# Contoh datanya
points = [(0, 0), (2, 6), (3, 4), (6, 3), (7, 8)]

best_order, best_distance = tsp(points)

print("Titik Terbaik :")
for i in best_order:
    print(points[i])
print("Jarak Terbaik :", best_distance)
