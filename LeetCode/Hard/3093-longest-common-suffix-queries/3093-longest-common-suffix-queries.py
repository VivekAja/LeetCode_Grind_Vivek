class Trie:
    def __init__(self):
        self.children = {}
        self.besti = -1


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = Trie()
        

        n = float('inf')
        global_best_index = -1
        
        for i, word in enumerate(wordsContainer):
            if len(word) < n:
                n = len(word)
                global_best_index = i
        
        root.besti = global_best_index


        for i, word in enumerate(wordsContainer):
            curr = root

            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = Trie()
                curr = curr.children[char]

                if curr.besti == -1:
                    curr.besti = i
                else:
                    curr_best_len = len(wordsContainer[curr.besti])
                    if len(word) < curr_best_len:
                        curr.besti = i


        ans = []
        for query in wordsQuery:
            curr = root

            for char in reversed(query):
                if char in curr.children:
                    curr = curr.children[char]
                else:
 
                    break

            ans.append(curr.besti)
            
        return ans

        