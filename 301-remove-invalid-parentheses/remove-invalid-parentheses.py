class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        def is_valid(string):
            balance = 0
            for char in string:
                if char == '(':
                    balance += 1
                elif char ==')':
                    balance -= 1

                    if balance < 0:
                        return  False
            return balance == 0
        
        queue = deque([s])
        visited = {s}
        result = []

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                curr = queue.popleft()

                if is_valid(curr):
                    result.append(curr)
                
                if result:
                    continue
                
                for i in range(len(curr)):
                    if curr[i] not in "()":
                        continue
                    
                    new_string = curr[:i] + curr[i+1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append(new_string)

        if result:
            return result
        return [""]
        