class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == "" and needle == "":
            return 0
        try:
            return haystack.index(needle)
        except:
            return -1
            