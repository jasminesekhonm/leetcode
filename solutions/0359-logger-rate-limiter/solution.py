class Logger:

    def __init__(self):
        self.dict = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.dict or (timestamp - self.dict[message]) >= 10:
            self.dict[message] = timestamp
            return True 
        return False

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
