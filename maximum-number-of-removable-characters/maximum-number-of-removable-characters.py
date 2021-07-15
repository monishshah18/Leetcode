class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def sub_Seq(new_str,p):
            start = -1
            for i in p:
                start = new_str.find(i,start+1)
                if start==-1: return False
            return True
        ans = 0
        start, end = 0, len(removable)
        while start <= end:
            mid = (start+end)//2
            new_str = list(s)
            for i in range(mid):
                new_str[removable[i]] = ''
            new_str = ''.join(new_str)
            if sub_Seq(new_str,p):
                ans = mid
                start = mid+1
            else:
                end = mid-1
        return ans