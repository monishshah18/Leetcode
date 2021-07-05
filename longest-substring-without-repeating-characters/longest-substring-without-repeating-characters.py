class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longString = ""
        llString = 0
        for i in s:
            index = longString.find(i)
            if index > -1:
                llString = max(llString, len(longString))
                longString += i
                longString = longString[index+1:]
            else:
                longString += i
            llString = max(llString, len(longString))
        return llString
        