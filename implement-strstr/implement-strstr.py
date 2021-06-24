class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == "" and needle == "":
            return 0
        try:
            temp = haystack.index(needle)
            return temp
        except:
            return -1
        # if temp:
        #     return temp
        