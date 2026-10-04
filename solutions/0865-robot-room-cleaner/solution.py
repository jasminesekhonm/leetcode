# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        r, c = 0, 0 

        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]  
        visited = set()

        def go_back():
            robot.turnRight()
            robot.turnRight()       # face the opposite way
            robot.move()            # step back into the previous cell
            robot.turnRight()
            robot.turnRight()       # face the original direction again

        def dfs(robot, curr_r, curr_c, move_index):

            robot.clean()
            visited.add((curr_r, curr_c))

            for i in range(len(moves)):
                new_move_index = (move_index + i) % 4 
                dr, dc = moves[new_move_index][0], moves[new_move_index][1]
                nr, nc = curr_r + dr, curr_c + dc 
                if not (nr, nc) in visited and robot.move():
                    
                    dfs(robot, nr, nc, new_move_index)
                    go_back()
                
                robot.turnRight() # reset move 

        
        dfs(robot, r, c, 0)


        
