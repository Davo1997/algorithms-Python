"""
This is a function, where you set the starting destination and final
destination of the chess horse and the function returns square by square
your steps, which is the shortest path to reach to the end...
"""

from collections import deque


def chess_horse_move(start, end):
    """This is a function that outputs the
    shortest path of the horse in chess from
    start square to end square..."""

    N = 64  # number of squares
    letters = "abcdefjh"
    numbers = "12345678"

    """Creating graph...with keys a1, b1, e6 etc."""

    graph = dict()
    for l in letters:
        for n in numbers:
            graph[l + n] = set()

    def add_edge(v1, v2):
        """A function for adding edges to graph (edges will be
        the direction of horse)"""
        graph[v1].add(v2)
        graph[v2].add(v1)

    """Looping in the 64 squares and creating first vertexes...second is empty"""

    for i in range(8):
        for j in range(8):
            v1 = letters[i] + numbers[j]
            v2 = ''

            if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
                v2 = letters[i + 2] + numbers[j + 1]
                add_edge(v1, v2)

            if 0 <= i - 2 < 8 and 0 <= j - 1 < 8:
                v2 = letters[i - 2] + numbers[j - 1]
                add_edge(v1, v2)

            if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
                v2 = letters[i - 2] + numbers[j + 1]
                add_edge(v1, v2)

            if 0 <= i + 2 < 8 and 0 <= j - 1 < 8:
                v2 = letters[i + 2] + numbers[j - 1]
                add_edge(v1, v2)

            if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
                v2 = letters[i + 1] + numbers[j + 2]
                add_edge(v1, v2)

            if 0 <= i - 1 < 8 and 0 <= j - 2 < 8:
                v2 = letters[i - 1] + numbers[j - 2]
                add_edge(v1, v2)

            if 0 <= i - 1 < 8 and 0 <= j + 2 < 8:
                v2 = letters[i - 1] + numbers[j + 2]
                add_edge(v1, v2)

            if 0 <= i + 1 < 8 and 0 <= j - 2 < 8:
                v2 = letters[i + 1] + numbers[j - 2]
                add_edge(v1, v2)

    distance = {v: None for v in graph}
    parents = {v: None for v in graph}

    distance[start] = 0
    queue = deque([start])

    while queue:
        current_vertex = queue.popleft()
        for neighbour_vertex in graph[current_vertex]:
            if distance[neighbour_vertex] is None:
                distance[neighbour_vertex] = distance[current_vertex] + 1
                parents[neighbour_vertex] = current_vertex
                queue.append(neighbour_vertex)

    path = [end]
    parent = parents[end]
    while parent is not None:
        path.append(parent)
        parent = parents[parent]
    path.reverse()
    return path

# example
print(chess_horse_move('c2', 'h7'))
