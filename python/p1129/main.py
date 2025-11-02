from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        shortest_paths = [-1]*n
        redEdges.sort(key=lambda x: x[0])
        blueEdges.sort(key=lambda x: x[0])

        self.r_walk([0], 0, shortest_paths, [False]*n, [False]*n, redEdges, blueEdges)
        self.r_walk([0], 0, shortest_paths, [False]*n, [False]*n, blueEdges, redEdges)
        return shortest_paths


    def r_walk(self, nodes: List[int], depth: int, shortest_paths: List[int], visited_primary: List[int], visited_secondary: List[int], primary_edges: List[List[int]], secondary_edges: List[List[int]]):
        if len(nodes) == 0:
            return

        next_edges = primary_edges if depth%2 == 0 else secondary_edges
        visited = visited_primary if depth%2 == 0 else visited_secondary

        q = []
        for node in nodes:
            if visited[node]:
                continue

            visited[node] = True
            if shortest_paths[node] == -1 or shortest_paths[node] > depth:
                shortest_paths[node] = depth

            for next_edge in next_edges:
                if node > next_edge[0]:
                    continue
                if node < next_edge[0]:
                    break

                q.append(next_edge[1])

        self.r_walk(q, depth+1, shortest_paths, visited_primary, visited_secondary, primary_edges, secondary_edges)
