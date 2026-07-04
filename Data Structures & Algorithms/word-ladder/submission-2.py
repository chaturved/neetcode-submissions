class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def is_transformable(word1, word2):
            diff_count = sum(c1 != c2 for c1, c2 in zip(word1, word2))
            return diff_count == 1
        
        adj = defaultdict(list)
        if beginWord not in wordList:
            wordList.append(beginWord)

        length = len(wordList)
        for i in range(length):
            for j in range(i + 1, length):
                if is_transformable(wordList[i], wordList[j]):
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        
        visited = {beginWord}
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            for neighbor in adj[word]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
        
        return 0