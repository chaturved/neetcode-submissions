class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for folder_element in folder:
            trie.add(folder_element)
        
        res = []
        for folder_element in folder:
            if not trie.isSubFolder(folder_element):
                res.append(folder_element)
        
        return res

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_dir = False


class Trie:
    def __init__(self):
        self.head = TrieNode()
    
    def add(self, folder_element):
        curr = self.head
        for folder in folder_element.split("/"):
            if folder not in curr.children:
                curr.children[folder] = TrieNode()
            curr = curr.children[folder]
        
        curr.end_dir = True
    
    def isSubFolder(self, folder_element):
        curr = self.head
        parts = folder_element.split("/")
        for i, folder in enumerate(parts):
            curr = curr.children[folder]
            if curr.end_dir and i < len(parts) - 1:
                return True
            
        return False


            