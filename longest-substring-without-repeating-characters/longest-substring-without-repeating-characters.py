class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longString = ""
        longCount = 0
        for i in s:
            st_index = longString.find(i)
            if st_index > -1:
                longCount = max(longCount, len(longString))
                longString += i
                longString = longString[st_index+1:]
            else:
                longString += i
            longCount = max(longCount, len(longString))
        return longCount