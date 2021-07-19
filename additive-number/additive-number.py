class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        length = len(num)
        for i in range(1, length//2+1):
            for j in range(1, (length-i)//2+1):
                first, second, others = num[:i],num[i:i+j],num[i+j:]
                if (len(first) > 1 and first[0] == "0") or (len(second) > 1 and second[0] == "0"):
                    continue
                while others:
                    sum_str = str(int(first)+int(second))
                    if sum_str == others:
                        return True
                    elif others.startswith(sum_str):
                        first,second,others = second,sum_str,others[len(sum_str):]
                    else:
                        break
        return False    
            
        