class graph:
    def __init__(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["A"],
            "C": ["A"]
        }

    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        if v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)

    def print_graph(self):
        print(self.graph)

g = graph()
g.remove_edge("A", "B")
g.print_graph()