class Solution(object):
    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # Step 1: Generate all valid states for a single column
        valid_column_states = []
        # current_path stores the colors for the current column being built
        current_path = [-1] * m  # -1 indicates not yet colored

        def generate_states_dfs(row_idx):
            """
            Recursively generates all valid colorings for a single column.
            A column is valid if no two vertically adjacent cells have the same color.
            """
            if row_idx == m:
                # If all m rows are colored, add a copy of the path to valid states
                valid_column_states.append(tuple(current_path))
                return

            # Try assigning each of the 3 colors (0, 1, 2) to the current cell
            for color in range(3):
                # Check vertical constraint: color must be different from the one above
                if row_idx > 0 and current_path[row_idx - 1] == color:
                    continue  # Skip if color is same as cell above
                
                current_path[row_idx] = color
                generate_states_dfs(row_idx + 1)
                # Backtracking is implicit: current_path[row_idx] will be overwritten
                # in the next iteration or when the function returns.

        generate_states_dfs(0)
        
        num_states = len(valid_column_states)

        # If m is such that no valid column state exists (e.g., m=1, 0 colors - not this problem)
        # or if n=0 (though constraints say n>=1)
        if num_states == 0:
            return 0

        # Step 2: Precompute compatibility between column states
        # adj[state1_idx] stores a list of state2_idx such that
        # state1 can be immediately followed by state2 in adjacent columns.
        adj = [[] for _ in range(num_states)]
        for i in range(num_states):
            state1 = valid_column_states[i]
            for j in range(num_states):
                state2 = valid_column_states[j]
                
                # Check horizontal compatibility
                compatible = True
                for r in range(m): # For each row in the column
                    if state1[r] == state2[r]:
                        compatible = False
                        break
                
                if compatible:
                    adj[i].append(j)

        # Step 3: Dynamic Programming
        # dp[state_idx] = number of ways to color the current column with state_idx
        # Initialize for the first column (column 0)
        # Each valid state is one way to color the first column.
        dp = [1] * num_states 

        # Iterate for the remaining n-1 columns (from column 1 to n-1)
        for _col_num in range(1, n):
            new_dp = [0] * num_states # DP values for the current column being calculated
            for prev_state_idx in range(num_states):
                # If there are no ways to reach prev_state_idx, it can't contribute
                if dp[prev_state_idx] == 0:
                    continue
                
                # For each state (curr_state_idx) that can follow prev_state_idx
                for curr_state_idx in adj[prev_state_idx]:
                    new_dp[curr_state_idx] = (new_dp[curr_state_idx] + dp[prev_state_idx]) % MOD
            
            dp = new_dp # Move to the next column

        # Step 4: Calculate the final result
        # The total number of ways is the sum of ways to color the last column
        # with any valid state.
        total_ways = sum(dp) % MOD
        
        return total_ways 