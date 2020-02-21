Reviewed the lecture video
Reviewed the Spec
Reviwed the Code
Given:
    * All the code necessary to load a world with 500 rooms and move a player around it.
Task:
    * Create an algorithm that:
    - traverses the entire graph provided
    - appends a path to the traversal_path list
        + path must visit every room at least once
    * Optimize the graph to have overcome the following obstacles:
    - Deadends
    - Branches
    - Cycles
Questions/Explorations:
What are my inputs to the algorithm?
    - The current room (starting vertex)
    - The player
    - Empty Path
    - Empty visited??
What are we calling the algorithm on?
    - passing in the player and using player.travel(direction) to move through each of the rooms
    - leave show rooms as False because I don't want to get to much data back that is unnecessary.
What is being returned?
    - Return the Path
What type of graph is this?
    - Undirected
    - Dense
    - Cyclic
Is this going to be a depth first traversal, breadth first traversal, a combination, or another type of traversal?
    - I am going to have to use a combination of DFT and BFS to solve this problem
    - *** Research other algorithms before I get started ***
What will i need to keep track of during the traversal and how?
    - Visted_rooms (in a set)
    - Paths currently being built (in a stack with dft)
    - Dead Ends or Path with no more Unvisited branches (in a set) - or does this get added to the traversal path?
    - Unvisted paths (maybe in a queue with a bfs)
When do i add a path to the traversal path?
    - every time the player moves in that direction?
What conditional statements needs to be in place to manipulate the traversal behavior?
    - If no more unvisted branches backtrack to nearest room with unvisted branches
    - if there's a cycle don't stop and backtrack keep going.
Can i split these conditions into sperate functions? How?
    - Do the BFS in a seperate function from the DFT and use it only in certain situations.
What is the most optimal way to traverse a graph with dead ends?
    *** Research ***
How do i handle branches?
    *** Research ***
    - go to the deepest part of the branch then backtrack to the nearest room with unexplored branches and explore of them always returning back to that room until it too has no more branches to explore
    - This occurs with a DFT
How do i handle cycles?
    *** Research ***
    - 
Under what condition do I need DFT?
    - While exploring a path to put in the traversal_path list
Under what condition do I need BFS?
    - While building a map to all the rooms and exploring rooms with a question mark
Can I tell DFT what direction I want it to start in?
    *** Research ***
    - use the player.travel(direction) 
How do I translate a move, or room id into a direction to add to the path?
    - return the direction that was used to get to that room
How do i build an adjacey list or matrix while exploring the rooms?
    *** Research ***
    Explore the map by creating a adjacency dictionary 
    {
    0:{"n": "?", "s": "?", "e": "?", "w": "?" },
    4:{"s": "?"}
    }

    0 = the room
    list = the path to each adjacent room
    keys = the directions to move in
    value = the room you will arrive at

    get the room from player.current_room
    get the exits from player.current_room.get_exits()
    hard code the "?" string when first appending a room



