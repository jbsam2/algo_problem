def solution(n, path, order):
    graph = [[] for i in range(n)]
    while path:
        src, dest = path.pop()
        graph[src].append(dest)
        graph[dest].append(src)

    destination = set()
    src2dest = [0] * n
    for src, dest in order:
        destination.add(dest)
        src2dest[src] = dest

    queue = [0]
    visited = [False] * n
    while queue:
        node = queue.pop()
        visited[node] = True
        dest = src2dest[node]
        if dest: # this node is source
            destination.remove(dest)
            if visited[dest]:
                queue.extend([adj for adj in graph[dest] if not visited[adj]])
        elif node in destination:
            continue
        queue.extend([adj for adj in graph[node] if not visited[adj]])

    return not destination