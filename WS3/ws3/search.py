# search.py
# ---------------
# Created by Yaya Wihardi (yayawihardi@upi.edu) on 15/03/2020

# Fungsi search harus me-return path.
# Path berupa list tuples dengan format (row, col) 
# Path merupakan urutan states menuju goal.
# maze merupakan object dari Maze yang merepresentasikan keadaan lingkungan 
# beberapa method dari maze yang dapat digunakan:

# getStart() : return tuple (row, col) -> mendapatkan initial state
# getObjectives() : return list of tuple [(row1, col1), (row2, col2) ...] -> mendapatkan list goal state
# getNeighbors(row, col) : input posisi, return list of tuple [(row1, col1), (row2, col2) ...]
#                          -> mendapatkan list tetangga yg mungkin (expand/sucessor functiom)
# isObjective(row, col) : return true/false -> goal test function

import queue

# def search(maze):
#     return []

def search(maze):
    path = []
    visited = {}
    past = {}
    frontier = queue.Queue()
    start = maze.getStart()
    objective = maze.getObjectives()
    frontier.put(start)

    while(frontier.empty() == False):
        temp = frontier.get()
        if(temp in objective):
            path.append(temp)
            while (temp != start):
                path.append(past[temp])
                temp = past[temp]
            path.append(start)
            path.reverse()
            return path
        visited[temp] = 1;
        neighbors = maze.getNeighbors(temp[0], temp[1])
        current = temp
        for neighbor in neighbors:
            if(neighbor not in visited):
                visited[neighbor] = 1
                past[neighbor] = current
                frontier.put(neighbor)
    if not path:
        #print("None")
        return None
    #print("Path")
    return path


