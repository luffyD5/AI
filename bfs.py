from collections import defaultdict, deque
def bfs(graph, root, search):
    visited = set()
    queue = deque([(root, [root])])
    parent = {}  
    while queue:
        node, path = queue.popleft()
        visited.add(node)
        if node == search:
            print("Path to", search, ":", path)
            print("Visited ::",visited) 
            return True 
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))  # Include path
                parent[neighbor] = node  # Store parent information
    print("Element", search, "not found.")
    print("Visited ::",visited)
    return False
def graph_input():
    graph = defaultdict(list)
    no_edges = int(input("Enter no. of edges: "))
    for i in range(no_edges):
        u, v = input("Enter an edge (format: u v): ").split()
        graph[u].append(v)
    return graph
graph = graph_input()
root = (input("Enter the root element: "))
search = (input("Enter the element to search: "))
bfs(graph, root, search)
