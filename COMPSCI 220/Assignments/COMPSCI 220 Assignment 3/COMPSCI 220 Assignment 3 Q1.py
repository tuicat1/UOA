import sys


adjacency_list = []
lines = sys.stdin.read().splitlines()
for line in lines:
    adjacency_list.append(line)
#adjacency_list = ['4', '1 3', '2 3', '0', '', '3', '1 2', '', '1', '0']
return_statement = ''

while len(adjacency_list) > 0:
    order = int(adjacency_list[0])
    list_to_work_on = adjacency_list[1:order + 1]
    adjacency_list = adjacency_list[order + 1:]

    arcs_deleted = 0

    if order >= 3:
        node_to_delete = order - 3
        digraph_dic = dict(enumerate(list_to_work_on))

        arcs_deleted += len(digraph_dic.pop(node_to_delete).split())

        for key, value in digraph_dic.items():
            node_list = [int(i) for i in value.split() if int(i) != node_to_delete]
            if str(node_to_delete) in value:
                arcs_deleted += 1

            node_list = [n - 1 if n > node_to_delete else n for n in node_list]

            digraph_dic[key] = ' '.join(str(n) for n in node_list)

        return_statement += str(len(digraph_dic)) + '\n'
        for value in digraph_dic.values():
            return_statement += ' '.join(str(x) for x in value) + '\n'
        return_statement += str(arcs_deleted) + '\n'

return_statement += '0'
print(return_statement)
