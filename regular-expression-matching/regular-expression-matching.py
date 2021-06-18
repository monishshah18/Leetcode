class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.helper(s, p)

    def helper(self, s, p):
        '''
        helper function which checks for string matching
        '''
        if not p: return not s
        match = True if s and p[0] in (".", s[0]) else False
        return (len(p) >= 2 and p[1] == "*" and (self.helper(s, p[2:]) or match and self.helper(s[1:], p))) \
    or match and self.helper(s[1:], p[1:])  