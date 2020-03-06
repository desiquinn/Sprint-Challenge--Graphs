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

*** try using the dictionary like the ReadMe because the stacks and queues are confusing me***
# create a undiscovered dictionary
# Check room to see if there are any undiscovered rooms (if "?" in undiscovered[player.current_room.id].values())
# while their are undiscovered rooms
    # initialize the undiscovered rooms dictionary with the starting_room
    # move the player through the rooms by...
    # - picking a directions from the current room's keys that have a value of "?"
    # - update the path with this direction
    # - use player.travel(direction) to move the player in that direction
    # update the undiscovered dictionary to add the new current_room
    # update the newly added room with the .get_exits()
    # Then do it again/loop with the current room

How to backtrack? 
*** insert this in the loop above so that when it backtracks it finished undiscovered paths in the previous room ***

# Create an opposite path
# add the opposite direction to each path
# Want to only backtrack if there there are no paths to explore in the current room
    # use player.travel(back_direction) to move the playe back a room


*** Stacks and queues method... confusing me ***
An algorithm that explores the graph via DFT

# Create a stack
# Create a visted set
# Add current_room to the stack
# Create a paths list
# While the stack is full
    # remove the top room from the stack
    # if the room is not in visted
        # add room to visited
        # Do someting to the room...
            # get all the exits of current room
            - problem to solve: don't know what rooms are in each direction
            - solution: use the BFS algorithm to discover a path that ends with a ?
            # for each exit of the exits
                # pass them into the BFS algorithm
                # store returned path in a variable
        # for each of it's neighbors
            # add the neighboring rooms to the stack

Add BFS to find the neighboring rooms with ? as value

# Create a queue
# Create a discovered set
# Add exit to the queue
# While the queue is full
    # remove the first exit from the queue
    # if the room is not in discovered
        # add room to discovered
        # Do someting to the room...
            - return a path?
        # for each of it's neighbors
            # add the neighboring rooms to the queue

How to keep track of the path?

# Get direct path from the BFS
# call player.travel() to travel in these directions
# As player travels in a particular direction
    # add direction to the traversal_path list
# When player lands in room
    # Update current_room to that room and loop
