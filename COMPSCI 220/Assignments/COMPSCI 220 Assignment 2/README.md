Write a programme that takes input as described below and prints output as
described below. The programme must work with the automated marker.
A variant of the game of boules works as follows. First, a small ball is thrown onto a field, and
then every player throws one large ball each, attempting to get it as close as possible to the first
ball. Finally players are ranked by how close their ball is to the small ball. Given the names and
coordinates of all balls, compute the player ranking.

Input: The first input line is a non-negative integer n indicating how many players there are. The
next n lines consist of three elements each, separated by spaces: one string indicating the owner
of a ball, and the (x, y) coordinates of the ball with respect to the small ball in millimetres, as two
integers. For example:

3
Antoine 0 100
Brigitte 100 -10
Camille 50 50

You can assume that the small ball is at position (0, 0).

Output: The output must consist of the player names, ranked by the proximity of their ball to the
small ball. You may assume that there are no ties. For example, for the input given above the output
should be:

Camille
Antoine
Brigitte