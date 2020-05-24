class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def addEdge(self, src, dest):
        node = AdjNode(dest)        #Adding node to the source node
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)         #Adding the source node to destination node as it is undirected graph.
        node.next = self.graph[dest]
        self.graph[dest] = node

    def printGraph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(' \n')
if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.addEdge(0, 1)
    graph.addEdge(0, 4)
    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(1, 4)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)

    graph.printGraph()
