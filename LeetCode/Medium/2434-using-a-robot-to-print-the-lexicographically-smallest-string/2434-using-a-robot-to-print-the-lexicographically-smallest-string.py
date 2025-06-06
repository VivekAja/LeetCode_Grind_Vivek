class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)

        # Array to store the smallest character from index i to the end
        min_char_to_right = [''] * n
        min_char_to_right[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            min_char_to_right[i] = min(s[i], min_char_to_right[i + 1])

        stack = deque()
        paper = []

        i = 0
        while i < n:
            stack.append(s[i])
            min_char = min_char_to_right[i + 1] if i + 1 < n else s[i]

            while stack and stack[-1] <= min_char:
                paper.append(stack.pop())

            i += 1

        # Empty the remaining characters from the stack
        while stack:
            paper.append(stack.pop())

        return ''.join(paper)