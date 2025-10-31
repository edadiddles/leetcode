from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = [1]*len(graph)

        for i in range(len(safe_nodes)):
            if safe_nodes[i] == 0:
                print(f"node not safe: ({i})")
                continue

            for j in range(len(graph[i])):
                visited_nodes = [0]*len(graph)
                print(f"starting walk: {i},{j}")
                if not self.r_walk(graph, safe_nodes, visited_nodes, graph[i][j]):
                    print(f"walk not safe: ({i})")
                    safe_nodes[i] = 0
                else:
                    print(f"walk safe")

        return [idx for idx, val in enumerate(safe_nodes) if val == 1]


    def r_walk(self, graph: List[List[int]], safe_nodes: List[int], visited_nodes: List[int], node_idx: int):
        visited_nodes[node_idx] = 1
        for i in range(len(graph[node_idx])):
            visited_nodes_cpy = visited_nodes.copy()
            if graph[node_idx][i] == node_idx:
                print(f"graph[i]==node_idx: ({node_idx}, {i})")
                safe_nodes[node_idx] = 0
                print(f"node not safe: {node_idx}")
                return False
            elif safe_nodes[graph[node_idx][i]] == 0:
                print(f"safe_nodes[i] == 0: ({node_idx},{i})")
                safe_nodes[node_idx] = 0
                print(f"node not safe: {node_idx}")
                return False
            elif visited_nodes_cpy[graph[node_idx][i]] == 1:
                print(f"visited_nodes[i] == 1: ({node_idx},{i})")
                safe_nodes[i] = 0
                print(f"node not safe: {node_idx}")
                return False

            if not self.r_walk(graph, safe_nodes, visited_nodes_cpy, graph[node_idx][i]):
                return False

        return True
