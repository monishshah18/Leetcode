class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        def con2min(time):
            t = [0,0]
            t[0], t[1] = map(int, time.split(":"))
            t = 60*t[0]+t[1]
            return t
        s = con2min(startTime)
        f = con2min(finishTime)
        if s < f:
            return int(floor(f/15)-ceil(s/15))
        else:
            return int(floor(f/15)+con2min("24:00")/15-ceil(s/15))