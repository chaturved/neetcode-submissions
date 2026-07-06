class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)
        letters = set()
        for w in words:
            letters.update(w)

        for i in range(len(words) - 1):
            word1, length1 = words[i], len(words[i])
            word2, length2 = words[i + 1], len(words[i + 1])

            found = False
            for j in range(min(length1, length2)):
                if word1[j] != word2[j]:
                    adj[word1[j]].append(word2[j])
                    found = True
                    break
            
            if found or word2.startswith(word1):
                continue
            
            return ""
        
        result = []
        def dfs(u):
            if u in global_visited:
                return True
            
            if u in visited:
                return False
            
            visited.add(u)
            
            for v in adj[u]:
                if not dfs(v):
                    return False
            
            global_visited.add(u)
            result.append(u)
            return True

        global_visited = set()
        for u in letters:
            if u in global_visited:
                continue
            
            visited = set()
            if not dfs(u):
                return ""

        return "".join(result[::-1])