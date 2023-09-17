# isthakur
### PART 1 SEARCHING A MAP FOR PATH 
The solution defined in the map_castle.py file uses the BFS strategy to define the path since the problem mentions that shortest path is required and BFS guarantees that.
## CHALLENGES FACED
While starting on the solution I wasn't sure if I should initialize another queue or work on the fringe variable itself.
Also how exactly should we incorporate directions character depending on the move was one issue I faced during the programming.Initially I took the direction variable as ([1,0,'U'],[-1,0,'D'],[0,1,'R'],[0,-1,'L']) but then I used the if-else statement
## SIMPLIFICATIONS 
The move variable contains row and columns coordinate and Earlier I decided to use 2 queues each for row queue and column queue , the program felt too complex to deal with so many variables so improvised to using just 1 queue

## SEARCH ABSTRACTION
The program uses the Breadth First Search to output the shortest path to reach goal state.First the fringe queue for noed to be explored and is intialized with current location.
BFS used which explores all the nodes it encounters while also exploring the neighbouring nodes which are added to the queue afor each of the node that is dequeued 
Visited queue stores all the nodes that are visited to avoid going into an infinite loop.
If the current location is identified as goal state("@") then the path is traced back from start to end along with distance and direction string 

**GOAL STATE**=Cell marked "@" representing the end of the maze or the exit

**START STATE**=cell marked "p" represents the start position for maze traversal to reach the goal state

**VALID STATE**=the cells marked "." in the 4 directions namely up,down,left,right and "@" that are within the map indexes 

**SUCCESSOR FUNCTION**=determines the moves which can be made from start node to reah end node through the valid states.In this maze-solving problem, the successor function generates valid moves from a current position to neighboring positions within the maze that are open ('.') or the goal position ('@').

**COST FUNCTION**= The cost function defines the cost associated with moving from one state to another. In this specific problem, we are considering all moves to be of equal cost (uniform cost), i.e 1. This means that reaching any neighboring position within the maze has a cost of 1.

### REASON PROGRAM FAILS TO FIND A SOLUTION
1.MAZE COMPLEXITY-If the maze is too complex with dead-end and loops which can lead to longer time and algorithm failing to provide a solution

2.The program goes into the infinite loop if there are bugs in the code as in this case the code did not track the which nodes are already visited and hence the program would then enter an infinite loop 

3.Edge cases need to be handled carefully such as when multiple start nodes are there or unexpected symbols in maze.

4.Proper data structure (queue in this case) should be used which makes sure all the neighbouring nodes are visited before moving to the farther nodes.


### PART 2 SEARCH FOR DESIGN
The second part uses N-Queen to place the turrets on the map of the castle such that no 2 turrets can attack each other.The search abstraction involves exploring the solution space in a depth-first manner by considering each possible turret placement and checking if it leads to a valid solution.

**SUCCESSOR FUNCTION**=the successor function determines the possible places a turret can be placed within the map on position marked "."

**GOAL STATE**= It is the state when all the given turrets(=k) are successfully placed on the map such that no 2 turrets can attack each other

**START STATE**=Map with walls(X) and open spaces (".") and one turret placed (denoted by "p")

**SAFETY CHECK** = The is_safe function checks if the placement of turrets in the current configuration is safe, considering constraints such as not allowing turrets to threaten each other unless there's an "X" in between.

**COST FUNCTION**-no explicit cost function in this case

**SEARCH ABSTARCTION**=The solve function uses a basic DFS approach to explore the state space. It maintains a fringe (a stack) of states to explore and iteratively expands states by adding turrets. The fringe is implemented as a Last-In-First-Out (LIFO) queue, typical of DFS.

## CHALLENGES FACED
1.the function to determine whether the particular position is safe or not was little challenging as the position of walls also have to be considered and I could not make assumption when "@" is also involved hence i have assumed that wont affect the turret posiitoning.

2.Could not determine how to make the algorithm run faster 

3.Was unable to pass the second test case . Only 1 test case passed 
