class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans =[0]*n
        stack = []
        prev_time = 0
        for log in logs:
            fn,ident,t = log.split(":")
            fn, t = int(fn), int(t)
            
            if ident=="start":
                if stack:
                    ans[stack[-1]] += t - prev_time
                stack.append(fn)
                prev_time = t
            else:
                ans[stack.pop()] += t - prev_time + 1
                prev_time = t + 1
        return ans
        