Digraph input format

A sequence of one or more digraphs is taken from the standard input (eg sys.stdin). Each
graph is represented by an adjacency list. The first line is an integer n indicating the order
of the graph. This is followed by n white space separated lists of adjacencies for nodes
labeled 0 to n - 1. The lists are sorted. The input will be terminated by a line consisting
of one zero (0). This line should not be processed. The sample input below shows two
digraphs, the first has node set {0, 1, 2, 3} and arc set {(0, 1), (0, 3), (1, 2), (1, 3), (2, 0)}, the
second has node set {0, 1, 2} and arc set {(0, 1), (0, 2), (2, 1)}.

4
1 3
2 3
0

3
1 2

1
0