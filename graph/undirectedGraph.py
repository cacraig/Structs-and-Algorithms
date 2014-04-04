'''''
All of the graphs arcs are as follows:

    A -> B
    A -> C
    B -> C
    B -> D
    C -> D
    D -> C
    E -> F
    F -> C

'''''


# This graph has 6 nodes, and 8 arcs.
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

def findPath(graph, start, end, path=[]):
  path = path + [start]
  
  if start == end:
    return path
  if not graph.has_key(start):
    return None

  for node in graph[start]:
    if node not in path:
      newPath = findPath(graph, node, end, path)
      if newPath:
        return newPath
  return None

def findAllPaths(graph, start, end, path=[]):
  # add node to this path.
  path = path + [start]
  
  # if we have reached the same node, return our path.
  if start == end:
    return path
  # if the graph does not contain our node, return no path.
  if not graph.has_key(start):
    return None

  paths = []
  
  # begin at start node, iterate through graph.
  # recursively execute findAllPaths until path contains the passed node.

  for node in graph[start]:
    if node not in path:
      newPaths = findAllPaths(graph, node, end, path)
      for newPath in newPaths:
        paths.append(newPath)
  return paths

def findShortestPath(graph, start, end, path = []):
  # add node to this path.
  path = path + [start]

  # if we have reached the same node, return our path.
  if start == end:
    return path
  # if the graph does not contain our node, return no path.
  if not graph.has_key(start):
    return None

  shortest = None

  for node in graph[start]:
    if node not in path:
      newPath = findShortestPath(graph, node, end, path)
      if newPath:
        if not shortest or len(newPath) < len(shortest):
          shortest = newPath
  
  return shortest

# Find path from Node A to Node D.
print findPath(graph, 'A', 'D')

# Find all paths from Node A to Node D.
print findAllPaths(graph, 'A', 'D')

# Find the shortest path from Node A to Node D
print findShortestPath(graph, 'A', 'D')
