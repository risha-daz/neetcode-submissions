class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in prerequisites:
            if i[1] in adj:
                adj[i[1]]+=[i[0]]
            else:
                adj[i[1]] = [i[0]]
        exp_state = {_:0 for _ in range(numCourses)}

        def dfs(node):
            if exp_state[node] == 2:
                return True
            exp_state[node] = 1
            if node in adj: 
                for i in adj[node]:
                    if exp_state[i] == 1:
                        return False
                    if not dfs(i):
                        return False
            exp_state[node] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            
            





