from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = [-1]*len(graph)

        for i in range(len(safe_nodes)):
            if safe_nodes[i] == 0:
                continue
            elif safe_nodes[i] == 1:
                continue

            visited_nodes_master = [0]*len(graph)
            for j in range(len(graph[i])):
                visited_nodes = [0]*len(graph)
                if not self.r_walk(graph, safe_nodes, visited_nodes, graph[i][j]):
                    safe_nodes[i] = 0
                    break
                else:
                    for idx in range(len(visited_nodes)):
                        if visited_nodes[idx] == 1:
                            visited_nodes_master[idx] = 1

            if safe_nodes[i] == -1:
                safe_nodes[i] = 1
                for idx in range(len(visited_nodes_master)):
                    if visited_nodes_master[idx] == 1:
                        safe_nodes[idx] = 1

        return [idx for idx, val in enumerate(safe_nodes) if val == 1]


    def r_walk(self, graph: List[List[int]], safe_nodes: List[int], visited_nodes: List[int], node_idx: int):
        visited_nodes[node_idx] = 1
        if safe_nodes[node_idx] == 1:
            for idx in range(len(visited_nodes)):
                if visited_nodes[idx] == 1:
                    safe_nodes[idx] = 1
            return True
        elif safe_nodes[node_idx] == 0:
            for idx in range(len(visited_nodes)):
                if visited_nodes[idx] == 1:
                    safe_nodes[idx] = 0
            return False

        for i in range(len(graph[node_idx])):
            visited_nodes_cpy = visited_nodes.copy()
            if graph[node_idx][i] == node_idx:
                for idx in range(len(visited_nodes)):
                    if visited_nodes[idx] == 1:
                        safe_nodes[idx] = 0
                return False
            elif safe_nodes[graph[node_idx][i]] == 0:
                for idx in range(len(visited_nodes)):
                    if visited_nodes[idx] == 1:
                        safe_nodes[idx] = 0
                return False
            elif visited_nodes_cpy[graph[node_idx][i]] == 1:
                for idx in range(len(visited_nodes)):
                    if visited_nodes[idx] == 1:
                        safe_nodes[idx] = 0
                return False

            if not self.r_walk(graph, safe_nodes, visited_nodes_cpy, graph[node_idx][i]):
                return False

        return True
