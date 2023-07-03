import heapq
from math import sqrt
import sys


lines = sys.stdin.read().splitlines()
#print(lines)

def convert_to_list(data):
    result = []
    for item in data:
        values = item.split(',')
        converted_values = [int(val) if val.isdigit() else float(val) for val in values]
        result.append(converted_values)
    return result

def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def shortest_path(coordinates, max_distance):
    points = [(coordinates[i], coordinates[i+1]) for i in range(0, len(coordinates), 2)]
    num_points = len(points)
    graph = {i: [] for i in range(num_points)}
    for i in range(num_points):
        for j in range(i+1, num_points):
            distance = euclidean_distance(points[i], points[j])
            if distance <= max_distance:
                graph[i].append((j, distance))
                graph[j].append((i, distance))
    distances = [float('inf')] * num_points
    distances[0] = 0
    pq = [(0, 0)]  
    while pq:
        dist, point = heapq.heappop(pq)
        if point == num_points - 1:
            return dist
        if dist > distances[point]:
            continue
        for neighbor, weight in graph[point]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    # frog cant make it :(
    return -1


#coordinates = [25,25,10,1,50,25,140,30]

max_distance = 100

coordinates = convert_to_list(lines)
#print(coordinates)
for coordinate_list in coordinates:
    #print(coordinate_list[1:])
    result = shortest_path(coordinate_list[1:], max_distance)
    if result == -1:
        print(-1)
    else:
        print('{:.2f}'.format(result))
