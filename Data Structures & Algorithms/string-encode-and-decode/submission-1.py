class Solution:
    lst = []
    def encode(self, strs: List[str]) -> str:
        self.lst = strs

    def decode(self, s: str) -> List[str]:
        return self.lst