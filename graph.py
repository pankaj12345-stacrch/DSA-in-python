import timeit
class Graph:
    V = 0
    adj = [[]]
    def __init__(self, v):

        self.V = v
        self.adj = [[] for i in range(v)]
    def addEdge(self, v, w):
        self.adj[v - 1].append(w - 1)
        self.adj[w - 1].append(v - 1)
    def twoEdge(self, v):
        noOfEdges = [len(self.adj[i]) for i in range(v)]
        flag = True
        for i in range(v):
            if (noOfEdges[i] < 2):
                flag = False
                break
        if (flag):
            print("Yes")
        else:
            print("No")
if __name__ == "__main__":

    # Number of nodes and edges
    V = 8
    E = 9

    # Given Edges
    edges = [[1, 2], [1, 8],
             [1, 6], [2, 3],
             [2, 4], [3, 7],
             [3, 4], [7, 5],
             [7, 6]]

    g = Graph(V)
    for i in range(E):
        g.addEdge(edges[i][0],
                  edges[i][1])
    g.twoEdge(V)
print("time",timeit.timeit())
