class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen = set()
            for c in range(9):
                value = board[r][c]   
                if value in seen:
                    return False
                elif value != ".":
                    seen.add(value)
        
        for c in range(9):
            seen = set()
            for r in range(9):
                value = board[r][c]
                if value in seen:
                    return False
                elif value != ".":
                    seen.add(value)

        for r_start in range(0, 9, 3):
            for c_start in range(0, 9, 3):
                seen = set()
                for r in range(r_start, r_start + 3):
                    for c in range(c_start, c_start + 3):
                        value = board[r][c]
                        if value in seen:
                            return False
                        elif value != ".":
                            seen.add(value)
        return True
        



