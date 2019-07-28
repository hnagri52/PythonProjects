class Solution:
    
    def numJewelsInStones(self, J, S):
        self.counter = 0;
        for jewls in J:
            for stones in S:
                if jewls == stones:
                    self.counter = self.counter + 1;
            
        
        return self.counter;
