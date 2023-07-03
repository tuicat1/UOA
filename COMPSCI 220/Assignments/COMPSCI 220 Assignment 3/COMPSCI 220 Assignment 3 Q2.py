import sys


adjacency_list = []
lines = sys.stdin.read().splitlines()
for line in lines:
   adjacency_list.append(line)
def dfs(graph):
    num_nodes = len(graph)
    seen = [-1] * num_nodes
    done = [-1] * num_nodes
    time = 0

    def explore(node):
        nonlocal time
        seen[node] = time
        time += 1

        for neighbor in graph[node]:
            if seen[neighbor] == -1:
                explore(neighbor)

        done[node] = time
        time += 1

    for node in range(num_nodes):
        if seen[node] == -1:
            explore(node)

    return seen, done

def check_arc_type(graph, seen, done, v, w):
    if seen[w] < seen[v] < done[v] < done[w]:
        return "Back arc"
    elif seen[w] < done[w] < seen[v] < done[v]:
        return "Cross arc"
    else:
        return "Neither"







# Example graph
graph = {0: [1, 3], 1: [2, 3], 2: [0], 3: []}

seen_list, done_list = dfs(graph)

#print("Seen:", seen_list)
#print("Done:", done_list)



return_message = ''
#adjacency_list = ['4', '1 3', '2 3', '0', '', '3', '1 2', '', '1', '0']
graphs = []
i = 0
while i < len(adjacency_list):
    order = int(adjacency_list[i])
    graph = {index: [int(v) for v in value.split()] for index, value in enumerate(adjacency_list[i + 1 : i + order + 1])}
    graphs.append(graph)
    i += order + 1
graphs.pop()


for graph in graphs:
    seen_list, done_list = dfs(graph)
    cross_arcs = 0
    back_arcs = 0
    for v in graph:
        for w in graph[v]:
            arc_type = check_arc_type(graph, seen_list, done_list, v, w)
            if arc_type == "Back arc":
                back_arcs += 1
            if arc_type == "Cross arc":
                cross_arcs += 1
    print(back_arcs, cross_arcs)
            





