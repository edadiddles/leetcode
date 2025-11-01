from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        unsafe_nodes = [False]*len(graph)
        visited_nodes = [False]*len(graph)

        for i in range(len(graph)):
            self.r_walk(graph, unsafe_nodes, visited_nodes, i)

        return [idx for idx, val in enumerate(unsafe_nodes) if not val]


    def r_walk(self, adj_list: List[List[int]], unsafe_nodes: List[int], visited_nodes: List[int], node_idx: int):
        if unsafe_nodes[node_idx]:
            return True
        elif visited_nodes[node_idx]:
            return False

        visited_nodes[node_idx] = True
        unsafe_nodes[node_idx] = True
        for n in adj_list[node_idx]:
            if self.r_walk(adj_list, unsafe_nodes, visited_nodes, n):
                return True

        unsafe_nodes[node_idx] = False
        return False
