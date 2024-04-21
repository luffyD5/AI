from collections import defaultdict
def dfs(graph, root, search):
    visited = set()
    path = []
    stack = []
    stack.append(root)
    while stack:
        current = stack.pop()
        if current == search:
            visited.add(current)  
            path.append(current)  
            print("Visited nodes:", visited)
            print("DFS path:", path)
            return
        if current not in visited:
            visited.add(current)
            path.append(current)
            for i in graph[current]:
                stack.append(i)
    print("Element not found:", search)
    print("Visited nodes:", visited)
    print("DFS path:", path)
def graph_input():
    graph = defaultdict(list)
    no_edges = int(input("Enter no. of edges: "))
    for i in range(no_edges):
        u, v = map(int, input("Enter an edge (format: u v): ").split())
        graph[u].append(v)
    return graph
graph = graph_input()
root = int(input("Enter the root element: "))
search = int(input("Enter the element to search: "))
dfs(graph, root, search)
