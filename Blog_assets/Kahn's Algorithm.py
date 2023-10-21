from collections import defaultdict

# Kahn's algorithm for topological sorting
class Graph:
    def __init__(self, vertices) -> None:
        self.graph = defaultdict(list)
        self.V = 0  # Initialize the number of vertices to 0

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = []
        if u != v:  # Avoid self-loops
            self.V = len(self.graph)  # Update the number of vertices

    def topologicalSort(self):
        in_degree = [0] * self.V
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        cnt = 0
        finalSort = []

        while queue:
            u = queue.pop(0)
            finalSort.append(u)
            for i in self.graph[u]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)
            cnt += 1

        if cnt != self.V:
            print("There is a cycle within the graph")
        else:
            print(finalSort)

sampleGraph = {"Calc3": ["Calc1", "Calc2", "PreCalc"],
               "English": [],
               "Computer Science": ["Calc2"],
               "Machine Learning": ["Computer Science"],
               "Technical Writing": ["English"]}

def graphMaker(adictionaryGraph):
    finalGraph = Graph(0)
    for key, value in adictionaryGraph.items():
        finalGraph.V += 1  # Increment the number of vertices
        for v in value:
            finalGraph.addEdge(key, v)

    return finalGraph

endGraph = graphMaker(sampleGraph)
endGraph.topologicalSort()
