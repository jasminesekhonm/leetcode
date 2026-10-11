from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        for (a, b, price) in flights:
            graph[a].append((b, price))
        
        q = deque([(src,0, 0)])

        min_prices = {}

        while q:
            curr_city, curr_price, stops = q.popleft()
            if stops == k+1:
                continue
            for (next_city, flight_price) in graph[curr_city]:
                if next_city in min_prices and min_prices[next_city] <= curr_price+flight_price:
                    continue
                q.append((next_city, curr_price+flight_price, stops+1))
                min_prices[next_city] = curr_price+flight_price
            
        return min_prices[dst] if dst in min_prices else -1



