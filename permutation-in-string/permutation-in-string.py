class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        from collections import Counter
        d1 = Counter(s1)
        
        # initial window
        window = s2[:k]
        d2 = Counter(window)
        
        # check the intial window 
        if d1 == d2:
            return True
  
        for i in range(len(s2)-k):
        
            # SLIDE THE WINDOW
            # 1 - remove s2[i]
            if d2[s2[i]] == 1:
                del d2[s2[i]]
            elif d2[s2[i]] > 1:
                d2[s2[i]] -= 1
            
            # 2- add s2[i+k]
            if s2[i+k] in d2:
                d2[s2[i+k]] += 1
            else:
                d2[s2[i+k]] = 1
                
            # check after sliding
            if d1 == d2:
                return True
                
        return False