import networkx as nx

graph = nx.Graph()
graph.add_nodes_from(['put', 'but', 'cut', 'cat', 'bug', 'big', 'pug', 'pig'])
graph.add_edges_from(
    [('put', 'cut'),
     ('put', 'but'),
     ('but', 'cut'),
     ('but', 'put'),
     ('but', 'bug'),
     ('cut', 'but'),
     ('cut', 'cat'),
     ('cut', 'put'),
     ('cat', 'cut'),
     ('bug', 'but'),
     ('bug', 'big'),
     ('big', 'bug'),
     ('put', 'pug'),
     ('pig', 'pug'),
     ('pig', 'big')])
print(nx.shortest_path(graph, 'cat', 'big'))
print(*nx.all_shortest_paths(graph, 'put', 'big'))
