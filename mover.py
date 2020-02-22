from util import Stack, Queue
import random 

# Create an opposite path by switching directions
def turn(direction):
    if direction == "n":
        return "s"
    elif direction == "s":
        return "n"
    elif direction == "e":
        return "w"
    elif direction == "w":
        return "e"

def mover(player, graph):
    # track visited
    visited = set()
    # track directions
    current_path = []
    # Create a undiscovered dictionary
    undiscovered = {}
    # track back_path
    back_path = []

   
    # initialize the undiscovered rooms dictionary with the starting_room, exits, and "?" for values
    exits = player.current_room.get_exits()
    # {0:{"n": "?", "s": "?", "e": "?", "w": "?" }}
    undiscovered[player.current_room.id] = {key: "?" for key in exits}
    visited.add(player.current_room)


    print(f"Initial Undiscovered: {undiscovered}.\nNothing before this is repeated.\n")


    # Check if all rooms have been visited
    # while the length of visited is less than the length of the graph...
    while len(visited) < len(graph):
        print("All rooms have not been visited yet")

        # Check room to see if there are any undiscovered rooms
        # If their are undiscovered rooms (then go down that path)
        if "?" in undiscovered[player.current_room.id].values():
            # move the player through the rooms by...

            # - picking a directions from the current room's keys that have a value of "?"
            directions = undiscovered[player.current_room.id].keys() # gives me back a list
            unknown_room = []

            for key in directions:
                if undiscovered[player.current_room.id][key] == "?":
                    unknown_room.append(key)

            # pick a random choice from unknown_room
            choice = random.choice(unknown_room)
            # update the paths with this direction
            current_path.append(choice)

            opposite = turn(choice)
            back_path.append(opposite)
            print(f"back_path {back_path}")
            # - use player.travel(direction) to move the player in that direction
            player.prev_room = player.current_room

            #travel to next room
            player.travel(choice)
            print(player.current_room)
            # update the undiscovered dictionary to add the new current_room
            # update the newly added room with the .get_exits()
            undiscovered[player.prev_room.id][choice] = player.current_room.id
            
            visited.add(player.current_room)
            exits = player.current_room.get_exits()
            print(exits)
            undiscovered[player.current_room.id] = {key: "?" for key in exits}
            undiscovered[player.current_room.id][opposite] = player.prev_room.id
            # Then do it again/loop with the current room
            print(undiscovered)

        # if there are no undiscovered room (than backtrack)
        else:
            print(f"Moving Backwards now\n{back_path}\n")

            qq = Queue()
            qq.enqueue([player.current_room])
            while qq.len() > 0:
                short_path = qq.dequeue()
                print(f"sp {short_path}")
                rr = short_path[-1]
                if "?" in undiscovered[rr.id].values():
                    print(rr.id)
                    return rr.id
                else:
                    visited.add(rr)

                    for ee in player.current_room.get_exits():
                        new_path = short_path.copy()
                        new_path.append(ee)
                        qq.enqueue(new_path)

            print(short_path)
            back_up = back_path.pop()
            # back_up = short_path
            player.travel(back_up)
            current_path.append(back_up)



    print(current_path)
    # After all room have been visited at least once return the current_path
    return current_path






# Stacks and Queues Method 
#     # traverses via DFT
#     # Create a stack
#     stack=Stack()
#     # Create a visted set
#     visited = set()
#     # Add current_room to the stack
#     stack.push(player.current_room)
#     # Create a paths list
#     paths = []
#     # While the stack is full
#     while stack.len() > 0:
#         # remove the top room from the stack
#         room = stack.pop()
#         # if the room is not in visted
#         if room not in visited:
#             # add room to visited
#             visited.add(room)
#             # Do someting to the room...
#             # get all the exits of current room
#             exits = player.current_room.get_exits()
#             print(f"info from mover {room}")
#             print(exits)
#             # for each exit of the exits
#             for ee in exits:
#                 # pass them into the BFS algorithm
#                 discover_rooms(ee)
#                 # store returned path in a variable
#             # for each of it's neighbors
#                 # add the neighboring rooms to the stack
            
            
# def discover_rooms(exit):
#     # Create a queue
#     qq = Queue()
#     # Create a discovered set
#     discovered= set()
#     # Add exit to the queue
#     qq.enqueue(exit)
#     # While the queue is full
#     while queue.len() > 0:
#         # remove the first exit from the queue
#         mystery_room = qq.dequeue()
#         # if the room is not in discovered
#         if qq not in discovered:
#             # add room to discovered
#             discovered.add(mystery_room)
#             # Do someting to the room...
#                 #- return a path?
#             # for each of it's neighbors
#                 # add the neighboring rooms to the queue