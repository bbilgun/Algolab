from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends)
        if "0000" in dead_set:
            return -1
        
        queue = deque([("0000", 0)])  
        visited = set("0000") 
        
        while queue:
            current, turns = queue.popleft()
            
            if current == target:
                return turns
            
            for i in range(4):
                for move in [-1, 1]:
                    next_state = list(current)
                    next_state[i] = str((int(next_state[i]) + move) % 10)
                    next_state = "".join(next_state)
                    
                    if next_state not in visited and next_state not in dead_set:
                        queue.append((next_state, turns + 1))
                        visited.add(next_state)
        
        return -1
