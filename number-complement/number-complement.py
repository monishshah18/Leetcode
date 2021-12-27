class Solution:
    def findComplement(self, num: int) -> int:
        mask_len=len(bin(num))-2
        mask=int("1"*mask_len,2)
        return mask^num