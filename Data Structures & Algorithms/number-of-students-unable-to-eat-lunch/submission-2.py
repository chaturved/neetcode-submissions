class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        freq_students = Counter(students)
        
        for i, sandwich in enumerate(sandwiches):
            if freq_students[sandwich] == 0:
                return len(sandwiches) - i
            freq_students[sandwich] -= 1
        
        return 0