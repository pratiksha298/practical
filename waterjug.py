from collections import deque

def water_jug_bfs(capacity_a, capacity_b, target):
    visited = set()
    queue = deque([(0, 0)])  
    path = {(0, 0): None}  
    

    while queue:
        a, b = queue.popleft()

        if a == target or b == target:
            result_path = []
            current_state = (a, b)
            while current_state is not None: 
                result_path.append(current_state)
                current_state = path[current_state] 
            return result_path[::-1] 
        if (a, b) in visited:
            continue
        visited.add((a, b))

        possible_moves = [
            (capacity_a, b),  
            (a, capacity_b),  
            (0, b),           
            (a, 0),           
            (a - min(a, capacity_b - b), b + min(a, capacity_b - b)),  
            (a + min(b, capacity_a - a), b - min(b, capacity_a - a))   
        ]

        for new_state in possible_moves:
            if new_state not in visited and new_state not in path:
                queue.append(new_state)
                path[new_state] = (a, b)  
    
    return "No solution found"

if __name__ == "__main__":
    capacity_a = 4
    capacity_b = 3
    target = 2

    solution = water_jug_bfs(capacity_a, capacity_b, target)
    
    print("Steps to reach the target:")
    if isinstance(solution, str):
        print(solution)
    else:
        for step in solution:
            print(step)
