Delete a node from a digraph and record number of arcs removed 30 Marks
For each digraphs in a set of digraphs given as adjacency lists, read in the digraph,
delete the node with index n − 3 where n is the order of the digraph, and write the
digraph back to the terminal. After the adjacency lists, write out how many arcs
have been removed in the process. Assume input digraphs have order at least 3.
Input format: described below under the heading “Digraph input format”.

Output format: the same as the input format but with one extra line after each
digraph stating the number of arcs that were removed when the node was removed.
Ensure that you maintain the node naming conventions.

For the example input shown below, the first digraph would have node with index
1 removed, and the second graph would have node index 0 removed, so the output
would be
3
2
0

3
2

0
2
0
Here the first line indicates the order of the new digraph is 3, the next three lines
are the three adjacency lists showing the arcs of the this digraph, and the 3 on line
5 indicates that three arcs were removed from the input digraph. The next line has
a 2 indicating that the next digraph has order 2 and so on.


Back and cross arcs in a DFS 30 Marks

For a given set of digraphs, write a program that performs DFS on each digraph
starting at node 0 and prints out the total number of back arcs and cross arcs resulting
from the traversal. Use our standard convention that when there is a choice of white
or grey nodes, the one with the lowest index should be chosen.

Input format: described below under the heading, “Digraph input format”.

Output format: For each input digraph, print out a line with the number of back
arcs, then whitespace, and then the number of cross arcs.

For the example input shown below, the output would be
1 0
0 1


BFS to find distances 30 Marks

Write a program that performs BFS on each of a given set of digraphs starting at
node 1 and prints the distance to the most distant node from 1 and reports the node
with the highest index at that distance. Nodes that are not reachable from 1 have
an undefined distance and should be ignored.

Input format: described below under the heading, “Digraph input format”.

Output format: For each input digraph, print out a line with the distance to the
most distant node, then a space, then the highest index of a node at that distance.
Ignore nodes that are not reachable from 1.

For the example input shown below, the output would be
2 0
0 1