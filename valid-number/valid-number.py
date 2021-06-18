import re
class Solution:
    def isNumber(self, s: str) -> bool:
        if(re.compile('^([+-]?(((\d+\.\d*)|(\.\d+))|(\d+))([eE][+-]?\d+)?)$').match(s) == None):
            return False
        return True;
        