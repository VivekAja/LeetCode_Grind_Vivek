from collections import Counter
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
                # Inner function to calculate the minimum deletions required for a given threshold
        def f(threshold: int) -> int:
            deletions = 0
            for frequency in frequencies:
                # If frequency is less than the threshold, we need to delete all occurrences
                if frequency < threshold:
                    deletions += frequency
                # If frequency is greater than the threshold plus k, delete the excess
                elif frequency > threshold + k:
                    deletions += frequency - threshold - k
            return deletions

        # Get a list of the frequencies of each character in the word
        frequencies = Counter(word).values()
        # Calculate and return the minimum deletions for all possible threshold values
        return min(f(threshold) for threshold in range(len(word) + 1))