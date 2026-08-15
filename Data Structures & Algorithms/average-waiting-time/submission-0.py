class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_waiting_time = 0
        completes_at = 0
        for arrival, time in customers:
            completes_at = max(arrival, completes_at) + time
            waiting_time = completes_at - arrival
            total_waiting_time += waiting_time
        
        return total_waiting_time / len(customers)

