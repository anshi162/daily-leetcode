class RandomizedSet:

    def __init__(self):
        self.s=[]
        

    def insert(self, val: int) -> bool:
        s=self.s
        if val not in self.s:
            self.s.append(val)
            return True
        else:
            return False      

    def remove(self, val: int) -> bool:
        if val in self.s:
            self.s.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        
        return random.choice(self.s)
