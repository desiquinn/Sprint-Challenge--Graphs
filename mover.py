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

def short_back(curr_room, dest_room=0):
    # dest_room is the room whose exits still have a ? for a value

    # Create a queue
    queue = Queue()
    dd = Queue()
    # Create a visited set (use set because O(1) search)
    visitedB = set()
    # Add starting PATH to the queue
    #need to use a list because for a path order matters
    queue.enqueue([curr_room])
    dd.enqueue([])
    # While: queue is not empty
    while queue.len() > 0:
        # Pop first PATH out of queue
        v_path = queue.dequeue()
        d_path = dd.dequeue()
        # grab the last vertex from the path
        vertex = v_path[-1]
        # Here is where you want to check if it's dest_room
        # print(f"INSIDE BFS1: {d_path}")
        # print(vertex.id)
        # print(dest_room)
        if vertex.id == dest_room: #compare ids?
            # then return the path
            # print(f"INSIDE BFS2: {d_path}")
            return d_path
            # return v_path
        # check if not visted
        elif vertex not in visitedB:
            # mark as visited
            visitedB.add(vertex)
            # get adjacent edges and add to back of path
            # print(f"VERTEX:\n {vertex}")
            for direction in vertex.get_exits():
                # make a copy of the path
                new_path = v_path.copy()
                new_direct = d_path.copy()
                # add neighbor to the back of that path
                new_path.append(vertex.get_room_in_direction(direction))
                # print(new_path)
                # how do we get the direction to append
                new_direct.append(direction)
                # print(new_direct)
                # add the path to the queue
                queue.enqueue(new_path)
                dd.enqueue(new_direct)
    # goto top of loop - happens automatically


def mover(player, graph):
    # track directions
    current_path = []
    # track back_path
    back_path = []

    """
    initiated visited
    """
    # track visited
    visited = set()
    # add starting room of player to visited
    visited.add(player.current_room)

    """
    creating the map
    """
    # Create a undiscovered dictionary
    undiscovered = {}
    # initialize the undiscovered rooms dictionary with the starting_room, exits, and "?" for values
    exits = player.current_room.get_exits()
    # {0:{"n": "?", "s": "?", "e": "?", "w": "?" }}
    undiscovered[player.current_room.id] = {key: "?" for key in exits}

    print(f"Initial Map: {undiscovered}.\n\n")

    # Check if all rooms have been visited
    # while the length of visited is less than the length of the graph...
    while len(visited) < len(graph):
        print("More rooms to discover in this world...\n")

        # Check room to see if there are any undiscovered rooms
        # If their are undiscovered rooms (then go down that path)
        if "?" in undiscovered[player.current_room.id].values():
            # move the player through the rooms by...

            """
            Randomizing the exit choice
            """
            # - picking a directions from the current room's keys that have a value of "?"
            directions = undiscovered[player.current_room.id].keys() # gives me back a list
            unknown_room = []

            for key in directions:
                if undiscovered[player.current_room.id][key] == "?":
                    unknown_room.append(key)

            # pick a random choice from unknown_room
            choice = random.choice(unknown_room)
            # store the opposite direction of that choice
            opposite = turn(choice)
            # update the foward path with this direction
            current_path.append(choice)


            """
            Move player forward
            """
            print("Player moving foward...\n")
            # - use player.travel(direction) to move the player in that direction
            player.prev_room = player.current_room
            #travel to next room
            player.travel(choice)
            print(f"CURRENT ROOM:\n {player.current_room}\n\n")
            # update the undiscovered dictionary to add the new current_room
            undiscovered[player.prev_room.id][choice] = player.current_room.id
            # add current room to visited
            visited.add(player.current_room)
            # update the newly added room with the .get_exits()
            exits = player.current_room.get_exits()
            print(f"ROOM EXITS: {exits}\n")
            undiscovered[player.current_room.id] = {key: "?" for key in exits}
            undiscovered[player.current_room.id][opposite] = player.prev_room.id
            
            """
            create a path to go backwards
            """
            # print(f"BACK PATH1:\n{back_path}\n")
            # incomplete_room = 
            print("Creating back_path...\n")
            # back_path = short_back(player.current_room, incomplete_room)
            back_path.append(opposite)
            # print(f"UPDATED MAP:\n{undiscovered}\n")
            # print(f"BACK PATH2:\n{back_path}\n")

            # Then do it again/loop with the current room

        # if there are no undiscovered room (than backtrack)
        else:
            

            # print(f"No Undiscovered exits in this room...\n\nPlayer moving backwards...\n{back_path}\n")
            print(f"No Undiscovered exits in this room...\n\nPlayer moving backwards...\n")
            """
            Move Player Backwards
            """
            
            # move_back = back_path[:1][0]
            move_back = back_path.pop()
            print(f"MOVING... {move_back}")
            player.travel(move_back)
            # print(f"CURRENT ROOM:\n {player.current_room}\n\n")
            current_path.append(move_back)

            # qq = Queue()
            # qq.enqueue([player.current_room.id])
            # while qq.len() > 0:
            #     short_path = qq.dequeue()
            #     print(f"sp {short_path}")
            #     room_id = short_path[-1]
            #     if "?" in undiscovered[room_id].values():
            #         print(short_path)
            #         return short_path
            #     else:
            #         for ee in player.current_room.get_exits():
            #             new_path = short_path.copy()
            #             neighbor_id = undiscovered[player.current_room.id][ee]
            #             new_path.append(neighbor_id)
            #             qq.enqueue(new_path)

            # print(short_path)
            # back_up = short_path


    print(f"MAP:\n\n{undiscovered}\n")
    print(f"PATH TAKEN:\n\n {current_path}\n")
    # After all room have been visited at least once return the current_path
    return current_path
