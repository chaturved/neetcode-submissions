class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        word_set.add(beginWord)

        pattern_map = defaultdict(list)
        for word in word_set:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)

        visited = {beginWord}
        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps

            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                for neighbor in pattern_map[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))

        return 0