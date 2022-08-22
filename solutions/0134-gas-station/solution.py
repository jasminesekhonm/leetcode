class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        numStations = len(gas)
        
        startingStation = 0 
        
        currentTank, totalTank = 0, 0
        
        for i in range(numStations):
            currentTank += gas[i] - cost[i]
            totalTank += gas[i] - cost[i]
            if currentTank < 0:
                startingStation = i + 1
                currentTank = 0
        return startingStation if totalTank >= 0 else -1 
            
                
                
                
                
