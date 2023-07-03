from collections import deque
import sys

adjacency_list = []
lines = sys.stdin.read().splitlines()
for line in lines:
   adjacency_list.append(line)

def bfs(graph, start_node):
    distance = {}
    distance[start_node] = 0
    queue = deque([start_node])

    while queue:
        node = queue.popleft()

        for neighbour in graph[node]:
            if neighbour not in distance:
                distance[neighbour] = distance[node] + 1
                queue.append(neighbour)

    return distance

def find_most_distant_node(graph):
    start_node = 1
    distances = bfs(graph, start_node)
    max_distance = max(distances.values())

    most_distant_node = max(
        (node for node, dist in distances.items() if dist == max_distance),
        default=None
    )

    return max_distance, most_distant_node





# Example graph
return_statement = ''
graphs = []
#adjacency_list = ['4', '1 3', '2 3', '0', '', '3', '1 2', '', '1', '0']
adjacency_list.pop()

i = 0
while i < len(adjacency_list):
    order = int(adjacency_list[i])
    graph = {index: [int(v) for v in value.split()] for index, value in enumerate(adjacency_list[i + 1 : i + order + 1])}
    graphs.append(graph)
    i += order + 1
#print(graphs)

for idx, graph in enumerate(graphs, start=1):
    max_distance, node = find_most_distant_node(graph)
    return_statement = return_statement + str(max_distance) + " " + str(node) + '\n'
    # print(f"Graph {idx}:")
    # print(f"Maximum distance from node 1: {max_distance}")
    # print(f"Node with the highest index at that distance: {node}")
    # print()
return_statement = return_statement.rstrip()
print(return_statement)    

# adjacency_list = ['4', '1 3', '2 3', '0', '', '3', '1 2', '', '1', '0']
# adjacency_list.pop()
# while len(adjacency_list) > 0:
#     order = int(adjacency_list[0])
#     list_to_work_on = adjacency_list[0:order+1]
#     adjacency_list = adjacency_list[order+1:]
     
#     graph = dict(enumerate(list_to_work_on[1:]))
   
    
#     for key, value in graph.items():            
#         value_list = value.split()
#         graph[key] = [int(i) for i in value_list]
#     print(graph)