#!/usr/local/bin/python3
#
# place_turrets.py : arrange turrets on a grid, avoiding conflicts
#
# Submitted by : [ISHIKA THAKUR ISTHAKUR]
#
# Based on skeleton code in CSCI B551, Fall 2022.

import sys

# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of turrets on castle_map
def count_turrets(castle_map):
    return sum([row.count('p') for row in castle_map])

# Return a string with the castle_map rendered in a human-turretly format
def printable_castle_map(castle_map):
    return "\n".join(["".join(row) for row in castle_map])

# Add a turret to the castle_map at the given position, and return a new castle_map (doesn't change original)
def add_turret(castle_map, row, col):
    return castle_map[0:row] + [castle_map[row][0:col] + ['p',] + castle_map[row][col+1:]] + castle_map[row+1:]

# Get list of successors of given castle_map state
def successors(castle_map):
    return [add_turret(castle_map, r, c) for r in range(0, len(castle_map)) for c in range(0, len(castle_map[0])) if castle_map[r][c] == '.']

# check if castle_map is a goal state
def is_goal(castle_map, k):
    return count_turrets(castle_map) == k

#safe function determines if it is safe to put turret at that position
def is_safe(castle_map):
   turret_positions = [(r, c) for r in range(len(castle_map)) for c in range(len(castle_map[0])) if castle_map[r][c] == 'p']
    # Check if any two turrets can attack each other
   for i in range(len(turret_positions)):
        for j in range(i + 1, len(turret_positions)):
            row1, col1 = turret_positions[i]
            row2, col2 = turret_positions[j]

            # Check if turrets are in the same row, column, or diagonal
            if row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2):
                return False  # Turrets can attack each other

   return True 


# Arrange turrets on the map
#
# This function MUST take two parameters as input -- the castle map and the value k --
# and return a tuple of the form (new_castle_map, success), where:
# - new_castle_map is a new version of the map with k turrets,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_castle_map, k):
    fringe = [initial_castle_map]
    while len(fringe) > 0:
        current_map = fringe.pop()
        #turrets_placed=count_turrets(current_map)
        if is_goal(current_map, k):
            return current_map, True
        for new_castle_map in successors(current_map):
                if is_safe(new_castle_map):           #if the successor map is safe then add it to fringe
                   fringe.append(new_castle_map)

    return None, False
# Main Function
if __name__ == "__main__":
    castle_map = parse_map(sys.argv[1])
    # This is k, the number of turrets
    k = int(sys.argv[2])
    print("Starting from initial castle map:\n" + printable_castle_map(castle_map) + "\n\nLooking for a solution...\n")
    solution = solve(castle_map, k)
    print("Here's what we found:")
    print(printable_castle_map(solution[0]) if solution[1] else "False")
