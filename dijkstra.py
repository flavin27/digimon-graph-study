import heapq
import json
import os


class Node:
    def __init__(self, value):
        self.neighbors = []
        self.value = value
        self.color = "white"
        self.pi = None
        self.d = float("inf")
        self.cc = 0
        self.f = float("inf")


class Graph:
    def __init__(self):
        self.nodes = []
        self.origin = None
        self.cycle = False

    def add_node(self, value):
        n = Node(value)
        self.nodes.append(n)
        return n

    def add_edge(self, u, v, cost=0):
        u.neighbors.append((v, cost))

    def create_graph(self, evolution_data, cost_data):
        evolutions = json.loads(evolution_data)
        costs = json.loads(cost_data)
        node_map = {}

        for digimon, targets in evolutions.items():
            if digimon not in node_map:
                node_digimon = self.add_node(digimon)
                node_map[digimon] = node_digimon
            else:
                node_digimon = node_map[digimon]

            for target in targets:
                if target not in node_map:
                    node_target = self.add_node(target)
                    node_map[target] = node_target
                else:
                    node_target = node_map[target]

                cost = costs.get(target, 0)
                self.add_edge(node_digimon, node_target, cost)

    def dijkstra(self, origin_value):
        for u in self.nodes:
            u.d = float("inf")
            u.pi = None
            u.color = "white"

        origin_node = next((n for n in self.nodes if n.value == origin_value), None)
        if origin_node is None:
            print(f"Origin {origin_value} not found in graph.")
            return

        origin_node.d = 0

        counter = 0
        pq = [(0, counter, origin_node)]

        while pq:
            dist_u, _, u = heapq.heappop(pq)

            if u.color == "black":
                continue

            u.color = "black"

            for v, cost in u.neighbors:
                if v.color != "black":
                    new_dist = u.d + cost
                    if new_dist < v.d:
                        v.d = new_dist
                        v.pi = u
                        v.color = "gray"
                        counter += 1
                        heapq.heappush(pq, (new_dist, counter, v))



graph = Graph()

evolution_file = os.path.join(os.path.dirname(__file__), 'digimon.json')
cost_file = os.path.join(os.path.dirname(__file__), 'costs.json')

with open(evolution_file, 'r') as f:
    evolution_data = f.read()

with open(cost_file, 'r') as f:
    cost_data = f.read()

graph.create_graph(evolution_data, cost_data)
print(f"Total Digimons: {len(graph.nodes)}")

origin = input("Insert the origin Digimon (ex: Agumon): ").capitalize()
print("\n" + "="*50)
print(f"Running Dijkstra from {origin}")
print("="*50)
graph.dijkstra(origin)

print(f"\nMinimum distances from {origin}:")
print("-" * 50)
distances = sorted([(n.value, n.d) for n in graph.nodes], key=lambda x: x[1])

for digimon, dist in distances:
    if dist == float("inf"):
        print(f"{digimon}: unreachable")
    else:
        print(f"{digimon}: {dist} key points")
