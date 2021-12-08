from collections import deque
import random

"""
  This is a program, that takes randomly some roads (the quantity of the randomly taken
roads is equal to quantity of vertexes // 2), takes randomly any number from 1 to 
10 (it will be the traffic minute), creates a traffic in that roads. After that it adds
the traffic minute to the main minute that approximately would be taken for driving by
the current road. After that program asks user - 'You want to know the shortest path or
the path that will take for crossing the minimal time? and shows the choice of the user
(shows path (for ex. a -> b -> c->) and the distance or time, it depends on user's choice.)
"""

def traffic(G):
    """This is a function for adding traffic time to the main time..."""

    """list of graph's keys"""
    G_keys = []
    for i in G:
        G_keys.append(i)
    a = len(G)
    """looping in range equal to graph's vertexes quantity // 2"""
    for i in range(a // 2):
        """randomly taking a vertex from graph"""
        vertex_1 = random.choice(G_keys)
        """list of vertex's keys"""
        vertex_1_keys = list(G[vertex_1].keys())
        """randomly taking second vertex (that is neighbour with first vertex)"""
        vertex_2 = random.choice(vertex_1_keys)
        """randomly getting a traffic time (from 1 to 10 minutes)"""
        traffic_time = random.randint(1, 10)
        """adding the traffic time to the vertexes's main time"""
        G[vertex_1][vertex_2][-1] += traffic_time
        G[vertex_2][vertex_1][-1] += traffic_time
    return G

def reveal_shortest_path(G, start, finish, shortest_distances):
    """This is a function that shows the path from
    start to finish..."""

    """adding finish vertex to the list"""
    complete = [finish]
    """looping while finish vertex is not the start vertex..."""
    while shortest_distances[finish] != shortest_distances[start]:
        """looping in 'G' graph 'finish' vertex's neighbours..."""
        for neighbour in G[finish]:
            """if the distance of 'finish' is equal to distance of his neighbour + their edge weight..."""
            if shortest_distances[finish] == shortest_distances[neighbour] + G[finish][neighbour][0]:
                complete.append(neighbour)
                """turning the neighbour vertex into the finish vertex..."""
                finish = neighbour
                break
    complete.reverse()
    return complete

def reveal_shortest_time(G, start, finish, shortest_times):
    final = [finish]
    while shortest_times[finish] != shortest_times[start]:
        """looping in graph's 'finish' vertex's neighbours..."""
        for neighbour in G[finish]:
            """if the distance of 'finish' is equal to distance of his neighbour + their edge weight..."""
            if shortest_times[finish] == shortest_times[neighbour] + G[finish][neighbour][-1]:
                final.append(neighbour)
                """turning the neighbour vertex into the finish vertex..."""
                finish = neighbour
                break
    final.reverse()
    return final

def maps(G):
    start = input("Enter from which vertex to start: ")
    while start not in G:
        start = input("Your entered vertex is not in Graph. Enter from which vertex to start: ")
    finish = input("Enter the final vertex: ")
    while finish not in G:
        finish = input("Your entered vertex is not in Graph. Enter the final vertex: ")

    traffic(G)

    queue = deque()
    shortest_distances = dict()
    shortest_distances[start] = 0
    queue.append(start)
    while queue:
        current_vertex = queue.pop()
        for neighbour in G[current_vertex]:
            if neighbour not in shortest_distances \
                    or shortest_distances[current_vertex] + G[current_vertex][neighbour][0] \
                    < shortest_distances[neighbour]:
                shortest_distances[neighbour] = shortest_distances[current_vertex] + G[current_vertex][neighbour][0]
                queue.append(neighbour)

    time_queue = deque()
    shortest_times = dict()
    shortest_times[start] = 0
    time_queue.append(start)
    while time_queue:
        current_v = time_queue.pop()
        for neighbour in G[current_v]:
            if neighbour not in shortest_times \
                    or shortest_times[current_v] + G[current_v][neighbour][-1] < shortest_times[neighbour]:
                shortest_times[neighbour] = shortest_times[current_v] + G[current_v][neighbour][-1]
                time_queue.append(neighbour)

    answer = input("You want to khow the shortest path from %r to "
                   "%r or the path that takes the shortest time ? \nPlease enter 'path' or 'time': " % (start, finish))
    choice = ['path', 'time']
    while answer not in choice:
        answer = input("Please enter 'path' or 'time': ")
    if answer == 'path':
        answer = reveal_shortest_path(G, start, finish, shortest_distances)
        path = ''
        for i in answer:
            if answer[-1] == i:
                path += i
            else:
                path += i + ' -> '
        return "The shortest distance from %r to %r is -> "%(start, finish) + str(shortest_distances[finish]) \
               + "\nThe path from %r to %r is ===> "%(start, finish) + path
    elif answer == 'time':
        answer = reveal_shortest_time(G, start, finish, shortest_times)
        path = ''
        for i in answer:
            if answer[-1] == i:
                path += i
            else:
                path += i + ' -> '
        return "The shortest time that takes to go from %r to %r is -> " % (start, finish) \
               + str(shortest_times[finish]) + "\nThe path from %r to %r is ===> " % (start, finish) + path


# G = {v1: {v2: [distance, time]}}

G = {'a': {'b': [1, 2], 'c': [3, 1]},
     'b': {'a': [1, 2], 'd': [2, 2]},
     'c': {'a': [3, 1], 'd': [2, 5]},
     'd': {'b': [2, 2], 'c': [2, 5]}
     }

print(maps(G))
