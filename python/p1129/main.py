from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        shortest_paths = [-1]*n

        self.r_walk(0, 0, shortest_paths, redEdges, blueEdges)
        self.r_walk(0, 0, shortest_paths, blueEdges, redEdges)
        return shortest_paths


    def r_walk(self, n: int, depth: int, shortest_paths: List[int], primary_edges: List[List[int]], secondary_edges: List[List[int]]):
        print(f"depth: {depth}, shortest_paths: {shortest_paths}, primary_edges: {primary_edges}, secondary_edges: {secondary_edges}")
        if depth >= len(shortest_paths):
            return

        shortest_paths[n] = depth
        for i in range(len(primary_edges)):
            if primary_edges[i][0] != n:
                continue

            self.r_walk(primary_edges[i][1], depth+1, shortest_paths, secondary_edges, [edge for k, edge in enumerate(primary_edges) if i != k])
