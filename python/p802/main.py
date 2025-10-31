from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = [1]*len(graph)

        for i in range(len(safe_nodes)):
            print(safe_nodes)
            if safe_nodes[i] == 0:
                print(f"node not safe: ({i})")
                continue

            for j in range(len(graph[i])):
                visited_nodes = [0]*len(graph)
                if not self.r_walk(graph, safe_nodes, visited_nodes, graph[i][j]):
                    safe_nodes[i] = 0
                    break

        return [idx for idx, val in enumerate(safe_nodes) if val == 1]


    def r_walk(self, graph: List[List[int]], safe_nodes: List[int], visited_nodes: List[int], node_idx: int):
        print(f"visiting node: {node_idx}")
        visited_nodes[node_idx] = 1
        for i in range(len(graph[node_idx])):
            visited_nodes_cpy = visited_nodes.copy()
            if graph[node_idx][i] == node_idx:
                safe_nodes[node_idx] = 0
                print(f"node not safe: {node_idx}")
                return False
            elif safe_nodes[graph[node_idx][i]] == 0:
                safe_nodes[node_idx] = 0
                print(f"node not safe: {node_idx}")
                return False
            elif visited_nodes_cpy[graph[node_idx][i]] == 1:
                safe_nodes[node_idx] = 0
                print(f"node not safe: {node_idx}")
                return False

            if not self.r_walk(graph, safe_nodes, visited_nodes_cpy, graph[node_idx][i]):
                return False

        return True
